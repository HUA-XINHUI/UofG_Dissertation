from django.shortcuts import render

def home(request):
    return render(request, "dailyquest/home.html")