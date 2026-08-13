from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.utils import timezone
from challenge.models import Question, QuestionOption
from mainquest.models import Unit
from dailyquest.models import UserDailyData
from store.models import Skill, Character
from userprofile.models import UserProfile, UserTaskData
from . import skills, utility

def home(request, unit_id):

    unit = get_object_or_404(Unit, id=unit_id)
    questions = (
        Question.objects
        .filter(unit=unit)
        .prefetch_related("options")
    )
    character = request.user.user_profile.selected_character

    if not request.session.get("challenge_activate", False):
        utility.challenge_session_initialising(request, character, unit_id)
    # challenge_activating = True; current_index = 0; total_correct = 0; total_wrong = 0; is_win=False
    # character_id = character.id; current_hp = character.max_hp; current_mp = character.max_mp
    current_question = questions[request.session["current_index"]]
    options = current_question.options.all()

    result = None
    selected_option_id = None
    hide_options = False

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "check":
            hide_options = True
            utility.question_session_initialising(request)
            selected_option_id = request.POST.get("selected_option")
            selected_option = get_object_or_404(QuestionOption, id=selected_option_id, )

            if selected_option.is_correct:
                result = "Correct!"
                skills.process_after_correct_skill(request, character)
                request.session["total_correct"] += 1
            else:
                result = "Wrong!"
                request.session["current_hp"] -= 1
                request.session["total_wrong"] += 1

        elif action == "continue":
                request.session["current_index"] += 1
                if request.session["current_hp"] <= 0:
                    ending_process(request, False, unit)
                    return redirect("challenge:finish")
                elif request.session["current_index"] == questions.count():
                    ending_process(request, True, unit)
                    return redirect("challenge:finish")
                else:
                    utility.question_session_clearing(request)
                    return redirect("challenge:home", unit_id=unit_id)

        elif action == "skill":
            skills.process_manual_skill(request, character, current_question)
            options = options.exclude(id__in=request.session.get("removed_options_id", []))

        elif action == "quit":
            utility.challenge_session_clearing(request)
            utility.question_session_clearing(request)
            return redirect("mainquest:home")

    skill_available = (character.skill.trigger_time == Skill.TriggerTime.MANUAL)

    context = {
        "unit": unit,
        "question": current_question,
        "options" : options,
        "result": result,
        "current_hp": request.session["current_hp"],
        "current_mp": request.session["current_mp"],
        "character": character,
        "skill_available": skill_available,
        "hide_options": hide_options
    }

    return render(
        request,
        "challenge/challenge.html",
        context,
    )

def ending_process(request, is_win, unit):

    daily_data, created = UserDailyData.objects.get_or_create(user=request.user)
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_task_data, created = UserTaskData.objects.get_or_create(user=request.user)

    today = timezone.localdate()
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
        request.session["is_win"] = True
        if request.session["current_hp"] == Character.objects.get(id=request.session["character_id"]).max_hp:
            daily_data.full_hp_units_passed_today += 1
        user_profile.unit_progress = utility.get_next_unit(unit)
        daily_data.units_passed_today += 1
    daily_data.questions_correct_today += request.session["total_correct"]

    user_profile.experience += 20
    user_profile.gold += 20
    user_task_data.total_questions_answered += (request.session["total_correct"] + request.session["total_wrong"])
    user_task_data.total_correct_answered += request.session["total_correct"]

    daily_data.save()
    user_profile.save()
    user_task_data.save()

def finish(request):

    if request.method == "POST":
        return redirect("dailyquest:home")

    user = request.user
    user_gold = user.user_profile.gold
    user_exp = user.user_profile.experience
    exp_to_next_level = user.user_profile.exp_to_next_level

    total_correct = request.session.get("total_correct", 0)
    total_wrong = request.session.get("total_wrong", 0)
    total_questions = total_correct + total_wrong
    accuracy = total_correct/(total_correct + total_wrong)

    if request.session["is_win"]:
        challenge_result = "YOU WIN!!!!!"
    else:
        challenge_result = "YOU LOSE!!!!!"
    utility.challenge_session_clearing(request)

    context = {
        "challenge_result" : challenge_result,
        "total_questions" : total_questions,
        "total_correct": total_correct,
        "total_wrong": total_wrong,
        "accuracy" : accuracy,
        "user_gold" : user_gold,
        "user_exp" : user_exp,
        "exp_to_next_level" : exp_to_next_level,
    }

    return render(
        request, 
        "challenge/finish.html",
        context,)
