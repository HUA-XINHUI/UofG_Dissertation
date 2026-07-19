from django.shortcuts import get_object_or_404, render
from mainquest.models import Question, QuestionOption

def home(request):

    question = Question.objects.first()
    result = None
    selected_option_id = None

    if request.method == "POST":
        selected_option_id = request.POST.get("selected_option")

        if not selected_option_id:
            result = "Please select an answer."
        else:
            selected_option = get_object_or_404(
                QuestionOption,
                id=selected_option_id,
                question=question,
            )

            if selected_option.is_correct:
                result = "Correct!"
            else:
                result = "Wrong!"

    context = {
        "question": question,
        "result": result,
        "selected_option_id": selected_option_id,
    }

    return render(
        request,
        "challenge/challenge.html",
        context,
    )