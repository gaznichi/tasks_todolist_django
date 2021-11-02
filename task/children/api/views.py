from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from taskapp.models import Task

@api_view(['GET'])
def View():
    _tasks = Task.objects.all()
    response = []

    for i in _tasks:
        response.append({
            "id" : i.id,
            "task" : i.task
        })
    return Response(response)

@api_view(['POST'])
def AddTask(request):
    _task = request.data.get('task')
    newtask = Task(task = _task)
    newtask.save()
    return Response('Saved')

@api_view(['POST'])
def Delete(request):
    _id = request.data.get('id')
    id = Task.objects.get(id = _id)
    id.delete()
    return Response('Deleted')