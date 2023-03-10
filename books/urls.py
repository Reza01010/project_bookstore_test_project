from django.urls import path

from .views import (
    BookListView,
    book_detail_view,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)


urlpatterns = [
    path('', BookListView.as_view(), name='book_list_view'),
    path('<int:pk>/', book_detail_view, name='book_detail'),
    path('newbooke/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delet/', BookDeleteView.as_view(), name='book_delete'),
]
#
# comment_form = CommentForm(request.POST)
# if comment_form.is_valid():
#     new_comment = comment_form.save(commit=False)
#     new_comment.book = book
#     new_comment.user = request.user
#     new_comment.save()
#     comment_form = CommentForm()



