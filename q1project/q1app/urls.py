from django.urls import path
from .views import add_book, BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('add-book/', add_book, name='add-book'),
]
