# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ssearch.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gen_id', models.CharField(unique=True, max_length=32)),
                ('record_id', models.CharField(max_length=32, db_index=True)),
                ('scheme', models.CharField(default=b'rusmarc', max_length=16, verbose_name='Scheme', choices=[(b'rusmarc', 'Rusmarc'), (b'usmarc', 'Usmarc'), (b'unimarc', 'Unimarc')])),
                ('content', ssearch.models.ZippedTextField(verbose_name='Xml content')),
                ('add_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('update_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('deleted', models.BooleanField(default=False)),
                ('hash', models.TextField(max_length=16)),
            ],
            options={
                'db_table': 'collections',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetailAccessLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gen_id', models.CharField(max_length=64, verbose_name='\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442, \u043a \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u0431\u044b\u043b\u043e \u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u043e \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0435', db_index=True)),
                ('catalog', models.CharField(max_length=32, verbose_name='\u041a\u0430\u0442\u0430\u043b\u043e\u0433, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u044c\u0441\u044f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442', db_index=True)),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u044f', db_index=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dublet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=128, verbose_name='\u041a\u043b\u044e\u0447 \u0434\u0443\u0431\u043b\u0435\u0442\u043d\u043e\u0441\u0442\u0438', db_index=True)),
                ('statuc', models.IntegerField(db_index=True, choices=[(0, '\u041d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0435'), (1, '\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d')])),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0441\u0442\u0430\u0442\u0443\u0441\u0430', db_index=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gen_id', models.CharField(unique=True, max_length=32)),
                ('record_id', models.CharField(max_length=32, db_index=True)),
                ('scheme', models.CharField(default=b'rusmarc', max_length=16, verbose_name='Scheme', choices=[(b'rusmarc', 'Rusmarc'), (b'usmarc', 'Usmarc'), (b'unimarc', 'Unimarc')])),
                ('content', ssearch.models.ZippedTextField(verbose_name='Xml content', null=True)),
                ('add_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('update_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('deleted', models.BooleanField(default=False)),
                ('hash', models.TextField(max_length=16)),
            ],
            options={
                'db_table': 'ebooks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Holdings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record_id', models.CharField(max_length=255, db_index=True)),
                ('department', models.CharField(max_length=255, db_index=True)),
            ],
            options={
                'db_table': 'ssearch_holdings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gen_id', models.CharField(unique=True, max_length=32)),
                ('record_id', models.CharField(max_length=32, db_index=True)),
                ('scheme', models.CharField(default=b'rusmarc', max_length=16, verbose_name='Scheme', choices=[(b'rusmarc', 'Rusmarc'), (b'usmarc', 'Usmarc'), (b'unimarc', 'Unimarc')])),
                ('content', ssearch.models.ZippedTextField(verbose_name='Xml content', null=True)),
                ('add_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('update_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('deleted', models.BooleanField(default=False)),
                ('hash', models.TextField(max_length=16)),
            ],
            options={
                'db_table': 'records',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SearchRequestLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catalog', models.CharField(max_length=32, null=True, db_index=True)),
                ('library_code', models.CharField(db_index=True, max_length=32, blank=True)),
                ('search_id', models.CharField(max_length=32, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043f\u0440\u043e\u0441\u0430', db_index=True)),
                ('use', models.CharField(max_length=32, verbose_name='\u0422\u043e\u0447\u043a\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u0430', db_index=True)),
                ('not_normalize', models.CharField(max_length=256, verbose_name='\u041d\u0435\u043d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u0440\u043c', db_index=True)),
                ('datetime', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_type', models.CharField(max_length=32)),
                ('organization_code', models.CharField(max_length=32)),
                ('database_group', models.CharField(max_length=32)),
                ('databse_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'source',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WrongRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gen_id', models.CharField(unique=True, max_length=32)),
                ('record_id', models.CharField(max_length=32, db_index=True)),
                ('key', models.CharField(unique=True, max_length=128, verbose_name='\u041a\u043b\u044e\u0447 \u0434\u0443\u0431\u043b\u0435\u0442\u043d\u043e\u0441\u0442\u0438', db_index=True)),
                ('catalog', models.CharField(db_index=True, max_length=16, choices=[(b'records', '\u0421\u0432\u043e\u0434\u043d\u044b\u0439'), (b'ebooks', '\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430')])),
                ('send_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u0442\u0430\u0442\u0443\u0441\u0430', db_index=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndexStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catalog', models.CharField(unique=True, max_length=32)),
                ('last_index_date', models.DateTimeField()),
                ('indexed', models.IntegerField(default=0)),
                ('deleted', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SavedRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('search_request', models.CharField(max_length=1024)),
                ('catalog', models.CharField(max_length=64, null=True, blank=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='saved_request_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'uploads')),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('records_scheme', models.CharField(default=b'rusmarc', max_length=16, choices=[(b'rusmarc', 'Rusmarc'), (b'usmarc', 'Usmarc'), (b'unimarc', 'Unimarc')])),
                ('records_format', models.CharField(default=b'iso2709', max_length=16, choices=[(b'iso2709', 'ISO 2709'), (b'xml', 'XML')])),
                ('records_encodings', models.CharField(default=b'utf-8', max_length=16, choices=[(b'utf-8', 'UTF-8'), (b'cp1251', 'Windows 1251'), (b'koi8-r', 'koi8-r'), (b'latin-1', 'Unimarc'), (b'marc8', 'Marc 8')])),
                ('notes', models.CharField(max_length=255, blank=True)),
                ('processed', models.BooleanField(default=False, db_index=True)),
                ('success', models.BooleanField(default=False, db_index=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
