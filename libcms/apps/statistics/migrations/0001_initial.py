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
            name='PageView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=1024, blank=True)),
                ('query', models.CharField(max_length=1024, blank=True)),
                ('url_hash', models.CharField(max_length=32, db_index=True)),
                ('session', models.CharField(max_length=32, db_index=True)),
                ('datetime', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'permissions': [['view_org_statistic', 'Can view self org statistic reports'], ['view_all_statistic', 'Can view all statistic reports']],
            },
        ),
    ]
