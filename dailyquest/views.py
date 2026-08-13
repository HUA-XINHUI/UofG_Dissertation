from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import UserDailyData

def home(request):

    quest1_target = 5
    quest2_target = 1
    quest3_target = 2

    quest1_reward = 20
    quest2_reward = 20
    quest3_reward = 20

    user_daily_data, created = UserDailyData.objects.get_or_create(user=request.user)

    today = timezone.localdate()
    if user_daily_data.progress_date != today:
        user_daily_data.progress_date = today
        user_daily_data.daily_challenge_rewarded = False
        user_daily_data.daily_quest1_rewarded = False
        user_daily_data.daily_quest2_rewarded = False
        user_daily_data.daily_quest3_rewarded = False
        user_daily_data.full_hp_units_passed_today = 0
        user_daily_data.questions_correct_today = 0
        user_daily_data.units_passed_today = 0
        user_daily_data.save()

    quest1_progress = min(user_daily_data.questions_correct_today, quest1_target)
    quest2_progress = min(user_daily_data.full_hp_units_passed_today, quest2_target)
    quest3_progress = min(user_daily_data.units_passed_today, quest3_target)

    quest1_completed = (
        user_daily_data.questions_correct_today >= quest1_target
    )
    quest2_completed = (
        user_daily_data.full_hp_units_passed_today >= quest2_target
    )
    quest3_completed = (
        user_daily_data.units_passed_today >= quest3_target
    )

    if request.method == "POST":
        action = request.POST.get("action")
        if (action == "1"
            and quest1_completed
            and not user_daily_data.daily_quest1_rewarded) :
            user_daily_data.daily_quest1_rewarded = True
            request.user.user_profile.gold += quest1_reward
            request.user.user_profile.save()
            messages.success(
                request,
                f"daily quest 1 rewarded"
            )
        elif (action == "2"
              and quest2_completed
              and not user_daily_data.daily_quest2_rewarded) :
            user_daily_data.daily_quest2_rewarded = True
            request.user.user_profile.gold += quest2_reward
            request.user.user_profile.save()
            messages.success(
                request,
                f"daily quest 2 rewarded"
            )
        elif (action == "3"
              and quest3_completed
              and not user_daily_data.daily_quest3_rewarded) :
            user_daily_data.daily_quest3_rewarded = True
            request.user.user_profile.gold += quest3_reward
            request.user.user_profile.save()
            messages.success(
                request,
                f"daily quest 3 rewarded"
            )
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