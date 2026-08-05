from django.shortcuts import get_object_or_404, render, redirect
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
    if current_index >= total_questions:
        current_index = 0
        request.session["current_index"] = 0
    current_question = questions[current_index]

    result = None
    selected_option_id = None

    if request.method == "POST":
        action = request.POST.get("action")
        #when pressing check
        if action == "check":
            selected_option_id = request.POST.get("selected_option")
            if not selected_option_id:
                result = "Please select an answer."
            else:
                selected_option = get_object_or_404(
                    QuestionOption,
                    id=selected_option_id,
                )

                if selected_option.is_correct:
                    result = "Correct!"

                else:
                    result = "Wrong!"
        #when pressing continue
        elif action == "continue":
                current_index += 1
                if current_index == total_questions:
                    current_index == 0
                    request.session["current_index"] = 0
                    return redirect("mainquest:home")

                else:
                    request.session["current_index"] = current_index
                    current_question = questions[current_index]
        #when pressing skill
        elif action == "skill":
            print("yes")
        #when pressing quit
        else:
            request.session.pop(
                "current_index",
                None,
            )
            return redirect("mainquest:home")

    context = {
        "unit": unit,
        "question": current_question,
        "result": result,
        "selected_option_id": selected_option_id,
    }

    return render(
        request,
        "challenge/challenge.html",
        context,
    )