from django.contrib import admin
from news.models import NewsModel

@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'added_by']
