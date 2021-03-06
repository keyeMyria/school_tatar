# -*- coding: utf-8 -*-
import time
import socket
import copy
import datetime
import json
from lxml import etree
import urllib2
from django.conf import settings
from django.shortcuts import HttpResponse, render, get_object_or_404, Http404, redirect, urlresolvers
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.utils.html import strip_tags
from libcms.libs.common.xslt_transformers import xslt_bib_draw_transformer
from zgate.models import ZCatalog
from zgate import zworker

from urt.models import LibReader
from sso_ruslan import models as sso_ruslan_models
from participants.models import Library
from thread_worker import ThreadWorker
from order_manager.manager import OrderManager
from forms import DeliveryOrderForm, CopyOrderForm, MailOrderForm
from ssearch.models import Record, Ebook
from ssearch.rusmarc_template import beautify
from ssearch.models import get_records
from order_manager.ill import ILLRequest
from ..templatetags.order_tags import org_by_id
from ..models import UserOrderTimes

DEFAULT_FROM_EMAIL = getattr(settings, 'DEFAULT_FROM_EMAIL', '')
RUSLAN_ORDER = getattr(settings, 'RUSLAN_ORDER', {})
RUSLAN_ORDER_URLS = RUSLAN_ORDER.get('urls', {})
RUSLAN_ORDER_SERVERS = RUSLAN_ORDER.get('checked_servers', [])

RUSLAN = getattr(settings, 'RUSLAN', {})
RUSLAN_USERNAME = RUSLAN.get('username', '')
RUSLAN_PASSWORD = RUSLAN.get('password', '')


def set_cookies_to_response(cookies, response, domain=None):
    for key in cookies:
        response.set_cookie(key, cookies[key], domain=domain)
    return response


class MBAOrderException(Exception):
    pass


@login_required
def index(request):
    links = LibReader.objects.select_related('library').filter(user=request.user)
    return render(request, 'orders/frontend/index.html', {
        'links': links,
    })


@login_required
def books_on_hand(request):
    """
    Выданные книги.
    Отображение списка библиотек и книг, которые были выданы в соответствующих библиотека
    """
    ruslan_user = sso_ruslan_models.get_ruslan_user(request)
    if ruslan_user:
        libraries = list(Library.objects.filter(z_service__gt=''))

        args = []
        for library in libraries:
            args.append({'id': library.id, 'url': RUSLAN_ORDER_URLS['books'] % (
                RUSLAN_USERNAME, RUSLAN_PASSWORD, library.z_service, ruslan_user.username)})

        results = ThreadWorker(_get_content, args).do()
        for result in results:
            for library in libraries:
                if hasattr(result, 'value') and library.id == result.value['id']:
                    if 'result' in result.value:
                        library.books = _get_books(result.value['result'])
                    if 'exception' in result.value:
                        if type(result.value['exception']) == socket.timeout:
                            library.error = u'Сервер с заказами недоступен'
                        else:
                            raise result.value['exception']
    else:
        libraries = []
    return render(request, 'orders/frontend/on_hand.html', {
        'libraries': libraries,
    })


@login_required
def reservations(request):
    ruslan_user = sso_ruslan_models.get_ruslan_user(request)
    if ruslan_user:
        libraries = list(Library.objects.filter(z_service__gt=''))

        args = []
        for library in libraries:
            args.append({'id': library.id, 'url': RUSLAN_ORDER_URLS['orders'] % (
                RUSLAN_USERNAME, RUSLAN_PASSWORD, library.z_service, ruslan_user.username)})

        results = ThreadWorker(_get_content, args).do()
        for result in results:
            for library in libraries:
                if hasattr(result, 'value') and library.id == result.value['id']:
                    if 'result' in result.value:
                        library.reservations = _get_orders(result.value['result'])
                    if 'exception' in result.value:
                        if type(result.value['exception']) == socket.timeout:
                            library.error = u'Сервер с заказами недоступен'
                        else:
                            raise result.value['exception']
    else:
        libraries = []
    return render(request, 'orders/frontend/reservations.html', {
        'libraries': libraries,
    })


@login_required
def books_on_hand_in_lib(request, id):
    library = get_object_or_404(Library, id=id)
    lib_reader = get_object_or_404(LibReader, library=library, user=request.user)

    if not library.z_service:
        return HttpResponse(
            u'Отсутвуют параметры связи с базой заказаов библиотеки. Если Вы видите это сообщение, пожалуйста, сообщите администратору портала.')
    books = _get_content('http://www.unilib.neva.ru/cgi-bin/zurlcirc?z39.50r://8007756:a6Tka0l1@ruslan.ru/circ?8007756')
    books = _get_books(books)
    return render(request, 'orders/frontend/on_hand_in_lib.html', {
        'books': books
    })


@login_required
def lib_orders(request, id):
    library = get_object_or_404(Library, id=id)
    if not library.z_service:
        return HttpResponse(
            u'Отсутвуют параметры связи с базой заказаов библиотеки. Если Вы видите это сообщение, пожалуйста, сообщите администратору портала.')

    # lib_reader = get_object_or_404(LibReader, library=library, user=request.user)
    #
    # urls = [
    #     RUSLAN_ORDER_URLS['orders'] % (
    #         lib_reader.lib_login, lib_reader.lib_password, library.z_service, lib_reader.lib_login),
    #     RUSLAN_ORDER_URLS['books'] % (
    #         lib_reader.lib_login, lib_reader.lib_password, library.z_service, lib_reader.lib_login),
    # ]

    ruslan_user = get_object_or_404(sso_ruslan_models.RuslanUser, user=request.user)

    urls = [
        RUSLAN_ORDER_URLS['orders'] % (
            ruslan_user.username, ruslan_user.password, library.z_service, ruslan_user.username),
        RUSLAN_ORDER_URLS['books'] % (
            ruslan_user.username, ruslan_user.password, library.z_service, ruslan_user.username),
    ]

    results = ThreadWorker(_get_content, urls).do()
    for result in results:
        if isinstance(result, BaseException):
            raise result
            #    print results[0].value
    orders = _get_orders(results[1].value)
    books = _get_books(results[0].value)

    return render(request, 'orders/frontend/lib_orders.html', {
        'orders': orders,
        'books': books,
        'library': library
    })


@login_required
def zorder(request, library_id):
    record_id = request.GET.get('id', None)
    if not record_id:
        raise Http404()
    library = get_object_or_404(Library, id=library_id)

    # проверяем, привязан ли zgate к библиотеке чтобы можно было перенаправить на него
    try:
        zcatalog = ZCatalog.objects.get(latin_title=library.code)
    except ZCatalog.DoesNotExist:
        return HttpResponse(u'Библиотека не может принимать электронные заказы')

    # ищем связь пользователя с библиотекой, чтобы автоматически авторизовать для заказа
    # иначе перенаправляем для установления связи

    # try:
    #     lib_reader = LibReader.objects.get(user=request.user, library=library)
    # except LibReader.DoesNotExist:
    #     back = request.get_full_path()
    #     return redirect(urlresolvers.reverse('urt:frontend:auth', args=[library_id]) + '?back=' + back)
    try:
        ruslan_user = sso_ruslan_models.RuslanUser.objects.get(user=request.user)
    except sso_ruslan_models.RuslanUser.DoesNotExist:
        return HttpResponse(u'Необходимо войти под учетной записью читателя')

    (zgate_form, cookies) = zworker.get_zgate_form(
        zgate_url=zcatalog.url,
        xml=zcatalog.xml,
        xsl=zcatalog.xsl,
        cookies=request.COOKIES,
        username=ruslan_user.username,
        password=ruslan_user.password,
    )
    session_id = zworker.get_zgate_session_id(zgate_form)
    form_params = zworker.get_form_dict(zgate_form)
    if form_params.has_key('scan'):
        del (form_params['scan'])  # удаляем, иначе происходит сканирование :-)
    form_params['use_1'] = '12:1.2.840.10003.3.1'
    form_params['term_1'] = record_id
    (result, cookies) = zworker.request(zcatalog.url, data=form_params, cookies=cookies)
    print(zcatalog.url)
    # анализируем полученный html на содержание текса с идентификатором записи - значит нашли
    if result.decode('utf-8').find(u'id="%s' % (record_id,)) >= 0:
        #        link = reverse('zgate_index', args=(catalog.id,)) + '?zstate=preorder+%s+1+default+1+1.2.840.10003.5.28+rus' % session_id
        link = zcatalog.url + '?preorder+%s+1+default+1+1.2.840.10003.5.28+rus' % session_id
        resp = redirect(link)
        set_cookies_to_response(cookies, resp, domain='.kitap.tatar.ru')
        return resp
    return HttpResponse(u'Zgate order')


@login_required
def mail_order(request, library_id, gen_id):
    reader_id = ''
    try:
        ruslan_user = sso_ruslan_models.RuslanUser.objects.get(user=request.user)
        reader_id = ruslan_user.username
    except sso_ruslan_models.RuslanUser.DoesNotExist:
        pass
    library = get_object_or_404(Library, id=library_id)
    if not library.ext_order_mail:
        return HttpResponse(u'Организация не может принимать заказы на бронирование')
    records = get_bib_records([gen_id])
    if not records:
        raise Http404(u'Запись не найдена')
    record = records[0]
    if request.method == 'POST':
        form = MailOrderForm(request.POST)
        if form.is_valid():
            lines = []
            lines.append(
                u' '.join([u'Запись:', strip_tags(record['card'].decode('utf-8'))])
            )
            lines.append("\n")
            lines.append(
                u' '.join([u'Фамилия:', form.cleaned_data.get('last_name', u'не указано')])
            )
            lines.append(
                u' '.join([u'Имя:', form.cleaned_data.get('first_name', u'не указано')])
            )
            lines.append(
                u' '.join([u'Отчество:', form.cleaned_data.get('patronymic_name', u'не указано')])
            )
            lines.append(
                u' '.join([u'Номер чит. билета:', form.cleaned_data.get('reader_id', u'не указано')])
            )
            lines.append(
                u' '.join([u'Email:', form.cleaned_data.get('email', u'не указано')])
            )
            lines.append(
                u' '.join([u'Телефон:', form.cleaned_data.get('phone', u'не указано')])
            )
            lines.append(
                u' '.join([u'Комментарии:', form.cleaned_data.get('comments', u'не указано')])
            )

            send_mail(
                u'Заказ на бронирование',
                u"\n".join(lines),
                DEFAULT_FROM_EMAIL,
                [library.ext_order_mail],
                fail_silently=False,
            )
            return render(request, 'orders/frontend/mail_order_thanks.html', {
            })
    else:
        form = MailOrderForm(initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'reader_id': reader_id
        })
    return render(request, 'orders/frontend/mail_order.html', {
        'form': form,
        'library': library,
        'record': record
    })


def _get_content(args):
    # необходимо чтобы функция имела таймаут
    uh = urllib2.urlopen(args['url'], timeout=10)
    try:
        result = uh.read()
    except Exception as e:
        return {'id': args['id'], 'exception': e}
    return {'id': args['id'], 'result': result}


def _get_orders(xml):
    try:
        orders_root = etree.XML(xml)
    except etree.XMLSyntaxError:
        return []

    order_trees = orders_root.xpath('/result/eSTaskPackage')
    orders = []
    for order_tree in order_trees:
        order = {}
        record_tree = order_tree.xpath('taskSpecificParameters/targetPart/itemRequest/record')
        record_root = copy.deepcopy(record_tree[0])  # иначе возникнет ошибка трансформации
        if record_tree:
            try:
                bib_record = xslt_bib_draw_transformer(record_root, abstract='false()')
                order['record'] = etree.tostring(bib_record, encoding='utf-8').replace('<b/>', '')
            except etree.XSLTApplyError as e:
                order['record'] = e.message

        status_or_error_report = order_tree.xpath('taskSpecificParameters/targetPart/statusOrErrorReport')
        if status_or_error_report:
            order['status_or_error_report'] = status_or_error_report[0].text
        else:
            order['status_or_error_report'] = u'undefined'

        target_reference = order_tree.xpath('targetReference')
        if target_reference:
            order['target_reference'] = target_reference[0].text
        else:
            order['target_reference'] = u'undefined'

        task_status = order_tree.xpath('taskStatus')
        if task_status:
            status_titles = {
                '0': u'Не выполнен',
                '3': u'Отказ',
                '1': u'Выполнен',
                '2': u'Выдан'
            }
            order['task_status'] = status_titles.get(task_status[0].text, task_status[0].text)
        else:
            order['task_status'] = u'undefined'

        creation_date_time = order_tree.xpath('creationDateTime')
        if creation_date_time:
            try:
                date = datetime.datetime.strptime(creation_date_time[0].text, '%Y%m%d%H%M%S')
            except ValueError:
                date = u'value error'
            order['creation_date_time'] = date
        else:
            order['creation_date_time'] = u'undefined'

        orders.append(order)
    return orders


def _get_books(xml):
    #    url='http://www.unilib.neva.ru/cgi-bin/zurlcirc?z39.50r://%s:%s@ruslan.ru/circ?8003330' % (lib_login, lib_password)
    #    opener = urllib2.build_opener()
    #    result = opener.open(url)
    #    results = result.read()
    xml = xml.replace('<record syntax="">', '<record syntax="RUSmarc">')
    try:
        rcords_root = etree.XML(xml)
    except etree.XMLSyntaxError:
        return []
    books = []
    record_trees = rcords_root.xpath('/records/*')
    for record_tree in record_trees:
        rcord_root = copy.deepcopy(record_tree)  # иначе возникнет ошибка трансформации
        book = {}
        bib_record = xslt_bib_draw_transformer(rcord_root, abstract='false()')
        book['record'] = etree.tostring(bib_record, encoding='utf-8')

        description_tree = rcord_root.xpath('field[@id="999"]/subfield[@id="z"]')
        if description_tree:
            book['description'] = description_tree[0].text
        else:
            book['description'] = u''
        books.append(book)
    return books


order_statuses_titles = {
    'new': u'принят на обработку',
    'recall': u'отказ',
    'conditional': u'в обработке',
    'shipped': u'доставлен',
    'pending': u'в ожидании',  # Доставлен
    'notsupplied': u'выполнение невозможно',
}

apdy_type_titles = {
    'ILLRequest': u'Заказ',
    'ILLAnswer': u'Ответ',
    'Shipped': u'Доставлен',
    'Recall': u'Задолженность',
}

apdu_reason_will_supply = {
    '1': u'Заказ будет выполнен позднее',
    '2': u'Необходимо повторить запрос позднее',
    '3': u'Отказ',
    '4': u'Получена информация о местонахождении документа',
    '5': u'Заказ будет выполнен позднее',
    '6': u'Запрос поставлен в очередь',
    '7': u'Получена информация о стоимости выполнения заказа',
}
apdu_unfilled_results = {
    '1': u'Документ выдан',
    '2': u'Документ в обработке',
    '3': u'Документ утерян и/или списан',
    '4': u'Документ не выдается',
    '5': u'Документа нет в фонде',
    '6': u'Документ заказан, но еще не получен ',
    '7': u'Том / выпуск еще не приобретен',
    '8': u'Документ в переплете',
    '9': u'Отсутствуют необходимые части / страницы документа',
    '10': u'Нет на месте',
    '11': u'Документ временно не выдается',
    '12': u'Документ в плохом состоянии',
    '13': u'Недостаточно средств для выполнения заказа',
    # '14':u'',
    # '15':u'Документ в плохом состоянии',
}

# Вид и статусы заказов, в зависимоти от которых можно удалять заказ
can_delete_statuses = {
    '1': ['shipped', 'received', 'notsupplied', 'checkedin'],  # document
    '2': ['shipped', 'received', 'notsupplied', 'checkedin'],  # copy
    '5': ['shipped', 'notsupplied', 'checkedin']  # reserve
}


def check_for_can_delete(transaction):
    """
    return True or False
    """
    for apdu in transaction.illapdus:
        if isinstance(apdu.delivery_status, ILLRequest):
            if apdu.delivery_status.ill_service_type in can_delete_statuses and \
                    transaction.status in can_delete_statuses[apdu.delivery_status.ill_service_type]:
                return True
    return False


@login_required
def mba_orders(request):
    user_id = request.user.id

    def format_time(datestr='', timestr=''):
        if datestr:
            datestr = time.strptime(datestr, "%Y%m%d")
            datestr = time.strftime("%d.%m.%Y", datestr)
        if timestr:
            timestr = time.strptime(timestr, "%H%M%S")
            timestr = time.strftime("%H:%M:%S", timestr)
        return datestr + ' ' + timestr

    order_manager = OrderManager(settings.ORDERS['db_catalog'], settings.ORDERS['rdx_path'])
    transactions = order_manager.get_orders(user_id)
    orgs = {}
    # for org_id in transactions_by_org:
    orders = []
    for transaction in transactions:
        # print ET.tostring(transaction.illapdus[0].delivery_status.supplemental_item_description, encoding="UTF-8")
        try:
            doc = etree.XML(etree.tostring(transaction.illapdus[0].delivery_status.supplemental_item_description,
                                           encoding="UTF-8"))
            result_tree = xslt_bib_draw_transformer(doc)
            res = str(result_tree)
        except Exception, e:
            raise e
        res = res.replace('– –', '—')
        res = res.replace('\n', '</br>')
        order = {}

        if transaction.status in order_statuses_titles:
            order['status'] = order_statuses_titles[transaction.status]
        else:
            order['status'] = transaction.status
        order['type'] = ''
        order['copy_info'] = ''
        order['apdus'] = []

        for apdu in transaction.illapdus:
            apdu_map = {}

            apdu_map['type'] = apdu.delivery_status.type
            if apdu.delivery_status.type in apdy_type_titles:
                apdu_map['type_title'] = apdy_type_titles[apdu.delivery_status.type]
            else:
                apdu_map['type_title'] = apdu.delivery_status.type

            apdu_map['datetime'] = format_time(apdu.delivery_status.service_date_time['dtots']['date'],
                                               apdu.delivery_status.service_date_time['dtots']['time'])

            if isinstance(apdu.delivery_status, ILLRequest):
                order['order_id'] = apdu.delivery_status.transaction_id['tq']
                order['org_info'] = org_by_id(apdu.delivery_status.responder_id['pois']['is'])
                if apdu.delivery_status.third_party_info_type['tpit']['stl']['stlt']['si']:
                    order['org_info'] = org_by_id(
                        apdu.delivery_status.third_party_info_type['tpit']['stl']['stlt']['si'])
                apdu_map['requester_note'] = apdu.delivery_status.requester_note
                order['record'] = res
                order['user_comments'] = apdu.delivery_status.requester_note
                apdu_map['record'] = res
                if apdu.delivery_status.ill_service_type == '1':
                    apdu_map['service_type'] = u'доставка'
                    order['type'] = 'doc'

                elif apdu.delivery_status.ill_service_type == '2':
                    apdu_map['service_type'] = u'копия'
                    order['type'] = 'copy'
                    order['copy_info'] = apdu.delivery_status.item_id['pagination']

                order['type_title'] = apdu_map['service_type']
                order['can_delete'] = check_for_can_delete(transaction)

            else:
                # print apdu.delivery_status.type
                apdu_map['responder_note'] = apdu.delivery_status.responder_note
                if apdu.delivery_status.type == 'ILLAnswer':
                    apdu_map['reason_will_supply'] = apdu.delivery_status.results_explanation['wsr']['rws']
                    apdu_map['reason_will_supply_title'] = ''
                    if apdu_map['reason_will_supply'] in apdu_reason_will_supply:
                        apdu_map['reason_will_supply_title'] = apdu_reason_will_supply[apdu_map['reason_will_supply']]

                    apdu_map['unfilled_results'] = apdu.delivery_status.results_explanation['ur']['ru']
                    apdu_map['unfilled_results_title'] = ''
                    if apdu_map['unfilled_results'] in apdu_unfilled_results:
                        apdu_map['unfilled_results_title'] = apdu_unfilled_results[apdu_map['unfilled_results']]

            # apdu_map['record'] = res
            order['apdus'].append(apdu_map)

        orders.append(order)
        # if org_id in settings.LIBS:
    #    orgs[org_id] = settings.LIBS[org_id]
    # else:
    #    orgs[org_id] = org_id
    # orders_by_org[org_id] = orders

    return render(request, 'orders/frontend/mba_orders_list.html', {
        'orders': orders,
        'orgs': orgs
    })


def mba_order_copy(request):
    if not request.user.is_authenticated():
        return HttpResponse(u'Вы должны быть войти на портал', status=401)

    if request.method == "POST":
        form = CopyOrderForm(request.POST, prefix='copy')
        if form.is_valid():
            try:
                _make_mba_order(
                    gen_id=form.cleaned_data['gen_id'],
                    user_id=request.user.id,
                    order_type='copy',
                    order_manager_id=form.cleaned_data['manager_id'],
                    copy_info=form.cleaned_data['copy_info'],
                    comments=form.cleaned_data['comments'],
                )
            except MBAOrderException as e:
                return HttpResponse(u'{"status":"error", "error":"%s"}' % e.message)

            return HttpResponse(u'{"status":"ok"}')
        else:
            response = {
                'status': 'error',
                'errors': form.errors
            }
            return HttpResponse(json.dumps(response, ensure_ascii=False))
    else:
        return HttpResponse(u'{"status":"error", "error":"Only POST requests"}')


def mba_order_delivery(request):
    if not request.user.is_authenticated():
        return HttpResponse(u'Вы должны быть войти на портал', status=401)

    if request.method == "POST":
        form = DeliveryOrderForm(request.POST, prefix='delivery')
        if form.is_valid():
            try:
                _make_mba_order(
                    gen_id=form.cleaned_data['gen_id'],
                    user_id=request.user.id,
                    order_type='delivery',
                    order_manager_id=form.cleaned_data['manager_id'],
                    comments=form.cleaned_data['comments'],
                )
            except MBAOrderException as e:
                return HttpResponse(u'{"status":"error", "error":"%s"}' % e.message)
            return HttpResponse(u'{"status":"ok"}')
        else:
            response = {
                'status': 'error',
                'errors': form.errors
            }
            return HttpResponse(json.dumps(response, ensure_ascii=False))
    else:
        return HttpResponse(u'{"status":"error", "error":"Only POST requests"}')


def _check_order_times(user, order_manager_id, order_type):
    order_time = datetime.datetime.now()

    order_copy_limit = 10
    order_document_limit = 10

    user_order_times = UserOrderTimes.objects.filter(
        user=user,
        order_manager_id=order_manager_id,
        order_type=order_type,
        order_time__year=order_time.year,
        order_time__month=order_time.month,
        order_time__day=order_time.day
    ).count()

    if order_type == 'delivery':
        if user_order_times >= order_document_limit:
            return False
    elif order_type == 'copy':
        if user_order_times >= order_copy_limit:
            return False
    else:
        raise ValueError(u'Wrong order type' + str(order_type))

    return True


def _make_mba_order(gen_id, user_id, order_type, order_manager_id, copy_info=u'', comments=u''):
    user_id = str(user_id)
    order_types = ('delivery', 'copy')
    if order_type not in order_types:
        raise ValueError(u'Wrong order type ' + str(order_type))

    doc = None
    try:
        doc = Record.objects.using('records').get(gen_id=gen_id)
    except Record.DoesNotExist:
        pass
    if not doc:
        try:
            doc = Ebook.objects.using('records').get(gen_id=gen_id)
        except Ebook.DoesNotExist:
            raise MBAOrderException(u'Record not founded')

    order_manager = OrderManager(settings.ORDERS['db_catalog'], settings.ORDERS['rdx_path'])

    library = None
    try:
        library = Library.objects.get(id=order_manager_id)
    except Library.DoesNotExist:
        raise MBAOrderException(u'Library not founded')

    def get_first_recivier_code(library):
        ancestors = library.get_ancestors()
        for ancestor in ancestors:
            if ancestor.ill_service and ancestor.ill_service.strip():
                return ancestor.code
        return None

    # если у библиотеки указан ill адрес доставки, то пересылаем заказ ей
    if library.ill_service and library.ill_service.strip():
        manager_id = ''
        reciver_id = library.code

    # иначе ищем родителя, у которого есть адрес доставки
    else:
        manager_id = library.code
        reciver_id = get_first_recivier_code(library)

        if not reciver_id:
            raise MBAOrderException(u'Library cant manage orders')

    sender_id = user_id
    copy_info = copy_info

    order_manager.order_document(
        order_type=order_type,
        sender_id=sender_id,
        reciver_id=reciver_id,
        manager_id=manager_id,
        xml_record=doc.content,
        comments=comments,
        copy_info=copy_info
    )


@login_required
def delete_order(request, order_id=''):
    order_manager = OrderManager(settings.ORDERS['db_catalog'], settings.ORDERS['rdx_path'])
    transactions = order_manager.get_order(order_id=order_id.encode('utf-8'), user_id=unicode(request.user.id))
    if len(transactions):
        if check_for_can_delete(transactions[0]):
            pass
    order_manager.delete_order(order_id=order_id.encode('utf-8'), user_id=unicode(request.user.id))

    return redirect(urlresolvers.reverse('orders:frontend:mba_orders'))


def get_bib_records(bib_ids):
    bib_records = []
    if bib_ids:
        records = get_records(bib_ids)
        for record in records:
            doc_tree = etree.XML(record.content)
            bib_tree = xslt_bib_draw_transformer(doc_tree)
            bib_dump = etree.tostring(bib_tree, encoding='utf-8')
            bib_records.append({
                'record': record,
                'card': beautify(bib_dump.replace('<b/>', '')),
            })

    return bib_records
