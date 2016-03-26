# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class Feedback(models.Model):
    name = models.CharField(u"ФИО", max_length=255)
    contacts = models.CharField(u"Телефон или email", max_length=255)
    message = models.TextField(u'Сообщение')
    created = models.DateTimeField(u'Дата cоздания', auto_now_add=True, editable=False, null=True)

    class Meta:
        verbose_name = u'отзыв'
        verbose_name_plural = u'отзывы'

    def __unicode__(self):
        return self.name
