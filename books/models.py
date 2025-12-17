from django.db import models
from authors.models import Author


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название жанра")
    description = models.TextField(blank=True, null=True, verbose_name="Описание жанра")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название книги")
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Автор"
    )
    co_authors = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Соавторы"
    )
    isbn = models.CharField(max_length=50, unique=True)
    publication_year = models.IntegerField(verbose_name="Год публикации")
    genres = models.ManyToManyField(Genre, related_name="books", verbose_name="Жанры")
    summary = models.TextField(blank=True, null=True, verbose_name="Описание книги")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
