# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class AidType(models.Model):
    title = models.CharField(u'Название', max_length=60)

    class Meta:
        verbose_name = u'тип гуманитарной помощь'
        verbose_name_plural = u'типы гуманитарной помощи'

    def __unicode__(self):
        return self.title

TYPES = (
    ('1', 'Детям'),
    ('2', 'Центру'),
)


class HumanitarianAidForKid(models.Model):
    title = models.CharField(u'Название', max_length=60)
    description = models.TextField(u'Описание')

    class Meta:
        verbose_name = u'гуманитарная помощь родителям'
        verbose_name_plural = u'гуманитарная помощь родителям'

    def __unicode__(self):
        return self.title


class HumanitarianAidForSponsors(models.Model):
    title = models.CharField(u'Название', max_length=60)
    type = models.CharField(u"Кому?", max_length=1, default=1, choices=TYPES)
    description = models.TextField(u'Описание')

    class Meta:
        verbose_name = u'для потенциальных спонсоров'
        verbose_name_plural = u'для потенциальных спонсоров'

    def __unicode__(self):
        return self.title


class AidRequest(models.Model):
    aid_item = models.ForeignKey(HumanitarianAidForKid, verbose_name=u'Гуманитарная помощь')
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
