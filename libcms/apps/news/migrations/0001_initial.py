# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f', db_index=True)),
                ('type', models.IntegerField(default=(0, '\u041f\u0443\u0431\u043b\u0438\u0447\u043d\u044b\u0435'), db_index=True, verbose_name='\u0412\u0438\u0434 \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439', choices=[(0, '\u041f\u0443\u0431\u043b\u0438\u0447\u043d\u044b\u0435'), (1, '\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435'), (2, '\u041e\u0431\u0449\u0438\u0435')])),
                ('publicated', models.BooleanField(default=True, db_index=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e?')),
            ],
        ),
        migrations.CreateModel(
            name='NewsContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lang', models.CharField(db_index=True, max_length=2, verbose_name='\u042f\u0437\u044b\u043a', choices=[(b'ru', b'Russian'), (b'en', b'English'), (b'tt', b'Tatar')])),
                ('title', models.CharField(max_length=512, verbose_name='\u0417\u0430\u0433\u043b\u0430\u0432\u0438\u0435')),
                ('teaser', models.CharField(help_text='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0438', max_length=512, verbose_name='\u0422\u0438\u0437\u0435\u0440')),
                ('content', models.TextField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0438')),
                ('news', models.ForeignKey(to='news.News')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='newscontent',
            unique_together=set([('news', 'lang')]),
        ),
    ]
