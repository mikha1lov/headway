# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Page(models.Model):
    title = models.CharField(u"Название", max_length=200, default='', blank=True)
    url = models.CharField(u"Url", max_length=255)
    content = models.TextField(u"Текст")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'cтраница'
        verbose_name_plural = u'cтраницы'