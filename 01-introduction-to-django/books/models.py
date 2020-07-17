"""Books models."""

# Django
from django.db import models


class Book(models.Model):
    """Book class."""

    name = models.CharField(max_length=50)
    pub_date = models.DateField()

    def __str__(self):
        return self.name
