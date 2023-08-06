from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class CreateNewUser(UserCreationForm):
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(required=True, label="",
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, label="",
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
