from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, logout, login
from django.shortcuts import render, redirect

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = CustomUserCreationForm()
    return render(request, "todos/auth/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("todo_list")
    else:
        form = AuthenticationForm()
    return render(request, "todos/auth/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("/")
