import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from conf.settings import EMAIL_HOST_USER
from users.forms import RegistrationForm, LoginForm
from users.models import ConfirmationCodesModel


def send_confirmation_email(email):
    code = random.randint(1000, 9999)
    if ConfirmationCodesModel.objects.filter(code=code).exists():
        send_confirmation_email(email)
    subject = 'Confirmation Code'
    receivers = [email]
    sender_mail = EMAIL_HOST_USER
    if send_mail(message=str(code), subject=subject, recipient_list=receivers, from_email=sender_mail):
        ConfirmationCodesModel.objects.create(
            code=code,
            email=email,
            is_active=True,
        )

        return True
    else:
        return False


def RegisterUserView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.is_active = False
            user.save()

            if send_confirmation_email(form.cleaned_data["email"]) is True:
                return redirect('users:confirm')

            else:
                return HttpResponse('Email Could Not be Sent. Please try again')

        else:
            return HttpResponse(form.errors)


    elif request.method == 'GET':
        return render(request, 'user-registration-page.html')


def EmailConfirmationView(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        sent_code = ConfirmationCodesModel.objects.get(code=code)
        if sent_code:
            user = User.objects.get(email=sent_code.email)
            user.is_active = True
            user.save()
            return redirect('users:login')
        else:
            return redirect('users:confirm')
    else:
        return render(request, 'email-confirmation-page.html')


def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("book:list")
            else:
                return render(request, 'user-login-page.html')

    else:
        return render(request, 'user-login-page.html')


def LogoutView(request):
    logout(request)
    return redirect('book:list')
