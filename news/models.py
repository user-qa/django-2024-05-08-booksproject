from django.contrib.auth.models import User
from django.db import models


class NewsModel(models.Model):
    title = models.TextField()
    date = models.DateField(auto_created=True, default='2024-05-10')

    content = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    news_pic = models.ImageField(upload_to='news/', default='news/img-default-news.png', null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'