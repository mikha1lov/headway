# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from redactor.fields import RedactorField


class News(models.Model):
    title = models.CharField(u"Заголовок", max_length=255)
    photo = models.ImageField(u"Фотография", upload_to='news/')
    text = models.CharField(u"Текст", max_length=255)

    class Meta:
        verbose_name = u"Новость"
        verbose_name_plural = u"Новость"

    def __unicode__(self):
        return self.title
