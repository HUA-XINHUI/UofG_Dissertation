from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.db import transaction

from userprofile.models import UserProfile, UserTaskData
from dailyquest.models import UserDailyData
from store.models import Character

@transaction.atomic
def create_user_database(username, password):

    user = User.objects.create_user(
        username=username,
        password=password
    )
    default_character = Character.objects.filter(
        is_default=True
    ).first()
    UserProfile.objects.create(
        user=user,
        experience=0,
        gold=0,
        selected_character=default_character
    )
    UserDailyData.objects.create(
        user=user
    )
    UserTaskData.objects.create(
        user=user
    )
    return user

def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(request, "accounts/home.html", {
                "register_error": "Passwords do not match."
            })
        if User.objects.filter(username=username).exists():
            return render(request, "accounts/home.html", {
                "register_error": "Username already exists."
            })
        user = create_user_database(
            username=username,
            password=password
        )
        login(request, user)

    return redirect("accounts:home")

def logout_view(request):
    logout(request)

    return redirect("accounts:home")

def home(request):
    error_message = None
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("accounts:home")

        else:
            error_message = "Incorrect username or password."

    return render(
        request,
        "accounts/home.html",
        {
            "error_message": error_message,
        }
    )