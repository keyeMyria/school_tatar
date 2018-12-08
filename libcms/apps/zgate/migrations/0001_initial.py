# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner_id', models.CharField(max_length=32, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0435\u0441\u0441\u0438\u0438 (md5) \u0438\u043b\u0438 \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f', db_index=True)),
                ('document', models.TextField(verbose_name='\u0422\u0435\u043b\u043e \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430 (xml rusmarc)')),
                ('comments', models.CharField(max_length=2048, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043a \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0443', blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0432\u0430\u043b\u0435\u043d\u0438\u044f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430', db_index=True)),
                ('expiry_date', models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043a\u043e\u0433\u0434\u0430 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442 \u0443\u0434\u0430\u043b\u0438\u0442\u0441\u044f', db_index=True)),
                ('full_document', models.TextField(null=True, verbose_name='\u041f\u043e\u043b\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c \u043d\u0430 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442', blank=True)),
                ('short_document', models.TextField(null=True, verbose_name='\u041a\u0440\u0430\u0442\u043a\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c \u043d\u0430 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavedRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zurls', models.CharField(max_length=2048, verbose_name='\u0421\u043f\u0438\u0441\u043e\u043a \u0431\u0430\u0437 \u0434\u0430\u043d\u043d\u044b\u0445 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430')),
                ('query', models.CharField(max_length=1024, verbose_name='\u0417\u0430\u043f\u0440\u043e\u0441 \u0410\u0420\u041c \u0427\u0438\u0442\u0430\u0442\u0435\u043b\u044f')),
                ('human_query', models.CharField(max_length=1024, verbose_name='\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0430 \u0437\u0430\u043f\u0440\u043e\u0441\u0430', blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SearchRequestLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('search_id', models.CharField(max_length=32, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043f\u0440\u043e\u0441\u0430', db_index=True)),
                ('use', models.CharField(max_length=32, verbose_name='\u0422\u043e\u0447\u043a\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u0430', db_index=True)),
                ('normalize', models.CharField(max_length=256, verbose_name='\u041d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u0440\u043c', db_index=True)),
                ('not_normalize', models.CharField(max_length=256, verbose_name='\u041d\u0435\u043d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u0440\u043c', db_index=True)),
                ('datetime', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZCatalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430')),
                ('latin_title', models.SlugField(unique=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430 (\u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438\u043c\u0438 \u0431\u0443\u043a\u0432\u0430\u043c\u0438)')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430')),
                ('help', models.TextField(null=True, verbose_name='\u0421\u043f\u0440\u0430\u0432\u043a\u0430 \u0434\u043b\u044f \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430', blank=True)),
                ('default_lang', models.CharField(default=(b'rus', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), max_length=10, verbose_name='\u042f\u0437\u044b\u043a \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e', choices=[(b'rus', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'eng', 'English')])),
                ('url', models.URLField(help_text='\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: http://consortium.ruslan.ru/cgi-bin/zgate', verbose_name='URL \u0410\u0420\u041c \u0427\u0438\u0442\u0430\u0442\u0435\u043b\u044f')),
                ('xml', models.CharField(help_text='\u041d\u0443\u0436\u043d\u043e \u0443\u0442\u043e\u0447\u043d\u0438\u0442\u044c \u0443 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430', max_length=256, verbose_name='\u0418\u043c\u044f XML \u0444\u0430\u0439\u043b\u0430')),
                ('xsl', models.CharField(help_text='\u041d\u0443\u0436\u043d\u043e \u0443\u0442\u043e\u0447\u043d\u0438\u0442\u044c \u0443 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430', max_length=256, verbose_name='\u0418\u043c\u044f XSL \u0444\u0430\u0439\u043b\u0430')),
                ('can_search', models.BooleanField(default=True, help_text='\u0414\u043e\u0441\u0442\u0443\u043f \u043a \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0443 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430', verbose_name='\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043f\u043e\u0438\u0441\u043a\u0430')),
                ('can_order_auth_only', models.BooleanField(default=True, help_text='\u0417\u0430\u043a\u0430\u0437 \u0432 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u0435\u043d \u0442\u043e\u043b\u044c\u043a\u043e \u0435\u0441\u043b\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d \u043d\u0430 \u043f\u043e\u0440\u0442\u0430\u043b\u0435', verbose_name='\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u043a\u0430\u0437\u0430 \u0432 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u043c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c \u043d\u0430 \u043f\u043e\u0440\u0442\u0430\u043b\u0435')),
                ('can_order_copy', models.BooleanField(default=False, verbose_name='\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u043a\u0430\u0437\u0430 \u043a\u043e\u043f\u0438\u0438 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430')),
                ('can_order_document', models.BooleanField(default=False, verbose_name='\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u043a\u0430\u0437\u0430 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430 \u0432\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435')),
                ('can_reserve', models.BooleanField(default=False, verbose_name='\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c  \u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0430\u043b\u043e\u0433 (\u0410\u0420\u041c \u0447\u0438\u0442\u0430\u0442\u0435\u043b\u044f)',
                'verbose_name_plural': '\u041a\u0430\u0442\u0430\u043b\u043e\u0433\u0438 (\u0410\u0420\u041c \u0447\u0438\u0442\u0430\u0442\u0435\u043b\u044f)',
                'permissions': (('view_zcatalog', '\u0414\u043e\u0441\u0442\u0443\u043f \u043a \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0443'),),
            },
        ),
        migrations.AddField(
            model_name='searchrequestlog',
            name='catalog',
            field=models.ForeignKey(to='zgate.ZCatalog', null=True),
        ),
        migrations.AddField(
            model_name='savedrequest',
            name='zcatalog',
            field=models.ForeignKey(to='zgate.ZCatalog'),
        ),
        migrations.AddField(
            model_name='saveddocument',
            name='zcatalog',
            field=models.ForeignKey(to='zgate.ZCatalog'),
        ),
    ]
