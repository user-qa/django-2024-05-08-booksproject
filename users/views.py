import random

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from conf.settings import EMAIL_HOST_USER
from users.forms import RegistrationForm
from users.models import UserConfirmationModel


def send_confirmation_email(email):
    subject = 'Confirmation email'
    code = random.randint(1000, 9999)
    if UserConfirmationModel.objects.filter(code=code).exists():
        send_confirmation_email(email)
    receivers = [email]
    from_email = EMAIL_HOST_USER
    if send_mail(subject=subject, message=str(code), from_email=from_email, recipient_list=receivers):
        UserConfirmationModel.objects.create(
            code=code,
            email=email,
            is_active=True
        )
    else:
        return False


def RegisterView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()
            if send_confirmation_email(form.cleaned_data["email"]):
                return render(request, 'email-confirmation-page.html')
            else:
                return redirect('book:list')
        else:
            return HttpResponse('form.errors')
    else:
        return render(request, 'user-register-page.html')
