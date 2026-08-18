from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.utils import timezone

from challenge.models import Question
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
        utility.initialise_challenge_sessions(request, character, unit_id)

    current_question = questions[request.session["current_index"]]
    options = current_question.options.all()
    challenge_data = utility.pack_challenge_data(request)
    question_data = utility.pack_question_data(current_question)

    result = None
    hide_options = False

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "check":
            hide_options = True
            utility.initialise_question_sessions(request)

            is_correct = utility.check_correction_or_not(request)
            if is_correct:
                result = "correct"
                skills.process_after_correct_skill(request)
                request.session["total_correct"] += 1
            else:
                result = "wrong"
                skills.process_after_wrong_skill(request)
                request.session["current_hp"] -= 1
                request.session["total_wrong"] += 1
            challenge_data = utility.pack_challenge_data(request)
            utility.clear_question_sessions(request)
            return JsonResponse({
                "isCorrect" : is_correct,
                "challengeData" : challenge_data,
            })

        elif action == "continue":
            is_end = utility.check_ending_or_not(request, questions)
            if is_end:
                ending_process(request, False, unit)
                return JsonResponse({
                    "isEnd": True,
                    "redirectUrl": "/challenge/finish/",
                })

            question_data = utility.fetch_next_question(request, questions)
            return JsonResponse({
                "is_end" : is_end,
                "questionData" : question_data,
            })

        elif action == "skill":
            skills.process_manual_skill(request, current_question)
            options = options.exclude(id__in=request.session.get("removed_options_id", []))
            return JsonResponse({
                "challengeData" : {
                    "buffs" : request.session["buffs"],
                    "currentMp" : request.session["current_mp"]
                },
                "questionData" : {"options" : [
                {
                    "id" : option.id,
                    "orderNo" : option.order_no,
                    "title" : option.title,
                    "description" : option.description,
                }
                for option in options.all()]},
            })

        elif action == "quit":
            utility.clear_challenge_sessions(request)
            utility.clear_question_sessions(request)
            return JsonResponse({
                "isEnd": True,
                "redirectUrl": "/challenge/finish/",
            })

    skill_available = (character.skill.trigger_type == Skill.TriggerType.ACTIVE)

    context = {
        "unit": unit,
        "question": current_question,
        "options" : options,
        "result": result,
        "current_hp": request.session["current_hp"],
        "current_mp": request.session["current_mp"],
        "character": character,
        "skill_available": skill_available,
        "hide_options": hide_options,
        "challengeData" : challenge_data,
        "questionData" : question_data,
    }

    return render(
        request,
        "challenge/challenge.html",
        context,
    )

def ending_process(request, is_win, unit):

    gold_reward = 20
    exp_reward = 20

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
        gold_reward, exp_reward = skills.process_after_challenge_ending(request, gold_reward, exp_reward)
        user_profile.gold += gold_reward
        user_profile.experience += exp_reward
        user_profile.unit_progress = utility.get_next_unit(unit)

        #daily quest handler
        if request.session["current_hp"] == Character.objects.get(id=request.session["character_id"]).max_hp:
            daily_data.full_hp_units_passed_today += 1
        daily_data.units_passed_today += 1

    daily_data.questions_correct_today += request.session["total_correct"]
    user_task_data.total_questions_answered += (request.session["total_correct"] + request.session["total_wrong"])
    user_task_data.total_correct_answered += request.session["total_correct"]

    daily_data.save()
    user_profile.save()
    user_task_data.save()
    utility.clear_challenge_sessions(request)

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
    # accuracy = total_correct/(total_correct + total_wrong)

    if request.session["is_win"]:
        challenge_result = "YOU WIN!!!!!"
    else:
        challenge_result = "YOU LOSE!!!!!"

    context = {
        "challenge_result" : challenge_result,
        "total_questions" : total_questions,
        "total_correct": total_correct,
        "total_wrong": total_wrong,
        # "accuracy" : accuracy,
        "user_gold" : user_gold,
        "user_exp" : user_exp,
        "exp_to_next_level" : exp_to_next_level,
    }

    return render(
        request, 
        "challenge/finish.html",
        context,)
