from django.urls import path

from book.views import BookListView, BookDetailView, BookDownloadView, AddBookView, DeleteBookView

app_name = 'book'

urlpatterns = [
    path('', BookListView, name='list'),
    path('detail/<int:pk>/', BookDetailView, name='detail'),
    path('download/<int:pk>/', BookDownloadView, name='download'),
    path('add/', AddBookView, name='add_book'),
    path('delete/<int:pk>/', DeleteBookView, name='delete')
]
