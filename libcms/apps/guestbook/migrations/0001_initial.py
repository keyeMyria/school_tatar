# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email \u0434\u043b\u044f \u0441\u0432\u044f\u0437\u0438')),
                ('content', models.CharField(max_length=2048, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043e\u0442\u0437\u044b\u0432\u0430')),
                ('comment', models.CharField(max_length=10000, verbose_name='\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438 \u043a \u043e\u0442\u0437\u044b\u0432\u0443')),
                ('add_date', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u043f\u0438\u0441\u0430\u043d\u0438\u044f', db_index=True)),
                ('publicated', models.BooleanField(default=False, db_index=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e?')),
            ],
            options={
                'permissions': (('can_comment', 'Can comment feedback'), ('can_public', 'Can public feedback')),
            },
        ),
    ]
