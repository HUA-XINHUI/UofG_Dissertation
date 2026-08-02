from django.contrib import admin

from .models import (
    Character,
    Skill,
)

admin.site.register(Character)
admin.site.register(Skill)