# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AidRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u0424\u0418\u041e')),
                ('contacts', models.CharField(max_length=255, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u0438\u043b\u0438 email')),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0437\u0430\u044f\u0432\u043a\u0430 \u043d\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 \u0433\u0443\u043c \u043f\u043e\u043c\u043e\u0449\u0438',
                'verbose_name_plural': '\u0437\u0430\u044f\u0432\u043a\u0438 \u043d\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 \u0433\u0443\u043c \u043f\u043e\u043c\u043e\u0449\u0438',
            },
        ),
        migrations.CreateModel(
            name='AidType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='\u041d\u0430\u0447\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0433\u0443\u043c\u0430\u043d\u0438\u0442\u0430\u0440\u043d\u043e\u0439 \u043f\u043e\u043c\u043e\u0449\u0438')),
            ],
            options={
                'verbose_name': '\u0433\u0443\u043c\u0430\u043d\u0438\u0442\u0430\u0440\u043d\u0430\u044f \u043f\u043e\u043c\u043e\u0449\u044c',
                'verbose_name_plural': '\u0433\u0443\u043c\u0430\u043d\u0438\u0442\u0430\u0440\u043d\u0430\u044f \u043f\u043e\u043c\u043e\u0449\u044c',
            },
        ),
        migrations.CreateModel(
            name='GivingAid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u0424\u0418\u041e')),
                ('contacts', models.CharField(max_length=255, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u0438\u043b\u0438 email')),
                ('message', models.TextField(blank=True, max_length=255, null=True, verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0437\u0430\u044f\u0432\u043a\u0430 \u043d\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 \u0433\u0443\u043c \u043f\u043e\u043c\u043e\u0449\u0438',
                'verbose_name_plural': '\u0437\u0430\u044f\u0432\u043a\u0438 \u043d\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 \u0433\u0443\u043c \u043f\u043e\u043c\u043e\u0449\u0438',
            },
        ),
        migrations.CreateModel(
            name='HumanitarianAid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aid.AidType', verbose_name='\u041d\u0430\u0447\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0433\u0443\u043c\u0430\u043d\u0438\u0442\u0430\u0440\u043d\u043e\u0439 \u043f\u043e\u043c\u043e\u0449\u0438')),
            ],
            options={
                'verbose_name': '\u0433\u0443\u043c\u0430\u043d\u0438\u0442\u0430\u0440\u043d\u0430\u044f \u043f\u043e\u043c\u043e\u0449\u044c',
                'verbose_name_plural': '\u0433\u0443\u043c\u0430\u043d\u0438\u0442\u0430\u0440\u043d\u0430\u044f \u043f\u043e\u043c\u043e\u0449\u044c',
            },
        ),
        migrations.AddField(
            model_name='aidrequest',
            name='aid_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aid.HumanitarianAid', verbose_name='\u0413\u0443\u043c\u0430\u043d\u0438\u0442\u0430\u0440\u043d\u0430\u044f \u043f\u043e\u043c\u043e\u0449\u044c'),
        ),
    ]
