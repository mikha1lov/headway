# coding: utf-8
from __future__ import unicode_literals

from django.db import models

class Feedback(models.Model):
    name = models.CharField(u"ФИО", max_length=255)
    contacts = models.CharField(u"Телефон или email", max_length=255)
    message = models.TextField(u'Сообщение')

    class Meta:
        verbose_name = u'отзыв'
        verbose_name_plural = u'отзывы'