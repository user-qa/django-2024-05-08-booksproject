from django.urls import path

from book.views import BookListView, BookDetailView, BookDownloadView

app_name = 'book'

urlpatterns = [
    path('', BookListView, name='list'),
    path('detail/<int:pk>/', BookDetailView, name='detail'),
    path('download/<int:pk>/', BookDownloadView, name='download')
]
