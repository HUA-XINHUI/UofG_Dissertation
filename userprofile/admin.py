from django.contrib import admin

from .models import (
    UserProfile,
    UserTaskData,
    UserAsset,
)

admin.site.register(UserProfile)
admin.site.register(UserTaskData)
admin.site.register(UserAsset)