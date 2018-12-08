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
            name='ExternalUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('external_username', models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u0432\u043e \u0432\u043d\u0435\u0448\u043d\u0435\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u0435', db_index=True)),
                ('auth_source', models.CharField(max_length=32, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430 \u0430\u0443\u0442\u0435\u043d\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438', db_index=True)),
                ('attributes', models.TextField(max_length=10240, verbose_name='\u0410\u0442\u0440\u0438\u0431\u0443\u0442\u044b \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 JSON')),
                ('update', models.DateTimeField(auto_now=True, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name='\u0421\u0432\u044f\u0437\u044c \u0441 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u043c')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='externaluser',
            unique_together=set([('external_username', 'auth_source')]),
        ),
    ]
