from django.db import models
from django.conf import settings

"""
table 12 : User Profile
ID : Super key
User id : Foreign key, references to user id in table 1
Experience : the experience of user having
Gold : the golds of user having
Selected character id : the character user selecting
Unit progress : the number of units finished
Last daily challenge complete date : the last daily challenge complete date
"""
class UserProfile(models.Model):

    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_profile",
    )
    experience = models.PositiveIntegerField(default=0)
    gold = models.PositiveIntegerField(default=0)
    selected_character = models.ForeignKey(
        "store.Character",
        to_field="id",
        on_delete=models.SET_DEFAULT,
        default=1,
        related_name="selected_by_users",
    )
    unit_progress = models.ForeignKey(
        "mainquest.Unit",
        to_field="id",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="current_users",
    )
    last_daily_challenge = models.DateField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"user{self.user}"

"""
table 13 : User Task Data
ID : Super key
User id : Foreign key, references to user id in table 1
Total login days : the number of user login days
Last login date : the last login date of user to calculate the total login days
Total questions answered : the number of questions answered by user
Total correct answered : the number of correct answers answered by user
"""
class UserTaskData(models.Model):

    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="task_data",
    )
    total_login_days = models.PositiveIntegerField(default=0)
    last_login_date = models.DateField(
        null=True,
        blank=True,
    )
    total_questions_answered = models.PositiveIntegerField(default=0)
    total_correct_answered = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user} - Task Data"

"""
table 14 : User Asset
ID : Super key
User id : Foreign key, references to user id in table 1
Character unlocked id : the id of characters user have unlocked
"""
class UserAsset(models.Model):

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="unlocked_characters",
    )
    character = models.ForeignKey(
        "store.Character",
        to_field="id",
        on_delete=models.PROTECT,
        related_name="unlocked_by_users",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "character"],
                name="unique_unlocked_character_per_user",
            ),
        ]

    def __str__(self):
        return f"{self.user} - {self.character}"