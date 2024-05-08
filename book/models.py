from django.db import models

class BookModel(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    info = models.TextField()
    pages = models.IntegerField()

    ebook = models.FileField(upload_to='ebooks')
    cover_photo = models.ImageField(upload_to='cover_photos')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

