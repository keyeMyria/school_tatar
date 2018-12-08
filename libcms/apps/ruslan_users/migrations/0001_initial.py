# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RuslanUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(unique=True, max_length=256, db_index=True)),
                ('first_name', models.CharField(max_length=256, blank=True)),
                ('patronymic', models.CharField(max_length=256, blank=True)),
                ('last_name', models.CharField(max_length=256, blank=True)),
                ('email', models.EmailField(max_length=256, blank=True)),
                ('birth_date', models.DateField(null=True, db_index=True)),
                ('sex', models.CharField(db_index=True, max_length=1, choices=[(b'm', '\u041c'), (b'f', '\u0416')])),
                ('grs_json', models.TextField(max_length=1048576)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('sync_session', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SyncStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sync_started_at', models.DateTimeField(null=True)),
                ('last_sync', models.DateTimeField(null=True)),
                ('refresh_next_time', models.BooleanField(default=False)),
                ('record_processed', models.IntegerField(default=0)),
                ('sync_session', models.IntegerField(default=0)),
            ],
        ),
    ]
