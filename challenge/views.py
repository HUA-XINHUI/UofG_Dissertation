from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from challenge.models import Question, QuestionOption
from mainquest.models import Unit

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
    total_correct = request.session.get("total_correct", 0)
    total_wrong = request.session.get("total_wrong", 0)

    #HP testing
    MAX_HP = 3
    current_hp = request.session.get("current_hp",MAX_HP)
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
            else:
                result = "Wrong!"
                current_hp -= 1
                request.session["current_hp"] = current_hp
                total_wrong += 1
                request.session["total_wrong"] = total_wrong

        elif action == "continue":#when pressing continue
                current_index += 1
                if current_hp == 0:
                    return redirect("challenge:finish")
                if current_index == total_questions:
                    current_index == 0
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

    context = {
        "unit": unit,
        "question": current_question,
        "result": result,
        "selected_option_id": selected_option_id,
        "current_hp": current_hp,
        "current_index": current_index,
    }

    return render(
        request,
        "challenge/challenge.html",
        context,
    )

def finish(request):

    if request.method == "POST":
        return redirect("dailyquest:home")

    today = str(timezone.localdate())
    if str(request.session.get("progress_date")) != today:
        request.session["last_dailyquest1_complete_date"] = None
        request.session["last_dailyquest2_complete_date"] = None
        request.session["last_dailyquest3_complete_date"] = None
        request.session["progress_date"] = today
        request.session["total_questions_finished_today"] = 0
        request.session["total_units_finished_today"] = 0
    
    total_correct = request.session.get("total_correct", 0)
    total_wrong = request.session.get("total_wrong", 0)
    accuracy = total_correct/(total_correct + total_wrong)

    current_hp = request.session.get("current_hp")
    is_win = current_hp > 0

    if is_win:
        challenge_result = "YOU WIN!!!!!"
        if current_hp == 3:
            request.session["last_dailyquest1_complete_date"] = today
        request.session["total_units_finished_today"] += 1
    else:
        challenge_result = "YOU LOSE!!!!!"
    request.session["total_questions_finished_today"] += total_correct

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
