from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import UserProfile
from .forms import CreateNewUser


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
    return HttpResponseRedirect(reverse('App_Login:sign_in'))
