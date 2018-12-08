# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('in_descendants', models.BooleanField(default=False, verbose_name='\u0411\u0430\u043d\u0435\u0440 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0441\u0430\u0439\u0442\u0430\u0445 \u0434\u043e\u0447\u0435\u0440\u043d\u0438\u0445 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0439')),
                ('lang', models.CharField(help_text='\u042f\u0437\u044b\u043a \u0441\u0438\u0441\u0442\u0435\u043c\u044b, \u043f\u0440\u0438 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d \u0431\u0430\u043d\u0435\u0440', max_length=2, verbose_name='\u042f\u0437\u044b\u043a', db_index=True, choices=[(b'ru', b'Russian'), (b'en', b'English'), (b'tt', b'Tatar')])),
                ('place', models.CharField(default=b'left', max_length=64, verbose_name='\u041c\u0435\u0441\u0442\u043e \u0440\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u044f', choices=[(b'left', '\u0421\u043b\u0435\u0432\u0430'), (b'bottom', '\u041f\u043e\u0434 \u043f\u0440\u043e\u0444\u0438\u043b\u0435\u043c \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438')])),
                ('image', models.ImageField(help_text='\u0417\u0430\u0433\u0440\u0443\u0436\u0430\u0439\u0442\u0435 \u0444\u0430\u0439\u043b\u044b JPG \u0438 PNG \u0441 \u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438\u043c\u0438 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f\u043c\u0438', upload_to='participant_banners/%Y/%m/%d', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 \u0434\u043b\u044f \u0431\u0430\u043d\u0435\u0440\u0430')),
                ('title', models.CharField(max_length=500, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('description', models.TextField(max_length=1000, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('url', models.CharField(max_length=500, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u0434\u043b\u044f \u043a\u043b\u0438\u043a\u0430 \u043f\u043e \u0431\u0430\u043d\u0435\u0440\u0443', blank=True)),
                ('target_blank', models.BooleanField(default=False, verbose_name='\u041e\u0442\u043a\u0440\u044b\u0432\u0430\u0442\u044c \u0441\u0441\u044b\u043b\u043a\u0443 \u0432 \u043d\u043e\u0432\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0435')),
                ('show_period', models.IntegerField(default=5, help_text='\u041f\u0435\u0440\u0438\u043e\u0434 \u043f\u043e\u043a\u0430\u0437\u0430 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445')),
                ('global_banner', models.BooleanField(default=False, help_text='\u0411\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d \u043d\u0430 \u0432\u0441\u0435\u0445 \u0441\u0430\u0439\u0442\u0430\u0445 \u0431\u0435\u0437 \u0438\u0441\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f', db_index=True, verbose_name='\u0413\u043b\u043e\u0431\u0430\u043b\u044c\u043d\u044b\u0439 \u0431\u0430\u043d\u0435\u0440')),
                ('active', models.BooleanField(default=True, db_index=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0439')),
                ('order', models.IntegerField(default=0, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u0432\u044b\u0432\u043e\u0434\u0430', db_index=True)),
                ('start_date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u043e\u043a\u0430\u0437\u0430', db_index=True)),
                ('end_date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043f\u043e\u043a\u0430\u0437\u0430', db_index=True)),
                ('libraries', models.ManyToManyField(to='participants.Library', verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438, \u043d\u0430 \u0441\u0430\u0439\u0442\u0430\u0445 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0431\u0443\u0434\u0435\u0442 \u043f\u043e\u043a\u0430\u0437\u0430\u043d \u0431\u0430\u043d\u0435\u0440', blank=True)),
                ('library_creator', models.ForeignKey(related_name='library_creator', to='participants.Library')),
            ],
            options={
                'ordering': ['-order', '-id'],
                'verbose_name': '\u0411\u0430\u043d\u0435\u0440',
                'verbose_name_plural': '\u0411\u0430\u043d\u0435\u0440\u044b',
                'permissions': (('bind_to_descendants', 'Bind to descendants organisations'),),
            },
        ),
    ]
