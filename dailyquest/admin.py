from django.contrib import admin

from .models import (
    DailyChallengeRecord,
    DailyChallengeQuestion,
    UserDailyData,
)

admin.site.register(DailyChallengeRecord)
admin.site.register(DailyChallengeQuestion)
admin.site.register(UserDailyData)