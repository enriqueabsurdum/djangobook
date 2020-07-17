"""Books admin."""

# Django
from django.contrib import admin

# Models
from .models import Book

admin.site.register(Book)
