from django.shortcuts import get_object_or_404, render
from mainquest.models import Question, QuestionOption, Unit

def challenge():
    unit = get_object_or_404(Unit, id=unit_id)

    question = (
        Question.objects
        .filter(unit=unit)
        .order_by("id")
        .first()
    )

    submitted = False
    is_correct = False
    selected_option_id = None

    if request.method == "POST" and question:
        selected_option_id = request.POST.get("answer")

        if selected_option_id:
            selected_option = get_object_or_404(
                QuestionOption,
                id=selected_option_id,
                question=question,
            )

            submitted = True
            is_correct = selected_option.is_correct

    context = {
        "unit": unit,
        "question": question,
        "submitted": submitted,
        "is_correct": is_correct,
        "selected_option_id": selected_option_id,
    }

    return 

def home(request):
    return render(request, "challenge/challenge.html")

