from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    """docstring for LoginForm"""

    username = forms.CharField(
        min_length=4,
        max_length=75,
        required=True,
        label=('username').capitalize()
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label=('password').capitalize(),
        required=True
    )
    first_name = forms.CharField(
        min_length=4,
        max_length=30,
        required=True
    )
    last_name = forms.CharField(
        min_length=4,
        max_length=30,
        required=True,
    )
    email = forms.EmailField(
        required=True
    )