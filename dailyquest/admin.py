from django.contrib import admin

from .models import (
    DailyChallengeRecord,
    DailyChallengeQuestion,
)

admin.site.register(DailyChallengeRecord)
admin.site.register(DailyChallengeQuestion)