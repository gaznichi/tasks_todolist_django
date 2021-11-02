from django.urls import path
from . import views

urlpatterns = [
    path('', views.View, name = 'Main'),
    path('addtask/', views.AddTask, name = 'Add Task'),
    path('delete/<int:id>', views.Delete, name = 'Delete'),
]