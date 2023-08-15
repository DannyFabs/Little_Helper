from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CreateTask
import uuid

# Create your views here.
from .models import Task


@login_required
def home(request):
    return render(request, 'App_Task/home.html', context={'title': 'Home'})


@login_required
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


@login_required
def view_task(request, slug):
    curr_task = Task.objects.get(task_slug=slug)

    return render(request, 'App_Task/task.html', context={'task': curr_task, 'title': 'Task'})


@login_required
def delete_task(request, slug):
    task = Task.objects.get(task_slug=slug)
    task.delete()

    return render(request, 'App_Task/home.html', context={})


@login_required
def edit_task(request, slug):
    # using reverse relationship between user and task
    current_task = request.user.all_tasks.get(task_slug=slug)
    form = CreateTask(instance=current_task)

    init_name = current_task.task_name

    if request.method == "POST":
        form = CreateTask(request.POST, instance=current_task)
        if form.is_valid:
            task = form.save(commit=False)
            #         update slug, incase the task name is changed
            name = task.task_name
            if init_name != name:
                task.task_slug = name.replace(" ", "-") + "-" + str(uuid.uuid4())
            task.save()
            return HttpResponseRedirect(reverse('App_Task:current_task', kwargs={'slug': task.task_slug}))

    return render(request, 'App_Task/edit_task.html', context={'task': current_task, 'form': form})
