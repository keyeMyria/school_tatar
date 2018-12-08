# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442', blank=True, to='ask_librarian.Category', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CategoryTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lang', models.CharField(db_index=True, max_length=2, verbose_name='\u042f\u0437\u044b\u043a', choices=[(b'ru', b'Russian'), (b'en', b'English'), (b'tt', b'Tatar')])),
                ('title', models.CharField(max_length=512, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('category', models.ForeignKey(to='ask_librarian.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fio', models.CharField(max_length=128, verbose_name='\u0424\u0418\u041e', blank=True)),
                ('email', models.EmailField(help_text='\u041d\u0430 \u044d\u0442\u043e\u0442 \u0430\u0434\u0440\u0435\u0441 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u0441\u043b\u0430\u043d \u043e\u0442\u0432\u0435\u0442 \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441', max_length=256, verbose_name='email', blank=True)),
                ('city', models.CharField(max_length=64, verbose_name='\u0413\u043e\u0440\u043e\u0434', blank=True)),
                ('country', models.CharField(max_length=64, verbose_name='\u0421\u0442\u0440\u0430\u043d\u0430', blank=True)),
                ('question', models.TextField(max_length=2048, verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441')),
                ('answer', models.TextField(max_length=10000, verbose_name='\u041e\u0442\u0432\u0435\u0442')),
                ('bib_ids', models.TextField(help_text='\u041a\u0430\u0436\u0434\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u043a\u0430\u0442\u043e\u0440 \u043d\u0430 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0435. \u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u0440\u0438\u0441\u0443\u0442\u0432\u0443\u0435\u0442 \u0434\u0435\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043e \u0437\u0430\u043f\u0438\u0441\u0438', max_length=10000, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u044b \u0431\u0438\u0431. \u0437\u0430\u043f\u0438\u0441\u0435\u0439', blank=True)),
                ('status', models.IntegerField(default=0, db_index=True, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(0, '\u041d\u043e\u0432\u044b\u0439'), (1, '\u0413\u043e\u0442\u043e\u0432'), (2, '\u0412 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0435')])),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f', db_index=True)),
                ('start_process_date', models.DateTimeField(db_index=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0432\u0437\u044f\u0442\u0438\u044f \u0432\u043e\u043f\u0440\u043e\u0441\u0430 \u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443', blank=True)),
                ('end_process_date', models.DateTimeField(db_index=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u0432\u043e\u043f\u0440\u043e\u0441\u0430', blank=True)),
                ('category', models.ForeignKey(verbose_name='\u0422\u0435\u043c\u0430\u0442\u0438\u043a\u0430', to='ask_librarian.Category', help_text='\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0443, \u043a \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u044c\u0441\u044f \u0432\u043e\u043f\u0440\u043e\u0441', null=True)),
            ],
            options={
                'ordering': ['-create_date'],
                'permissions': (('assign_to_manager', 'Can assign question to manager'),),
            },
        ),
        migrations.CreateModel(
            name='QuestionManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('available', models.BooleanField(default=False, db_index=True, verbose_name='\u0414\u043e\u0441\u0442\u0443\u043f\u0435\u043d?')),
                ('user', models.OneToOneField(verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432',
                'verbose_name_plural': '\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440\u044b \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Recomendation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=2048, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd1\x80\xd0\xb5\xd0\xba\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb4\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('public', models.BooleanField(default=False, db_index=True, verbose_name='\u041f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c \u0412\u043c\u0435\u0441\u0442\u0435 \u0441 \u043e\u0442\u0432\u0435\u0442\u043e\u043c')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f', db_index=True)),
                ('question', models.ForeignKey(verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441, \u043a \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u044c\u0441\u044f \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u044f', to='ask_librarian.Question')),
                ('user', models.ForeignKey(verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='manager',
            field=models.ForeignKey(verbose_name='\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440', blank=True, to='ask_librarian.QuestionManager', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='categorytitle',
            unique_together=set([('category', 'lang')]),
        ),
    ]
