# Generated by Django 5.0.6 on 2024-05-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_confirmationcodesmodel_delete_userconfirmationmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmationcodesmodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]