from django.http import HttpResponseRedirect 
from django.shortcuts import render
from .models import Task

def View(request):
    alltasks = Task.objects.all()
    return render(request, 'todolist.html',
    {'all_tasks':alltasks}) 

def AddTask(request):
    _task = request.POST['task']
    newtask = Task(task = _task)
    newtask.save()
    return HttpResponseRedirect('/') 

def Delete(request, id):
    _id = Task.objects.get(id= id)
    _id.delete()
    return HttpResponseRedirect('/') 

