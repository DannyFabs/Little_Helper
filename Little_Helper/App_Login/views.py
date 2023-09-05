from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import UserProfile
from .forms import CreateNewUser, ProfilePicture, EditProfile


# Create your views here.
# sign_up view
def sign_up(request):
    form = CreateNewUser()

    if request.method == 'POST':
        form = CreateNewUser(request.POST)

        if form.is_valid():
            user = form.save()
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:sign_in'))
    return render(request, 'App_Login/sign_up.html', context={'title': 'Sign Up', 'form': form})


# sign_in view
def sign_in(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Task:home'))

    return render(request, 'App_Login/sign_in.html', context={'form': form, 'title': 'Sign In'})


# view to logout
@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('landing_page'))


@login_required
def profile(request):
    return render(request, 'App_Login/profile.html', context={'title': 'Profile Page'})


# view to edit profile picture
@login_required
def edit_profile_pic(request):
    form = ProfilePicture(instance=request.user.user_profile)

    if request.method == 'POST':
        form = ProfilePicture(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('App_Login:profile'))

    return render(request, 'App_Login/edit_prof_pic.html', context={'title': 'Profile Picture', 'form': form})


# edit internal parts of profile-- first name, last name, username
@login_required
def edit_profile(request):
    form = EditProfile(instance=request.user)

    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))

    return render(request, 'App_Login/edit_profile.html', context={'title': 'Edit Profile', 'form': form})


# password change
@login_required
def change_password(request):
    form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To prevent the user from being logged out
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('App_Login:edit_profile'))
        else:
            messages.error(request, 'Please correct the errors below.')
    return render(request, 'App_Login/change_password.html', context={'title': 'Password change', 'form': form})
