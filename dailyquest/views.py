from django.shortcuts import render, redirect
from .models import UserDailyData

def home(request):

    quest1_completed = False
    quest2_completed = False
    quest3_completed = False

    user_daily_data, created = UserDailyData.objects.get_or_create(user=request.user)

    if user_daily_data.questions_correct_today >= 5:
        quest1_completed = True
        quest1_progress = min(user_daily_data.questions_correct_today, 5)
    if user_daily_data.full_hp_units_passed_today >= 1:
        quest2_completed = True
        quest2_progress = min(user_daily_data.full_hp_units_passed_today, 1)
    if user_daily_data.units_passed_today >= 2:
        quest3_completed = True
        quest3_progress = min(user_daily_data.units_passed_today, 2)

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "1":
            user_daily_data.daily_quest1_rewarded = True
        elif action == "2":
            user_daily_data.daily_quest2_rewarded = True
        else:
            user_daily_data.daily_quest3_rewarded = True
        user_daily_data.save()
        return redirect("dailyquest:home")

    context = {
        "user_daily_data" : user_daily_data,
        "quest1_progress" : quest1_progress,
        "quest2_progress" : quest2_progress,
        "quest3_progress" : quest3_progress,
        "quest1_completed" : quest1_completed,
        "quest2_completed" : quest2_completed,
        "quest3_completed" : quest3_completed,
    }

    return render(request, "dailyquest/dailyquest.html", context)