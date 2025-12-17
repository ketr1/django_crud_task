from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'co_authors', 'isbn', 'publication_year', 'genres', 'summary']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_title'] = 'Добавить книгу'
        return ctx


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'co_authors', 'isbn', 'publication_year', 'genres', 'summary']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_title'] = 'Редактировать книгу'
        return ctx


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
