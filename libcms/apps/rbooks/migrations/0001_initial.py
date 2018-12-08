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
            name='Bookmarc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gen_id', models.CharField(max_length=32, db_index=True)),
                ('book_id', models.CharField(max_length=64, db_index=True)),
                ('page_number', models.IntegerField()),
                ('position_x', models.FloatField()),
                ('position_y', models.FloatField()),
                ('comments', models.CharField(max_length=2048, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438 \u043a \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0443', blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0432\u0430\u043b\u0435\u043d\u0438\u044f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430', db_index=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InternalAccessRange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('range', models.CharField(help_text='\u041f\u0440\u0438\u043c\u0435\u0440. 192.168.11.11 - ip \u0430\u0434\u0440\u0435\u0441; 192.168.0.0/16 - \u0441\u0435\u0442\u044c; 192.168.1.1-192.168.1.10 - \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d', max_length=256, verbose_name='IP \u0430\u0434\u0440\u0435\u0441 \u0438\u043b\u0438 \u0441\u0435\u0442\u044c')),
                ('comments', models.TextField(max_length=512, verbose_name='\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438', blank=True)),
                ('type', models.IntegerField(verbose_name='\u0422\u0438\u043f \u0432\u0432\u0435\u0434\u0435\u043d\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f', choices=[(0, '\u0421\u0435\u0442\u044c'), (1, '\u0425\u043e\u0441\u0442'), (2, '\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d')])),
                ('pickle', models.CharField(max_length=1024)),
            ],
        ),
    ]
