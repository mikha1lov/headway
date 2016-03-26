# coding: utf-8
from __future__ import unicode_literals

from django.db import models

class Expert(models.Model):
    name = models.CharField(u"ФИО", max_length=255)
    direction = models.CharField(u"Направление", max_length=255)
    work_time = models.CharField(u"Время работы", max_length=255)

    class Meta:
        verbose_name = u'эксперт'
        verbose_name_plural = u'эксперты'

    def __unicode__(self):
        return self.name
