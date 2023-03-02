from django import http
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .models import Book
from .forms import CommentForm,CommentForm2,BookForm


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list_view.html'
    context_object_name = 'books'
    paginate_by = 2


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail_view.html'
@login_required()
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()
    # if request.user.is_authenticated:
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    # else:
    #     if request.method == 'POST':
    #         comment_form = CommentForm2(request.POST)
    #         if comment_form.is_valid():
    #             new_comment = comment_form.save(commit=False)
    #             new_comment.book = book
    #             new_comment.save()
    #             comment_form = CommentForm2()
    #     else:
    #         comment_form = CommentForm2()

    return render(request, 'books/book_detail_view.html', {
        'book': book,
        'comments': comments,
        'comment_form': comment_form,
    })


class BookCreateView(LoginRequiredMixin, generic.CreateView):

    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover',]
    template_name = 'books/book_create.html'

    def form_valid(self, form):
        b = form.save(commit=False)
        b.user = self.request.user
        return super().form_valid(form)




class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/book_update.html'

    def test_func(self):
        return self.get_object().user == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView, ):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list_view')

    def test_func(self):
        return self.get_object().user == self.request.user
