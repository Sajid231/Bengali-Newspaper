from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Sign Up form
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={'class': 'input100', 'placeholder': 'Type your Username'}
        ), label=False
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input100', 'placeholder': 'Type your First Name'}
        ), label=False
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input100', 'placeholder': 'Type your Last Name'}
        ), label=False
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input100', 'placeholder': 'Type your Email'}
        ), label=False
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'input100', 'placeholder': 'Type your Password'}
        ), label=False
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'input100', 'placeholder': 'Retype your Password'}
        ), label=False
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user