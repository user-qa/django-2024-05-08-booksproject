from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from news.models import NewsModel
from news.forms import NewsModelForm


class NewsListView(View):
    def get(self, request):
        news_list = NewsModel.objects.all().order_by('-date')
        q = request.GET.get('q')
        if q:
            news_list = news_list.filter(title__icontains=q)

        return render(request, 'news-list-page.html', context={'news_list': news_list})


def NewsDetailView(request, pk):
    news = NewsModel.objects.filter(id=pk).first()
    return render(request, 'news-detail-page.html', context={'news': news})


class AddNewsView(View):
    def get(self, request):
        return render(request, 'news-add-page.html')


    def post(self, request):
        form = NewsModelForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.added_by = request.user
            news.save()
            return redirect('news:list')
        else:
            return HttpResponse(f'The news could not be added. {form.errors}')

def DeleteNewsView(request, pk):
    news = NewsModel.objects.get(id=pk)
    news.delete()
    redirect('news:list')

