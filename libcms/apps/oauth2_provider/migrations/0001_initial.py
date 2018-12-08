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
            name='AccessToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(unique=True, max_length=128)),
                ('created', models.DateTimeField(auto_now=True)),
                ('expired', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f')),
                ('url', models.URLField(max_length=512, verbose_name='URL \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f')),
                ('description', models.TextField(max_length=1024, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('skip_authorization', models.BooleanField(default=False, verbose_name='\u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044e')),
                ('callback', models.URLField(max_length=512, verbose_name='Callback URL')),
                ('client_id', models.CharField(verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043a\u043b\u0438\u0435\u043d\u0442\u0430', unique=True, max_length=128, editable=False, db_index=True)),
                ('client_secret', models.CharField(verbose_name='\u0421\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043a\u043b\u044e\u0447 \u043a\u043b\u0438\u0435\u043d\u0442\u0430', max_length=128, editable=False, db_index=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AuthCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=128)),
                ('created', models.DateTimeField(auto_now=True)),
                ('expired', models.DateTimeField()),
                ('application', models.ForeignKey(to='oauth2_provider.Application')),
                ('auth_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='application',
            field=models.ForeignKey(to='oauth2_provider.Application'),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='auth_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='authcode',
            unique_together=set([('application', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='application',
            unique_together=set([('owner', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='accesstoken',
            unique_together=set([('application', 'auth_user')]),
        ),
    ]
