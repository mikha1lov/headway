# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u0424\u0418\u041e')),
                ('direction', models.CharField(max_length=255, verbose_name='\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435')),
                ('work_time', models.CharField(max_length=255, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0431\u043e\u0442\u044b')),
            ],
        ),
    ]
