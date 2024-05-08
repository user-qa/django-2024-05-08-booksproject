from django.urls import path

from users.views import RegisterUserView, EmailConfirmationView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterUserView, name='register'),
    path('confirm/', EmailConfirmationView, name='confirm')
]
