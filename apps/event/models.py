# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class EventType(models.Model):
    title = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = u"Тип мероприятия"
        verbose_name_plural = u"Тип мероприятия"

    def __unicode__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(u'Название', max_length=60)
    event_type = models.ForeignKey(EventType, verbose_name=u"Тип мероприятия")
    description = models.TextField(u'Описание')
    data = models.DateTimeField(u'Время проведения')
    price = models.IntegerField(u'Цена', default=0)

    class Meta:
        verbose_name = u'мероприятие'
        verbose_name_plural = u'мероприятия'

    def __unicode__(self):
        return self.title


class EventParticipants(models.Model):
    event = models.ForeignKey(Event, verbose_name=u"Мероприятие")
    name = models.CharField(u"ФИО", max_length=255)
    contacts = models.CharField("Телефон или email", max_length=255)
    note = models.CharField(u"Примечание", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u"Заявка на участие в мероприятии"
        verbose_name_plural = u"Заявки на участие в мероприятиях"

    def __unicode__(self):
        return self.name
