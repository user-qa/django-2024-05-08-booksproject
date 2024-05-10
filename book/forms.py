from django import forms

from book.models import BookModel


class BookModelForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['author', 'title', 'info', 'pages', 'ebook', 'cover_photo']

    