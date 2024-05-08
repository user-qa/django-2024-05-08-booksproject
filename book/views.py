from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookModel


def BookListView(request):
    books = BookModel.objects.all()
    q = request.GET.get('q')
    if q:
        books = books.filter(title__icontains=q) | books.filter(author__icontains=q)
    context = {
        'books' : books,
    }

    return render(request, 'book-list-page.html', context=context)


def BookDetailView(request, pk):
    book = BookModel.objects.filter(id=pk).first()
    if book:
        context = {
            'book':book,
        }
        return render(request, 'book-detail-page.html', context=context)

    else:
        context = {
            'problem': 'Book with the given ID could not be found.'
        }
        return render(request, 'book-list-page.html', context=context)


def BookDownloadView(request, pk):
    book = BookModel.objects.filter(id=pk).first()
    if book:
        file_path = book.ebook.path
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            return response
    else:
        return HttpResponse('Book Not Found')




