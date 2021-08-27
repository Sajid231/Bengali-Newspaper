from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Login form
class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input100', 'placeholder': 'Type your Username'}
        ), label=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'input100', 'placeholder': 'Type your Password'}
        ), label=False
    )
