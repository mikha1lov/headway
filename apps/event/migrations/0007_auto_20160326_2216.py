# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 22:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20160326_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_type',
            new_name='type',
        ),
    ]
