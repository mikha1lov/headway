# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('data', models.DateTimeField(verbose_name='\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f')),
                ('price', models.IntegerField(default=0, verbose_name='\u0426\u0435\u043d\u0430')),
            ],
            options={
                'verbose_name': '\u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435',
                'verbose_name_plural': '\u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='EventParticipants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u0424\u0418\u041e')),
                ('contacts', models.CharField(max_length=255, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u0438\u043b\u0438 email')),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event', verbose_name='\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u044f\u0432\u043a\u0430 \u043d\u0430 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043b\u0435\u0433\u043e\u0442\u0435\u043a\u0438',
                'verbose_name_plural': '\u0417\u0430\u044f\u0432\u043a\u0438 \u043d\u0430 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u044b \u043b\u0435\u0433\u043e\u0442\u0435\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f',
                'verbose_name_plural': '\u0422\u0438\u043f \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventType', verbose_name='\u0422\u0438\u043f \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f'),
        ),
    ]
