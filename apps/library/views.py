# coding: utf-8
from django.shortcuts import render

from forms import BookOrderForm
from models import Book


def book_list(request):
    message = None
    books = Book.objects.all()
    get_book_form = BookOrderForm(request.POST or None)
    if request.method == 'POST':
        if get_book_form.is_valid():
            get_book_form.save()
            message = 'Запрос отправлен'

    return render(request, 'library.html', {'books': books, 'get_book_form': get_book_form, 'message': message})
