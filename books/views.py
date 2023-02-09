from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list_view.html'
    context_object_name = 'books'
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail_view.html'


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list_view')
