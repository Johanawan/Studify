from django.shortcuts import render, redirect
from .models import *
from .forms import TaskForm

# Create your views here.
def todo(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/todo")
    
    context = {
        "tasks": tasks,
        "form": form,
    }
    return render(request, "todo/todo.html", context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/todo")

    context = {
        "form": form,
    }
    return render(request, "todo/update_task.html", context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect("/todo")

    context = {
        "item": item,
    }

    return render(request, "todo/delete.html", context)