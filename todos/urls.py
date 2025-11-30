from django.urls import path
from django.contrib.auth import views as auth_views
from .views import todo_list, add_todo, toggle_complete, delete_todo, edit_todo
from .views.auth import register

urlpatterns = [
    path('', todo_list, name="todo_list"),

    # auth 추가
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='todos/auth/login.html'
    ), name='login'),

    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('accounts/register/', register, name="register"),

    path('add/', add_todo, name="add_todo"),
    path('complete/<int:id>/', toggle_complete, name="toggle_complete"),
    path('delete/<int:id>/', delete_todo, name="delete_todo"),
    path('edit/', edit_todo, name="edit_todo"),
]
