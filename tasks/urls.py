# tasks/urls.py

from django.urls import path
from . import views

app_name = 'tasks'  # This is where you define the namespace for the app

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('complete/<int:id>/', views.complete_task, name='complete'),
    path('delete/<int:id>/', views.delete_task, name='delete'),
]
