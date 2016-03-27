# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    title = models.CharField(_("Название"), max_length=255)

    class Meta:
        verbose_name = _(u"Категория")
        verbose_name_plural = _(u"Категории")

    def __unicode__(self):
        return self.title


class LegotekaItem(models.Model):
    category = models.ForeignKey(Category, verbose_name=_(u"Категория"))
    title = models.CharField(_("Название"), max_length=255)
    photo = models.ImageField(u"Фотография", upload_to='legoteka/')
    code = models.CharField(_("Код"), max_length=255, blank=True)
    available = models.BooleanField(_("В наличии"), default=True)
    holder = models.CharField(_(u"У кого на руках"), max_length=255, blank=True)
    receiving_date = models.DateField(_(u"Дата получения"), blank=True, null=True)
    return_date = models.DateField(_(u"Дата возврата"), blank=True, null=True)

    class Meta:
        verbose_name = _(u"Предмет леготеки")
        verbose_name_plural = _(u"Предметы леготеки")

    def __unicode__(self):
        return self.title


class LegotekaItemOrder(models.Model):
    item = models.ForeignKey(LegotekaItem, verbose_name=_("Предмет"))
    name = models.CharField(_(u"ФИО"), max_length=255)
    contacts = models.CharField(_("Телефон или email"), max_length=255)
    note = models.CharField(_(u"Примечание"), max_length=255, blank=True)

    class Meta:
        verbose_name = _(u"Заявка на предмет леготеки")
        verbose_name_plural = _(u"Заявки на предметы леготеки")

    def __unicode__(self):
        return self.name