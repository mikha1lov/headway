from django.contrib import admin

from library.models import Book
from library.models import BookOrder

admin.site.register(Book)
admin.site.register(BookOrder)
