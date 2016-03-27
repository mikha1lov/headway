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


class Follower(models.Model):
    email = models.CharField(u'Email', max_length=255)
    created_at = models.DateField(u'Дата подписки', auto_now_add=True, editable=False)

    class Meta:
        verbose_name = u"Подписчик"
        verbose_name_plural = u"Подписчики"

    def __unicode__(self):
        return self.email
