# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20160327_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='receiving_date',
            field=models.DateField(blank=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='book',
            name='return_date',
            field=models.DateField(blank=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0432\u043e\u0437\u0432\u0440\u0430\u0442\u0430'),
        ),
    ]
