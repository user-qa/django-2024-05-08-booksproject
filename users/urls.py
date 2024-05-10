from django.urls import path

from users.views import RegisterUserView, EmailConfirmationView, LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterUserView, name='register'),
    path('login/', LoginView, name='login'),
    path('confirm/', EmailConfirmationView, name='confirm'),
    path('logout/', LogoutView, name='logout')
]
