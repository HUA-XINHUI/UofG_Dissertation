from django.shortcuts import render
from .models import UserDailyData

def home(request):

    daily_data, created = UserDailyData.objects.get_or_create(user=request.user,)

    context = {
        "daily_data" : daily_data
    }

    return render(request, "dailyquest/dailyquest.html", context)