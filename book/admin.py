from django.contrib import admin
from book.models import BookModel

@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'pages']
    list_filter = ['title', 'author', 'pages']
    search_fields = ['title', 'author', 'pages']
