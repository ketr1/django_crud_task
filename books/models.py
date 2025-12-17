from django.db import models
from authors.models import Author


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    publication_year = models.IntegerField()
    genres = models.CharField(max_length=255, help_text="Жанры через запятую")
    co_authors = models.CharField(max_length=255, blank=True, null=True, help_text="Соавторы через запятую")
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
