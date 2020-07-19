"""Books models"""

# Django
from django.db import models


class Publisher(models.Model):
    """Publisher class."""

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Author(models.Model):
    """Author class."""

    salutation = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(verbose_name='e-mail')
    headshot = models.ImageField(upload_to='tmp', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Book(models.Model):
    """Book class."""

    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
