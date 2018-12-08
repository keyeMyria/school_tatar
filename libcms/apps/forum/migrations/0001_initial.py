# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(help_text='Maximum 10000 simbols', max_length=10000, verbose_name='Text of message')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created', db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Created', db_index=True)),
                ('public', models.BooleanField(default=False, db_index=True, verbose_name='Publicated')),
                ('deleted', models.BooleanField(default=False, db_index=True, verbose_name='Deleted')),
                ('author', models.ForeignKey(verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Maximum 255 simbols', max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(help_text='Small latin letter, "-" and "_"', unique=True, verbose_name='Slug')),
                ('description', models.CharField(help_text='Maximum 1024 simbols', max_length=1024, verbose_name='Description')),
                ('ordering', models.IntegerField(default=0, help_text='Order in forums list', verbose_name='Ordering', db_index=True)),
                ('closed', models.BooleanField(default=False, help_text='If forum is closed, users can not create topics', db_index=True, verbose_name='Closed')),
                ('deleted', models.BooleanField(default=False, db_index=True, verbose_name='Deleted')),
            ],
            options={
                'ordering': ['ordering'],
                'permissions': (('can_views_forums', 'Can view forums'), ('can_close_forums', 'Can close forum'), ('can_view_topics', 'Can view topics in forum'), ('can_create_topics', 'Can create topics in forum'), ('can_change_topics', 'Can change topics in forum'), ('can_delete_topics', 'Can delete topics in forum'), ('can_close_topics', 'Can close all topics in forum'), ('can_close_own_topics', 'Can close own topics in forum'), ('can_hide_topics', 'Can hide topics in forum')),
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(help_text='Maximum 255 simbols', max_length=255, verbose_name='Subject')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created', db_index=True)),
                ('public', models.BooleanField(default=False, db_index=True, verbose_name='Publicated')),
                ('closed', models.BooleanField(default=False, help_text='If topic is closed, users can not create messages', db_index=True, verbose_name='Closed')),
                ('deleted', models.BooleanField(default=False, db_index=True, verbose_name='Deleted')),
                ('forum', models.ForeignKey(to='forum.Forum')),
            ],
            options={
                'ordering': ['-id'],
                'permissions': (('can_view_articles', 'Can view topic articles'), ('can_add_articles', 'Can add articles in topic'), ('can_change_articles', 'Can change articles in topic'), ('can_delete_articles', 'Can delete articles from topic'), ('can_hide_articles', 'Can hide articles in topic'), ('can_publish_own_articles', 'Can publish own articles in topic')),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.ForeignKey(to='forum.Topic'),
        ),
    ]
