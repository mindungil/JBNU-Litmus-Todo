from django.urls import path
from .views import todo_list, add_todo, toggle_complete, delete_todo, edit_todo
from .views.auth import register, login_view, logout_view

urlpatterns = [
    path('', todo_list, name="todo_list"),

    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/register/', register, name="register"),

    path('add/', add_todo, name="add_todo"),
    path('complete/<int:id>/', toggle_complete, name="toggle_complete"),
    path('delete/<int:id>/', delete_todo, name="delete_todo"),
    path('edit/', edit_todo, name="edit_todo"),
]
