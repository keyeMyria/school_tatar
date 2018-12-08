# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lang', models.CharField(db_index=True, max_length=2, verbose_name='\u042f\u0437\u044b\u043a', choices=[(b'ru', b'Russian'), (b'en', b'English'), (b'tt', b'Tatar')])),
                ('title', models.CharField(max_length=512, verbose_name='\u0417\u0430\u0433\u043b\u0430\u0432\u0438\u0435')),
                ('meta', models.CharField(help_text='\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430 \u0434\u043b\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b, \u0436\u0435\u043b\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u043d\u0430 \u044f\u0437\u044b\u043a\u0435 \u043a\u043e\u043d\u0442\u0435\u043d\u0442\u0430', max_length=512, verbose_name='SEO meta', blank=True)),
                ('content', models.TextField(verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(help_text='\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435! \u041f\u043e\u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u044f slug \u043d\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e!', max_length=255, verbose_name='Slug')),
                ('url_path', models.CharField(max_length=2048, db_index=True)),
                ('public', models.BooleanField(default=False, help_text='\u041f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443 \u043c\u043e\u0433\u0443\u0442 \u0442\u043e\u043b\u044c\u043a\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438 \u0441 \u043f\u0440\u0430\u0432\u0430\u043c\u0438 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438 \u0441\u0442\u0440\u0430\u043d\u0438\u0446', db_index=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u0430?')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f', db_index=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430', blank=True, to='pages.Page', null=True)),
            ],
            options={
                'ordering': ['-create_date'],
                'permissions': (('view_page', 'Can view page'), ('public_page', 'Can public page')),
            },
        ),
        migrations.AddField(
            model_name='content',
            name='page',
            field=models.ForeignKey(verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430', to='pages.Page'),
        ),
        migrations.AlterUniqueTogether(
            name='content',
            unique_together=set([('page', 'lang')]),
        ),
    ]
