from django.shortcuts import render
from .models import Section, Unit

def home(request):
    section = Section.objects.first()
    
    context = {
        "section": section,
    }

    return render(request, "mainquest/mainquest.html", context)