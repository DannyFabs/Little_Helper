from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'App_Task/home.html', context={'title': 'Home'})
