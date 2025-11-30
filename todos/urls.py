from django.urls import path
from .views import todo_list, add_todo, toggle_complete, delete_todo
from .views.auth import register

urlpatterns = [
    path('', todo_list, name="todo_list"),
    path('add/', add_todo, name="add_todo"),
    path('complete/<int:id>/', toggle_complete, name="toggle_complete"),
    path('delete/<int:id>/', delete_todo, name="delete_todo"),
    path('register/', register, name="register"),
]
