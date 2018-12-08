# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430 \u0440\u0430\u0441\u0441\u044b\u043b\u043e\u043a')),
                ('order', models.IntegerField(default=0, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u0432\u044b\u0432\u043e\u0434\u0430 \u0433\u0440\u0443\u043f\u043f\u044b')),
            ],
            options={
                'ordering': ['-order', 'name'],
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430 \u0440\u0430\u0441\u044b\u043b\u043e\u043a',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b \u0440\u0430\u0441\u0441\u044b\u043b\u043e\u043a',
            },
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=255, verbose_name='\u0422\u0435\u043c\u0430')),
                ('content_format', models.CharField(max_length=16, verbose_name='\u0424\u043e\u0440\u043c\u0430\u0442 \u043f\u0438\u0441\u044c\u043c\u0430', choices=[(b'text', '\u0422\u0435\u043a\u0441\u0442'), (b'html', 'HTML')])),
                ('content', models.TextField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435')),
                ('send_complated', models.BooleanField(default=False, db_index=True, verbose_name='\u0414\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u043e \u0432\u0441\u0435\u043c \u043f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u0430\u043c')),
                ('must_send_at', models.DateTimeField(verbose_name='\u0412\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438', db_index=True)),
                ('age_from', models.PositiveIntegerField(null=True, verbose_name='\u0412\u043e\u0437\u0440\u0430\u0441\u0442 \u043e\u0442 (\u0432\u043a\u043b\u044e\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e)')),
                ('age_to', models.PositiveIntegerField(null=True, verbose_name='\u0412\u043e\u0437\u0440\u0430\u0441\u0442 \u0434\u043e (\u0432\u043a\u043b\u044e\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e)')),
                ('sex', models.BooleanField(default=b'', max_length=1, verbose_name='\u041f\u043e\u043b', choices=[(b'', b'\xd0\xbd\xd0\xb5 \xd0\xb2\xd0\xb0\xd0\xb6\xd0\xbd\xd0\xbe'), (b'm', b'\xd0\xbc\xd1\x83\xd0\xb6'), (b'f', b'\xd0\xb6\xd0\xb5\xd0\xbd')])),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f', db_index=True)),
            ],
            options={
                'verbose_name': '\u041f\u0438\u0441\u044c\u043c\u043e',
                'verbose_name_plural': '\u041f\u0438\u0441\u044c\u043c\u0430',
            },
        ),
        migrations.CreateModel(
            name='SendStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_sended', models.BooleanField(default=False, db_index=True, verbose_name='\u041e\u0442\u043f\u0430\u0440\u0432\u043b\u0435\u043d\u043e')),
                ('has_error', models.BooleanField(default=False, db_index=True, verbose_name='\u041e\u0448\u0438\u0431\u043a\u0430 \u043f\u0440\u0438 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0438')),
                ('error_message', models.CharField(max_length=255, verbose_name='\u0414\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f', db_index=True)),
                ('letter', models.ForeignKey(verbose_name='\u041f\u0438\u0441\u044c\u043c\u043e', to='subscribe.Letter')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u0443\u0441 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438 \u043f\u0438\u0441\u044c\u043c\u0430',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0443\u0441\u044b \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438 \u043f\u0438\u0441\u0435\u043c',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0434\u043f\u0438\u0441\u043a\u0438')),
                ('code', models.SlugField(unique=True, max_length=32, verbose_name='\u041a\u043e\u0434 \u043f\u043e\u0434\u043f\u0438\u0441\u043a\u0438')),
                ('description', models.TextField(max_length=20000, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('is_active', models.BooleanField(default=True, db_index=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u0430')),
                ('order', models.IntegerField(verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430', db_index=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430 \u0440\u0430\u0441\u0441\u044b\u043b\u043e\u043a', blank=True, to='subscribe.Group', null=True)),
            ],
            options={
                'ordering': ['order', 'name'],
                'verbose_name': '\u041f\u043e\u0434\u043f\u0438\u0441\u043a\u0430',
                'verbose_name_plural': '\u041f\u043e\u0434\u043f\u0438\u0441\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(help_text='\u041d\u0430 \u044d\u0442\u043e\u0442 \u0430\u0434\u0440\u0435\u0441 \u0431\u0443\u0434\u0443\u0442 \u043f\u0440\u0438\u0445\u043e\u0434\u0438\u0442\u044c \u043f\u0438\u0441\u044c\u043c\u0430 \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438', unique=True, max_length=255, verbose_name='Email', db_index=True)),
                ('is_active', models.BooleanField(default=True, db_index=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0439')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f', db_index=True)),
                ('subscribe', models.ManyToManyField(to='subscribe.Subscribe', verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4\xd0\xbf\xd0\xb8\xd1\x81\xd0\xba\xd0\xb8')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a',
                'verbose_name_plural': '\u041f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u0438',
            },
        ),
        migrations.AddField(
            model_name='sendstatus',
            name='subscriber',
            field=models.ForeignKey(verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a', to='subscribe.Subscriber'),
        ),
        migrations.AddField(
            model_name='letter',
            name='subscribe',
            field=models.ForeignKey(verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u043a\u0430', to='subscribe.Subscribe'),
        ),
        migrations.AlterUniqueTogether(
            name='sendstatus',
            unique_together=set([('subscriber', 'letter')]),
        ),
    ]
