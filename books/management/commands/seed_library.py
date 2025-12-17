from django.core.management.base import BaseCommand
from authors.models import Author
from books.models import Book, Genre
import random


class Command(BaseCommand):
    help = "Заполняет базу тестовыми авторами, жанрами и книгами"

    def handle(self, *args, **options):
        # Очистка старых данных (необязательно)
        Book.objects.all().delete()
        Author.objects.all().delete()
        Genre.objects.all().delete()

        # Создание жанров
        genres = [
            Genre.objects.create(name="Фантастика", description="Фантастические произведения."),
            Genre.objects.create(name="Детектив", description="Расследования, тайны и загадки."),
            Genre.objects.create(name="Роман", description="Любовные и драматические истории."),
            Genre.objects.create(name="Научная литература", description="Книги для обучения и исследований."),
            Genre.objects.create(name="Фэнтези", description="Магия, мифические существа и приключения.")
        ]

        # Создание авторов
        authors = [
            Author.objects.create(first_name="Михаил", last_name="Булгаков", bio="Русский писатель.", birth_date="1891-05-15"),
            Author.objects.create(first_name="Фёдор", last_name="Достоевский", bio="Классик русской литературы.", birth_date="1821-11-11"),
            Author.objects.create(first_name="Артур", last_name="Конан Дойл", bio="Создатель Шерлока Холмса.", birth_date="1859-05-22"),
            Author.objects.create(first_name="Джордж", last_name="Оруэлл", bio="Автор 1984 и Скотного двора.", birth_date="1903-06-25"),
            Author.objects.create(first_name="Рэй", last_name="Брэдбери", bio="Американский писатель-фантаст.", birth_date="1920-08-22"),
        ]

        # Создание книг
        titles = [
            "Мастер и Маргарита",
            "Преступление и наказание",
            "Шерлок Холмс: Собака Баскервилей",
            "1984",
            "451° по Фаренгейту",
            "Игрок",
            "Скотный двор",
            "Вино из одуванчиков",
            "Записки из подполья",
            "Доктор Живаго"
        ]

        for title in titles:
            author = random.choice(authors)
            book = Book.objects.create(
                title=title,
                author=author,
                co_authors="",
                isbn=str(random.randint(1000000000000, 9999999999999)),
                publication_year=random.randint(1850, 2020),
                summary=f"Книга '{title}' написана автором {author.first_name} {author.last_name}.",
            )
            # Привязываем жанры
            book.genres.set(random.sample(genres, k=random.randint(1, 3)))

        self.stdout.write(self.style.SUCCESS("✅ База успешно заполнена тестовыми данными!"))
