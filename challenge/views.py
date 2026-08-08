from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from challenge.models import Question, QuestionOption
from mainquest.models import Unit
from dailyquest.models import UserDailyData
from store.models import Skill
from .skills import (
    process_after_correct_skill,
)

def home(request, unit_id):

    unit = get_object_or_404(Unit, id=unit_id)
    questions = (
        Question.objects
        .filter(unit=unit)
        .prefetch_related("options")
    )

    total_questions = questions.count()
    current_index = request.session.get("current_index", 0)
    current_question = questions[current_index]

    result = None
    selected_option_id = None

    #HP testing
    character = request.user.user_profile.selected_character
    max_hp = request.session.setdefault("MAX_HP", character.max_hp)
    current_hp = request.session.setdefault("current_hp", max_hp,)
    total_correct = request.session.get("total_correct", 0)
    total_wrong = request.session.get("total_wrong", 0)
    #HP testing ended

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "check":#when pressing check
            selected_option_id = request.POST.get("selected_option")
            selected_option = get_object_or_404(
                QuestionOption,
                id=selected_option_id,
            )
            if selected_option.is_correct:
                result = "Correct!"
                total_correct += 1
                request.session["total_correct"] = total_correct
                process_after_correct_skill(request.session, character)
                current_hp = request.session["current_hp"]
            else:
                result = "Wrong!"
                current_hp -= 1
                request.session["current_hp"] = current_hp
                total_wrong += 1
                request.session["total_wrong"] = total_wrong

        elif action == "continue":#when pressing continue
                current_index += 1
                if current_hp <= 0:
                    ending_process(request, False, current_hp, total_correct)
                    return redirect("challenge:finish")
                if current_index == total_questions:
                    ending_process(request, True, current_hp, total_correct)
                    return redirect("challenge:finish")
                else:
                    request.session["current_index"] = current_index
                    current_question = questions[current_index]

        elif action == "skill":#when pressing skill
            print("yes")

        else:#when pressing quit
            request.session.pop("current_index", None)
            request.session.pop("current_hp", None)
            return redirect("mainquest:home")

    skill_available = (character.skill.trigger_time == Skill.TriggerTime.MANUAL)

    context = {
        "unit": unit,
        "question": current_question,
        "result": result,
        "selected_option_id": selected_option_id,
        "current_hp": current_hp,
        "current_index": current_index,
        "character": character,
        "skill_available": skill_available,
    }

    return render(
        request,
        "challenge/challenge.html",
        context,
    )

def ending_process(request, is_win, current_hp, total_correct):
    today = timezone.localdate()
    daily_data, created = UserDailyData.objects.get_or_create(user=request.user,)
    if daily_data.progress_date != today:
        daily_data.progress_date = today
        daily_data.daily_challenge_rewarded = False
        daily_data.daily_quest1_rewarded = False
        daily_data.daily_quest2_rewarded = False
        daily_data.daily_quest3_rewarded = False
        daily_data.full_hp_units_passed_today = 0
        daily_data.questions_correct_today = 0
        daily_data.units_passed_today = 0

    if is_win:
        if current_hp == 3:
            daily_data.full_hp_units_passed_today += 1
        daily_data.units_passed_today += 1
    daily_data.questions_correct_today += total_correct
    daily_data.save()

def finish(request):

    if request.method == "POST":
        return redirect("dailyquest:home")

    total_correct = request.session.get("total_correct", 0)
    total_wrong = request.session.get("total_wrong", 0)
    accuracy = total_correct/(total_correct + total_wrong)

    current_hp = request.session.get("current_hp")
    is_win = current_hp > 0

    if is_win:
        challenge_result = "YOU WIN!!!!!"
    else:
        challenge_result = "YOU LOSE!!!!!"

    request.session.pop("total_correct", None)
    request.session.pop("total_wrong", None)
    request.session.pop("current_index", None)
    request.session.pop("current_hp", None)

    context = {
        "challenge_result": challenge_result,
        "total_correct": total_correct,
        "total_wrong": total_wrong,
        "accuracy": accuracy
    }
    
    return render(
        request, 
        "challenge/finish.html",
        context,)
