from django.shortcuts import render
from .models import Section, Unit

def home(request):
    section = Section.objects.first()
    unit = Unit.objects.first()
    context = {
        "section": section,
        "unit": unit,
    }

    return render(request, "mainquest/mainquest.html", context)