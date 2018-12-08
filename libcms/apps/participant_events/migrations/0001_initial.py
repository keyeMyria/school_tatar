# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import participant_events.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u041d\u0430\u0437\u0430\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u0412\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u0412\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u044b\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=participant_events.models.get_avatar_file_name, max_length=255, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f')),
                ('show_avatar', models.BooleanField(default=False, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f')),
                ('start_date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430', db_index=True)),
                ('end_date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f', db_index=True)),
                ('address', models.CharField(max_length=512, verbose_name='\u041c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f', blank=True)),
                ('active', models.BooleanField(default=True, db_index=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u043e')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f', db_index=True)),
                ('age_category', models.ManyToManyField(to='participant_events.AgeCategory', verbose_name='\u0412\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'ordering': ['-start_date'],
                'verbose_name': '\u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435',
                'verbose_name_plural': '\u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='EventComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=1024, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f (\u043c\u0430\u043a\u0441. 1024 \u0441\u0438\u043c\u0432\u043e\u043b\u0430)')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f')),
                ('event', models.ForeignKey(verbose_name='\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435', to='participant_events.Event')),
                ('user', models.ForeignKey(related_name='comment_user', verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439',
                'verbose_name_plural': '\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='EventContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lang', models.CharField(db_index=True, max_length=2, verbose_name='\u042f\u0437\u044b\u043a', choices=[(b'ru', b'Russian'), (b'en', b'English'), (b'tt', b'Tatar')])),
                ('title', models.CharField(max_length=512, verbose_name='\u0417\u0430\u0433\u043b\u0430\u0432\u0438\u0435')),
                ('teaser', models.CharField(max_length=512, verbose_name='\u0422\u0438\u0437\u0435\u0440')),
                ('content', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f')),
                ('event', models.ForeignKey(to='participant_events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(help_text='\u041d\u0430 \u044d\u0442\u043e\u0442 \u0430\u0434\u0440\u0435\u0441 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u0441\u043b\u0430\u043d\u043e \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435', max_length=255, verbose_name='email')),
                ('items_count', models.PositiveIntegerField(default=1, verbose_name='\u041d\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u0437\u0430')),
                ('time_item', models.CharField(default=b'day', max_length=16, verbose_name='\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b', choices=[(b'min', '\u043c\u0438\u043d.'), (b'hour', '\u0447.'), (b'day', '\u0434\u043d.')])),
                ('notification_time', models.DateTimeField(verbose_name='\u0412\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438 \u0441\u043e\u043e\u0431\u0448\u0435\u043d\u0438\u044f', db_index=True)),
                ('is_notificated', models.BooleanField(default=False, db_index=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(to='participant_events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventSubscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=255, verbose_name='Email \u0430\u0434\u0440\u0435\u0441')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('age_category', models.ManyToManyField(to='participant_events.AgeCategory', verbose_name='\u0412\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u041d\u0430\u0437\u0430\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='FavoriteEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.ForeignKey(verbose_name='\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435', to='participant_events.Event')),
                ('user', models.ForeignKey(related_name='favorite_event_user', verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u043e\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435',
                'verbose_name_plural': '\u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f',
            },
        ),
        migrations.AddField(
            model_name='eventsubscribe',
            name='event_type',
            field=models.ManyToManyField(to='participant_events.EventType', verbose_name='\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='eventsubscribe',
            name='library',
            field=models.ForeignKey(to='participants.Library'),
        ),
        migrations.AddField(
            model_name='eventsubscribe',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ManyToManyField(to='participant_events.EventType', verbose_name='\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='event',
            name='library',
            field=models.ForeignKey(to='participants.Library'),
        ),
        migrations.AlterUniqueTogether(
            name='eventnotification',
            unique_together=set([('event', 'email', 'items_count', 'time_item')]),
        ),
        migrations.AlterUniqueTogether(
            name='eventcontent',
            unique_together=set([('event', 'lang')]),
        ),
    ]
