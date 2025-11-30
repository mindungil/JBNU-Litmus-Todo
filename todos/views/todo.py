from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Todo
from django.utils import timezone

@login_required
def todo_list(request):
    now = timezone.now()

    undone = Todo.objects.filter(user=request.user, is_completed=False, end_at__gt=now)
    done = Todo.objects.filter(user=request.user, is_completed=True)
    overdue = Todo.objects.filter(user=request.user, is_completed=False, end_at__lt=now)

    context = {
        "undone": undone,
        "done": done,
        "overdue": overdue,
        "now": now
    }
    return render(request, "todos/index.html", context)

@login_required
def add_todo(request):
    if request.method == "POST":
        Todo.objects.create(
            user=request.user,
            title=request.POST["title"],
            start_at=request.POST.get("start_at", timezone.now()),
            end_at=request.POST.get("end_at") or None,
        )
    return redirect("todo_list")

@login_required
def toggle_complete(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect("todo_list")


@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect("todo_list")

@login_required
def edit_todo(request):
    if request.method == "POST":
        todo = get_object_or_404(Todo, id=request.POST["id"], user=request.user)
        todo.title = request.POST["title"]
        todo.end_at = request.POST.get("end_at")
        todo.save()
    return redirect("todo_list")
