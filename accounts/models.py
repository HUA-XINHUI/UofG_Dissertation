from django.conf import settings
from django.db import models


class UserSetting(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_setting",
    )

    sound_enabled = models.BooleanField(default=True)
    haptic_enabled = models.BooleanField(default=True)
    rpg_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s settings"