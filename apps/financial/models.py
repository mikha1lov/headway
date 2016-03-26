# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from redactor.fields import RedactorField


class FinancialEvent(models.Model):
    title = models.CharField(_(u"Название"), max_length=255)
    description = RedactorField(verbose_name=_(u"Описание и условия"),
                                redactor_options={
                                    'lang': 'en',
                                    'plugins': ['table', 'video', 'fullscreen']
                                })
    payment_center = models.CharField(_(u"Оплата со стороны центра"), max_length=255)
    payment_sponsor = models.CharField(_(u"Оплата от спонсора"), max_length=255)
    sponsor = models.CharField(_(u"Спонсор"), max_length=255)

    class Meta:
        verbose_name = _(u"Событие сооплаченное спонсором")
        verbose_name_plural = _(u"События сооплаченные спонсорами")

    def __unicode__(self):
        return self.title


class FinancialEventParticipants(models.Model):
    event = models.ForeignKey(FinancialEvent, verbose_name=u"Мероприятие")
    name = models.CharField(u"ФИО", max_length=255)
    contacts = models.CharField("Телефон или email", max_length=255)
    note = models.CharField(u"Примечание", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u"Заявка на участие в сооплпченом мероприятии"
        verbose_name_plural = u"Заявки на участие в сооплаченых мероприятиях"

    def __unicode__(self):
        return self.name
