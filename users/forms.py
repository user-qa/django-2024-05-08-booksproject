from django import forms
from django.contrib.auth import get_user_model

UserModel = get_user_model()
class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'first_name', 'last_name']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
