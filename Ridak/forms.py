from django import forms
from django.contrib.auth.models import User


class Registration(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username', 'placeholder': 'Name'}), label='Name')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'username', 'placeholder': 'Password'}))
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'username', 'placeholder': 'Password'}), label='Password confirm')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class Authentication(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username', 'placeholder': 'Name'}), label='Name')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'username', 'placeholder': 'Password'}))
