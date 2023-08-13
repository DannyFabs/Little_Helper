from django.urls import path
from . import views

app_name = 'App_Task'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_task/', views.create_task, name='create_task'),
    path('task/<slug:slug>/', views.view_task, name='current_task'),
]
