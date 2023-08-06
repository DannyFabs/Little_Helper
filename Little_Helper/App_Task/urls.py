from django.urls import path
from . import views

app_name = 'App_Task'

urlpatterns = [
    path('home/', views.home, name='home'),
]
