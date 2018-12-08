# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=64, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('show', models.BooleanField(default=True, db_index=True, verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u043f\u0443\u043d\u043a\u0442')),
                ('open_in_new', models.BooleanField(default=False, verbose_name='\u041e\u0442\u043a\u0440\u044b\u0432\u0430\u0442\u044c \u0432 \u043d\u043e\u0432\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0430')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442', blank=True, to='menu.MenuItem', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuItemTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lang', models.CharField(db_index=True, max_length=2, verbose_name='\u042f\u0437\u044b\u043a', choices=[(b'ru', b'Russian'), (b'en', b'English'), (b'tt', b'Tatar')])),
                ('title', models.CharField(max_length=512, verbose_name='\u0417\u0430\u0433\u043b\u0430\u0432\u0438\u0435')),
                ('url', models.CharField(default=b'#', max_length=1024, verbose_name='URL \u0434\u043b\u044f \u044d\u0442\u043e\u0433\u043e \u044f\u0437\u044b\u043a\u0430')),
                ('item', models.ForeignKey(to='menu.MenuItem')),
            ],
        ),
        migrations.CreateModel(
            name='MenuTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lang', models.CharField(db_index=True, max_length=2, verbose_name='\u042f\u0437\u044b\u043a', choices=[(b'ru', b'Russian'), (b'en', b'English'), (b'tt', b'Tatar')])),
                ('title', models.CharField(max_length=512, verbose_name='\u0417\u0430\u0433\u043b\u0430\u0432\u0438\u0435')),
                ('menu', models.ForeignKey(to='menu.Menu')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='root_item',
            field=models.ForeignKey(to='menu.MenuItem'),
        ),
        migrations.AlterUniqueTogether(
            name='menutitle',
            unique_together=set([('menu', 'lang')]),
        ),
        migrations.AlterUniqueTogether(
            name='menuitemtitle',
            unique_together=set([('item', 'lang')]),
        ),
    ]
