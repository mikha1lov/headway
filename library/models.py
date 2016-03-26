# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from redactor.fields import RedactorField


class Book(models.Model):
    title = models.CharField(_(u"Название"), max_length=255)
    description = RedactorField(verbose_name=_(u"текст"),
                                redactor_options={
                                    'lang': 'en',
                                    'plugins': ['table', 'video', 'fullscreen']
                                })
    book_file = models.FileField(_(u"Файл"), blank=True, upload_to='books/')
    holder = models.CharField(_(u"У кого на руках"), max_length=255, blank=True)
    receiving_date = models.DateField(_(u"Дата получения"), blank=True)
    return_date = models.DateField(_(u"Дата возврата"), blank=True)

    class Meta:
        verbose_name = _(u"Книга")
        verbose_name_plural = _(u"Книги")

    def __unicode__(self):
        return self.title


class BookOrder(models.Model):
    item = models.ForeignKey(Book, verbose_name=_("Книга"))
    name = models.CharField(_(u"ФИО"), max_length=255)
    contacts = models.CharField(_("Телефон или email"), max_length=255)
    note = models.CharField(_(u"Примечание"), max_length=255, blank=True)

    class Meta:
        verbose_name = _(u"Заявка на книгу")
        verbose_name_plural = _(u"Заявки на книги")

    def __unicode__(self):
        return self.name
