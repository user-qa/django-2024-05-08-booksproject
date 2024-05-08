from django.db import models


class ConfirmationCodesModel(models.Model):
    email = models.EmailField()
    code = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} - {self.email}"

    class Meta:
        verbose_name = 'code'
        verbose_name_plural = 'codes'
