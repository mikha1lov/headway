# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class AidType(models.Model):
    title = models.CharField(u'Начначение гуманитарной помощи', max_length=60)

    class Meta:
        verbose_name = u'тип гуманитарной помощь'
        verbose_name_plural = u'типы гуманитарной помощи'

    def __unicode__(self):
        return self.title


class HumanitarianAid(models.Model):
    title = models.CharField(u'Название', max_length=60)
    type = models.ForeignKey(AidType, verbose_name=u"Начначение гуманитарной помощи")
    description = models.TextField(u'Описание')

    class Meta:
        verbose_name = u'гуманитарная помощь'
        verbose_name_plural = u'гуманитарная помощь'

    def __unicode__(self):
        return self.title


class AidRequest(models.Model):
    aid_item = models.ForeignKey(HumanitarianAid, verbose_name=u'Гуманитарная помощь')
    name = models.CharField(u"ФИО", max_length=255)
    contacts = models.CharField("Телефон или email", max_length=255)
    note = models.CharField(u"Примечание", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u'заявка на получение гум помощи'
        verbose_name_plural = u'заявки на получение гум помощи'

    def __unicode__(self):
        return self.name


class GivingAid(models.Model):
    name = models.CharField(u"ФИО", max_length=255)
    contacts = models.CharField("Телефон или email", max_length=255)
    message = models.TextField(u"Сообщение", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u'заявка на оказание гум помощи'
        verbose_name_plural = u'заявки на оказание гум помощи'

    def __unicode__(self):
        return self.name
