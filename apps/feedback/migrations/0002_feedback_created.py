# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 c\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
    ]
