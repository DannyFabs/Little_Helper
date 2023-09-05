from django.urls import path
from . import views

app_name = 'App_Task'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_task/', views.create_task, name='create_task'),
    path('task/<slug:slug>/', views.view_task, name='current_task'),
    path('delete/<slug:slug>/', views.delete_task, name='delete'),
    path('edit_task/<slug:slug>', views.edit_task, name='edit_task'),

]
