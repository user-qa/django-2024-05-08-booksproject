from django import forms
from news.models import NewsModel


class NewsModelForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ['title', 'content', 'news_pic']

