# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordSync',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sync_date', models.DateTimeField(auto_now=True)),
                ('synchronized', models.BooleanField(default=False, db_index=True)),
                ('need_to_delete', models.BooleanField(default=False, db_index=True)),
                ('last_error', models.CharField(max_length=1024, blank=True)),
                ('password', models.OneToOneField(to='accounts.Password')),
            ],
        ),
        migrations.CreateModel(
            name='SyncStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sync_count', models.IntegerField(default=0)),
                ('sync_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('last_error', models.CharField(max_length=1024, blank=True)),
            ],
            options={
                'ordering': ['-sync_date'],
                'verbose_name': '\u0421\u0442\u0430\u0442\u0443\u0441 \u0441\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u0438',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0443\u0441\u044b \u0441\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u0439',
            },
        ),
    ]
