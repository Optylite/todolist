from django.shortcuts import render, redirect, get_object_or_404
from.models import Todos
from django.http import JsonResponse
from .forms import AddTodo
# Create your views here.
def todo_view(request):
    if request.method == 'POST':
        # Check if the request is a POST request (button clicked)
        todo_id = request.POST.get('todo_id')
        if todo_id:
            todo = get_object_or_404(Todos, pk=todo_id)
            todo.statues = True
            todo.save()
            return redirect('todo')
    
    # If not a POST request, render the todos as usual
    todos = Todos.objects.all().order_by('-created_at')
    context = {'todos': todos}
    return render(request, 'base/home.html', context)

def add_view(request):
    form = AddTodo(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('todo')
    context = {'form': form}
    return render(request, 'base/addtodo.html', context)


def update_view(request, pk):
    todo = get_object_or_404(Todos, pk=pk)
    if request.method == 'POST':
        todo.name = request.POST.get('name')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('todo')
    context = {'todo':todo}
    return render(request, 'base/update.html', context)


def delete_view(request, pk):
    todo = get_object_or_404(Todos, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo')
    context = {'todo':todo}
    return render(request, 'base/delete.html', context)