from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CreateTask
import uuid

# Create your views here.
from .models import Task


def home(request):
    return render(request, 'App_Task/home.html', context={'title': 'Home'})


def create_task(request):
    form = CreateTask()
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            tsk = form.save(commit=False)
            tsk.author = request.user
            name = tsk.task_name
            tsk.task_slug = name.replace(" ", "-") + "-" + str(uuid.uuid4())
            tsk.save()
            return HttpResponseRedirect(reverse('App_Task:home'))

    return render(request, 'App_Task/create_tsk.html', context={'title': 'Create Task', 'form': form})


def view_task(request, slug):
    curr_task = Task.objects.get(task_slug=slug)

    return render(request, 'App_Task/task.html', context={'task': curr_task, 'title': 'Task'})
