# urls.py
from django.urls import path
from .views import BookListView, add_book, login_view, home, logout_view

urlpatterns = [
    path('book-list/', BookListView.as_view(), name='book-list'),
    path('add-book/', add_book, name='add-book'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('logout/', logout_view, name='logout'),
    # Other URL patterns...
]


