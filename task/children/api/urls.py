from django.urls import path

from api.views import AddTask, Delete, View

urlpatterns = [
    path('get/', View, name = 'get'),
    path('add/', AddTask, name='add task'),
    path('del/', Delete, name = 'delete task')
]