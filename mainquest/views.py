from django.shortcuts import render, get_object_or_404, redirect
from .models import Section, Unit
from django.contrib.auth.decorators import login_required

@login_required(login_url="accounts:home")
def home(request):

    user = request.user
    current_section_id = user.user_profile.unit_progress.section.id
    current_unit_id = user.user_profile.unit_progress.id
    sections = Section.objects

    if request.method == "POST":
        unit_id = request.POST.get("unit-request")

        if unit_id:
            unit = get_object_or_404(Unit, id=unit_id)

            return redirect(
                "challenge:home",
                unit_id=unit.id,
            )

    context = {
        "user" : user,
        "sections": sections,
        "current_section_id" : current_section_id,
        "current_unit_id" : current_unit_id,
    }

    return render(request, "mainquest/mainquest.html", context)