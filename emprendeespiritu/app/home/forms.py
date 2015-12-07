from django import forms


class LoginForm(forms.Form):

    """docstring for LoginForm"""
    username = forms.CharField(
        min_length=4,
        max_length=75,
        label=('username').capitalize()
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label=('password').capitalize()
    )
