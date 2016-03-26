from django.contrib import admin

from models import Book
from models import BookOrder

admin.site.register(Book)
admin.site.register(BookOrder)
