from django.urls import path

from news.views import NewsListView, NewsDetailView, AddNewsView, DeleteNewsView

app_name = 'news'
urlpatterns = [
    path('list/', NewsListView.as_view(), name='list'),
    path('detail/<int:pk>/', NewsDetailView, name='detail'),
    path('add/', AddNewsView.as_view(), name='add'),
    path('delete/<int:pk>/', DeleteNewsView, name='delete')
]
