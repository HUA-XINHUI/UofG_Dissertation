from django.shortcuts import render, get_object_or_404, redirect
from .models import Section, Unit

def home(request):
    # unit = request.user.user_profile.unit_progress
    # section = unit
    user = request.user
    section = Section.objects.first()

    if request.method == "POST":
        unit_id = request.POST.get("mainquest-request")

        if unit_id:
            unit = get_object_or_404(Unit, id=unit_id)

            return redirect(
                "challenge:home",
                unit_id=unit.id,
            )

    context = {
        "user" : user,
        "section": section,
    }

    return render(request, "mainquest/mainquest.html", context)