from django.http import HttpResponse
from django.shortcuts import render
from tasks.models import User, Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': tasks})

def deleteTask(request, id):
    tasks = Task.objects.all()
    print(id)
    task = Task.objects.get(id=id)
    task.delete()
    return render(request, 'tasks/home.html', {'tasks': tasks})

def addTask(request):
    user = User.objects.get(id=1)
    task = None
    
    if request.GET and request.GET['taskName'] != None:
        task = Task.objects.create(userId=user, taskName=request.GET['taskName'], completionDate=request.GET['completionDate'], isDone=0)
    return render(request, 'tasks/addTask.html', {'task': task})    

def getEditTask(request, id):
    task = Task.objects.get(id=id)
    print(task)
    return render(request, 'tasks/editTask.html', {'task': task})

def editTask(request):
    id = request.GET['id']
    result = Task.objects.filter(pk=id).update(taskName=request.GET['taskName'], completionDate=request.GET['completionDate'])
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': tasks})

def markCompleted(request, id):
    result = Task.objects.filter(pk=id).update(isDone=1)
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': tasks})