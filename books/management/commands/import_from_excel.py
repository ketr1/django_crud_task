import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from authors.models import Author
from books.models import Book, Genre


class Command(BaseCommand):
    help = "Импортирует данные из data.xlsx (структура: id, title, author_id, isbn, publication_year, summary, genres)"

    def handle(self, *args, **options):
        try:
            df = pd.read_excel("data.xlsx")
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR("❌ Файл data.xlsx не найден в корне проекта!"))
            return

        required_cols = {"title", "author_id", "isbn", "publication_year", "summary", "genres"}
        if not required_cols.issubset(df.columns):
            self.stderr.write(self.style.ERROR(f"❌ В Excel должны быть колонки: {required_cols}"))
            return

        created_books = 0

        with transaction.atomic():
            for _, row in df.iterrows():
                # Найдём или создадим автора по ID
                author_id = int(row["author_id"])
                author, _ = Author.objects.get_or_create(
                    id=author_id,
                    defaults={
                        "first_name": f"Автор {author_id}",
                        "last_name": "",
                        "bio": "",
                        "birth_date": None,
                    },
                )

                # Создание книги
                book, created = Book.objects.get_or_create(
                    title=row["title"],
                    author=author,
                    isbn=str(row["isbn"]),
                    publication_year=int(row["publication_year"]),
                    summary=row.get("summary", ""),
                )

                if created:
                    created_books += 1

                # Обработка жанров — если указаны ID жанров
                if "genres" in row and pd.notna(row["genres"]):
                    genre_ids = [int(g.strip()) for g in str(row["genres"]).split(",") if g.strip().isdigit()]
                    genres = []
                    for gid in genre_ids:
                        genre, _ = Genre.objects.get_or_create(
                            id=gid,
                            defaults={"name": f"Жанр {gid}", "description": ""}
                        )
                        genres.append(genre)
                    book.genres.set(genres)

        self.stdout.write(self.style.SUCCESS(f"✅ Импорт успешно завершён! Добавлено книг: {created_books}"))
