from django.db import models
from django.conf import settings
from django.utils import timezone
"""
table 8 : DailyChallengeRecord
ID : Primary Key
Challenge date : the date of this tuple 
Title/Description : the textual information about this daily challenge
"""
class DailyChallengeRecord(models.Model):

    id = models.BigAutoField(primary_key=True)
    challenge_date = models.DateField(unique=True)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.title

"""
table 9 : DailyChallengeQuestion
ID : Primary Key
Daily challenge id : Foreign key, references to Daily challenge id in table 8.
Question id : Foreign key, references to question id in table 6
Order no : Sequence of this question.
"""
class DailyChallengeQuestion(models.Model):

    id = models.BigAutoField(primary_key=True)
    challenge = models.ForeignKey(
        DailyChallengeRecord,
        to_field="id",
        on_delete=models.CASCADE,
        related_name="daily_questions"
    )
    question = models.ForeignKey(
        "challenge.Question",
        to_field="id",
        on_delete=models.CASCADE,
    )
    
    order_no = models.PositiveIntegerField()

    class Meta:

        ordering = ["challenge", "order_no"]

        constraints = [
            models.UniqueConstraint(
                fields=["challenge", "order_no"],
                name="unique_question_order_in_daily_challenge",
            ),
            models.UniqueConstraint(
                fields=["challenge", "question"],
                name="unique_question_in_daily_challenge",
            ),
        ]

    def __str__(self):
        return (
            f"{self.challenge.challenge_date} - "
            f"Question {self.order_no}"
        )
"""Table 15 : User Daily Data
ID : Primary Key
User id : Foreign key, references to user id in table 1
Daily challenge rewarded: True if the daily challenge rewards have been claimed
Dailyquest1/2/3 rewarded: True if the daily quest rewards have been claimed
Progress date: the date of these recorded updated
Full hp units passed today: total units finished with full hp today
Questions correct today: total questions corrected today
Units passed today : total units passed today
"""
class UserDailyData(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="daily_data",
    )
    daily_challenge_rewarded = models.BooleanField(default=False)
    daily_quest1_rewarded = models.BooleanField(default=False)
    daily_quest2_rewarded = models.BooleanField(default=False)
    daily_quest3_rewarded = models.BooleanField(default=False)
    progress_date = models.DateField(default=timezone.localdate)
    full_hp_units_passed_today = models.PositiveIntegerField(default=0)
    questions_correct_today = models.PositiveIntegerField(default=0)
    units_passed_today = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Daily data - {self.user}"

