from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo


def create_todo(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    
    form = TodoForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        messages.success(request, 'todo created successfully!')
        return redirect('todo:create_todo')

    context = {'form': form}
    return render(request, 'todo/todo_form.html', context)


def todo_list(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    
    todos = Todo.objects.filter(user=request.user)
    context = {'todos': todos}
    return render(request, 'todo/todo_list.html')
