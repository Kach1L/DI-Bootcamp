from django.urls import path
from .views import list_books, book_detail, create_book

urlpatterns = [
    path('list_books/', list_books, name='list_books'),
    path('book_detail/', book_detail, name='one_book'),
    path('create_book/', create_book, name='create_book')
]