"""Books views."""

# Django
from django.shortcuts import render

# Models
from .models import Book


def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render(request, 'latest-books.html', {'book_list': book_list})
