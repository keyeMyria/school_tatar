# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(help_text='\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0430 JPG \u0438\u043b\u0438 PNG', upload_to=b'polls/%Y/%m', max_length=255, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('choice', models.TextField(max_length=255, verbose_name='\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u043e\u0442\u0432\u0435\u0442\u0430')),
                ('record_id', models.CharField(max_length=256, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043f\u0438\u0441\u0438', blank=True)),
                ('votes', models.IntegerField(default=0, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0433\u043e\u043b\u043e\u0441\u043e\u0432')),
                ('sort', models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u0432\u0430\u0440\u0438\u0430\u043d\u0442 \u043e\u0442\u0432\u0435\u0442\u0430',
                'verbose_name_plural': '\u0432\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043e\u0442\u0432\u0435\u0442\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=255, verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441')),
                ('multi_vote', models.BooleanField(default=False, verbose_name='\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u0442\u044c \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0440\u0430\u0437', choices=[(False, '\u041d\u0435\u0442'), (True, '\u0414\u0430')])),
                ('poll_type', models.CharField(default=b'radio', help_text='\u0420\u0430\u0434\u0438\u043e - \u043c\u043e\u0436\u043d\u043e \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u0442\u044c \u0437\u0430 \u043e\u0434\u0438\u043d \u0432\u0430\u0440\u0438\u0430\u043d\u0442. \u0413\u0430\u043b\u043e\u0447\u043a\u0438 - \u0437\u0430 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e.', max_length=16, verbose_name='\u0422\u0438\u043f \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u044f', choices=[(b'radio', '\u0420\u0430\u0434\u0438\u043e'), (b'checkboxes', '\u0413\u0430\u043b\u043e\u0447\u043a\u0438')])),
                ('show_results_on_vote', models.BooleanField(default=False, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u043e\u0441\u043b\u0435 \u043e\u0442\u0432\u0435\u0442\u0430')),
                ('published', models.BooleanField(db_index=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e')),
                ('start_poll_date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u044f', db_index=True)),
                ('end_poll_date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u044f', db_index=True)),
                ('show_results_after_end_poll', models.BooleanField(default=False, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u043e\u0441\u043b\u0435 \u0434\u0430\u0442\u044b \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u0435',
                'verbose_name_plural': '\u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u044f',
                'permissions': (('can_vote', '\u041c\u043e\u0436\u0435\u0442 \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u0442\u044c'), ('can_view_results', '\u041c\u043e\u0436\u0435\u0442 \u043f\u0440\u043e\u0441\u043c\u0430\u0442\u0440\u0438\u0432\u0430\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b')),
            },
        ),
        migrations.CreateModel(
            name='PolledUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('poller_id', models.CharField(max_length=32, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0441\u0435\u0441\u0441\u0438\u0438 (md5) \u0438\u043b\u0438 \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f', db_index=True)),
                ('poll', models.ForeignKey(to='polls.Poll')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(verbose_name='\u0413\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u0435', to='polls.Poll'),
        ),
    ]
