# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import recommended_reading.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section', models.CharField(db_index=True, max_length=32, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xb4\xd0\xb5\xd0\xbb', choices=[(b'school', '\u0428\u043a\u043e\u043b\u044c\u043d\u0430\u044f \u043b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u0430'), (b'recommended', '\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u0430\u044f \u043b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u0430')])),
                ('cover', models.ImageField(upload_to=b'recommended_reading/covers/%Y/%m', verbose_name='\u041e\u0431\u043b\u043e\u0436\u043a\u0430', blank=True)),
                ('title', models.CharField(max_length=2048, verbose_name='\u0417\u0430\u0433\u043b\u0430\u0432\u0438\u0435')),
                ('school_class', models.IntegerField(blank=True, help_text='\u0415\u0441\u043b\u0438 \u0438\u0437\u0434\u0430\u043d\u0438\u0435 \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442\u0441\u044f \u0448\u043a\u043e\u043b\u044c\u043d\u0438\u043a\u0430\u043c - \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043a\u043b\u0430\u0441\u0441', null=True, verbose_name='\u041a\u043b\u0430\u0441\u0441', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)])),
                ('author', models.CharField(help_text='\u0415\u0441\u043b\u0438 \u0430\u0432\u0442\u043e\u0440\u043e\u0432 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e, \u0442\u043e \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0447\u0435\u0440\u0435\u0437 \u0437\u0430\u043f\u044f\u0442\u0443\u044e', max_length=2048, verbose_name='\u0410\u0432\u0442\u043e\u0440', blank=True)),
                ('date_of_publication', models.IntegerField(null=True, verbose_name='\u0413\u043e\u0434 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438', blank=True)),
                ('publisher', models.CharField(max_length=2048, verbose_name='\u0418\u0437\u0434\u0430\u0442\u0435\u043b\u044c', blank=True)),
                ('annotation', models.TextField(max_length=10240, verbose_name='\u0410\u043d\u043d\u043e\u0442\u0430\u0446\u0438\u044f', blank=True)),
                ('record_id', models.CharField(max_length=128, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043f\u0438\u0441\u0438 \u0432 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0435', blank=True)),
                ('published', models.BooleanField(default=False, db_index=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f', db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f', db_index=True)),
            ],
            options={
                'verbose_name': '\u0418\u0437\u0434\u0430\u043d\u0438\u0435',
                'verbose_name_plural': '\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u0430\u044f \u043b\u0438\u0442\u0435\u0440\u0430\u0442\u0443\u0440\u0430',
            },
        ),
        migrations.CreateModel(
            name='ItemAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(verbose_name='\u0422\u0438\u043f \u0444\u0430\u0439\u043b\u0430', max_length=16, editable=False, choices=[(b'pdf', b'pdf'), (b'fb2', b'fb2'), (b'epub', b'epub')])),
                ('title', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('file', models.FileField(help_text='\u0422\u043e\u043b\u044c\u043a\u043e \u0444\u0430\u0439\u043b\u044b \u0441 \u0440\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u0438\u0435 .pdf .fb2 .epub', upload_to=recommended_reading.models.attachment_path, verbose_name='\u0424\u0430\u0439\u043b')),
                ('item', models.ForeignKey(to='recommended_reading.Item')),
            ],
            options={
                'verbose_name': '\u0424\u0430\u0439\u043b',
                'verbose_name_plural': '\u0424\u0430\u0439\u043b\u044b',
            },
        ),
        migrations.CreateModel(
            name='ItemAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.SlugField(help_text='\u0422\u043e\u043b\u044c\u043a\u043b \u043f\u0440\u043e\u043f\u0438\u0441\u043d\u044b\u0435 \u0431\u0443\u043a\u0432\u044b \u043b\u0430\u0442\u0438\u043d\u0441\u043a\u043e\u0433\u043e \u0430\u043b\u0444\u0430\u0432\u0438\u0442\u0430', unique=True, max_length=64, verbose_name='\u041a\u043e\u0434')),
                ('title', models.CharField(help_text='\u0427\u0435\u043b\u043e\u0432\u0435\u043a\u043e\u0447\u0438\u0442\u0430\u0435\u043c\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u0430', max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('type', models.CharField(default=b'string', max_length=16, verbose_name='\u0422\u0438\u043f', choices=[(b'string', '\u0421\u0442\u0440\u043e\u043a\u0430'), (b'number', '\u0427\u0438\u0441\u043b\u043e')])),
            ],
            options={
                'verbose_name': '\u0410\u0442\u0440\u0438\u0431\u0443\u0442',
                'verbose_name_plural': '\u0410\u0442\u0440\u0438\u0431\u0443\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='ItemAttributeValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=1024, verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435')),
                ('attribute', models.ForeignKey(verbose_name='\u0410\u0442\u0440\u0438\u0431\u0443\u0442', to='recommended_reading.ItemAttribute')),
                ('item', models.ForeignKey(to='recommended_reading.Item')),
            ],
            options={
                'verbose_name': '\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u0430',
                'verbose_name_plural': '\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u043e\u0432',
            },
        ),
    ]
