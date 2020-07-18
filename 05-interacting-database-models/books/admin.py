"""Books admin."""

# Django
from django.contrib import admin

# Models
from .models import Author, Book, Publisher

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
