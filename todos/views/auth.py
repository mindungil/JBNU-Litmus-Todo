from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
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
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, "todos/auth/register.html", {"form": form})
