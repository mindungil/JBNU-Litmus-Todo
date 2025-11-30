from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Todo
from django.utils import timezone
from django.http import JsonResponse
from datetime import datetime

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
        title = request.POST.get("title")
        end_at_str = request.POST.get("end_at") or None
        
        end_at = None
        if end_at_str:
            try:
                end_at = timezone.make_aware(datetime.strptime(end_at_str, "%Y-%m-%dT%H:%M"))
            except ValueError:
                pass

        new_todo = Todo.objects.create(
            user=request.user,
            title=title,
            end_at=end_at
        )

        return JsonResponse({
            "id": new_todo.id,
            "title": new_todo.title,
            "end_at": new_todo.end_at.strftime("%Y-%m-%dT%H:%M") if new_todo.end_at else "",
            "status": "todo"
        })
    return JsonResponse({"error": "Invalid request"}, status=400)

@login_required
def toggle_complete(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.is_completed = not todo.is_completed
    todo.save()
    return JsonResponse({
        "id": todo.id,
        "is_completed": todo.is_completed
    })

@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return JsonResponse({"id": id, "deleted": True})

@login_required
def edit_todo(request):
    if request.method == "POST":
        todo = get_object_or_404(Todo, id=request.POST.get("id"), user=request.user)
        todo.title = request.POST.get("title")
        end_at_str = request.POST.get("end_at") or None
        
        end_at = None
        if end_at_str:
            try:
                end_at = timezone.make_aware(datetime.strptime(end_at_str, "%Y-%m-%dT%H:%M"))
            except ValueError:
                pass
        
        todo.end_at = end_at
        todo.save()

        return JsonResponse({
            "id": todo.id,
            "title": todo.title,
            "end_at": todo.end_at.strftime("%Y-%m-%dT%H:%M") if todo.end_at else "",
        })
    return JsonResponse({"error": "Invalid request"}, status=400)