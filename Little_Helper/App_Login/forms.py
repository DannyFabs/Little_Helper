from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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


class EditProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    # # we modify the init method to keep the password field removed from our rendered fields to be changed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)


class ProfilePicture(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)
