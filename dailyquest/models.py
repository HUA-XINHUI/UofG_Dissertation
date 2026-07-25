from django.db import models

"""
table 8 : DailyChallengeRecord
ID : Super key
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
ID : Super key
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