from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CreateTask


# Create your views here.

def home(request):
    return render(request, 'App_Task/home.html', context={'title': 'Home'})


def create_task(request):
    form = CreateTask()
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            tsk = form.save(commit=False)
            tsk.author = request.user
            tsk.save()
            return HttpResponseRedirect(reverse('App_Task:home'))

    return render(request, 'App_Task/create_tsk.html', context={'title': 'Create Task', 'form': form})
