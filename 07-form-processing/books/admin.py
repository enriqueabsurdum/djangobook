"""Books admin."""

# Django
from django.contrib import admin

# Models
from .models import Author, Book, Publisher


class AuthorAdmin(admin.ModelAdmin):
    """Author admin class."""

    list_display = ('first_name', 'last_name', 'email',)
    search_fields = ('first_name', 'last_name',)


class BookAdmin(admin.ModelAdmin):
    """Book admin class."""

    list_display = ('title', 'publisher', 'publication_date',)
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)

    # Data entry form
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
