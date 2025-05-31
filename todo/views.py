from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404

#create contents

def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Reload the page

    return render(request, 'home.html', {'tasks': tasks, 'form': form})

#Delete Contents

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')

# Update Contents

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'update.html', {'form': form})

#Toggle Complete

def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # Toggle status
    task.save()
    return redirect('/')