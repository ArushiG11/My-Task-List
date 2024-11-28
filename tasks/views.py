from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    if request.method == 'POST':  # 1. Handling Form Submission
        form = TaskForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():  # Validate the form data
            form.save()  # Save the new Task to the database
            return redirect('task_list')  # Redirect to the same page (to avoid resubmission)
    else:  # 2. Handling GET Requests
        form = TaskForm()  # Create a blank form for the user to fill in
    tasks = Task.objects.all()  # 3. Fetch all tasks from the database
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})
    # Render the template with the tasks and the form as context

def complete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = not task.completed
    task.save()
    return redirect('tasks:task_list')

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('tasks:task_list')