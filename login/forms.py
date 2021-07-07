from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CreateUserForm(UserCreationForm):
    date = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'email', 'date', 'password1', 'password2']

