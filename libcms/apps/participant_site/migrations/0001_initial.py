# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import participant_site.models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryAvatar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(height_field=b'height', width_field=b'width', upload_to=participant_site.models.get_avatar_file_name, max_length=255, help_text='\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0430 JPG \u0438\u043b\u0438 PNG', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438')),
                ('width', models.IntegerField(default=0, verbose_name='\u0428\u0438\u0440\u0438\u043d\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0430\u0432\u0430\u0442\u0430\u0440\u043a\u0438')),
                ('height', models.IntegerField(default=0, verbose_name='\u0412\u044b\u0441\u043e\u0442\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0430\u0432\u0430\u0442\u0430\u0440\u043a\u0438')),
                ('library', models.OneToOneField(to='participants.Library')),
            ],
        ),
        migrations.CreateModel(
            name='LibrarySiteCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'permissions': [['view_library_card', 'Can view library site info card']],
            },
        ),
    ]
