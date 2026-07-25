from django.db import models
from django.conf import settings

"""
table 6 : Question
ID : Primary Key
Unit : Foreign key, references to unit id in table 4
Title/Description : The textual information about question
QuestionType : indicating multiple choice, matching, etc.
Explanation : The textual information popping up when user answer is incorrect.
Order no : Sequence of questions within a section
Available for daily : True/False for randomly draw into daily quest challenge
Created by : The lecturer ID of the question who upload it
Category :  Category of this question.
"""
class Question(models.Model):

    id = models.BigAutoField(primary_key=True)
    unit = models.ForeignKey(
        "mainquest.Unit",
        to_field="id",
        on_delete=models.CASCADE,
        related_name="questions"
    )
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    class QuestionType(models.TextChoices):
        MULTIPLE_CHOICE = "multiple_choice"
        MATCHING = "matching"
    question_type = models.CharField(
        max_length=30,
        choices=QuestionType.choices,
        default=QuestionType.MULTIPLE_CHOICE,
    )

    explanation = models.TextField(blank=True)
    order_no = models.PositiveIntegerField()
    available_for_daily = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field="id",
        on_delete=models.SET_NULL,
        related_name="created_questions",
        null=True,
        blank=True
    )
    category = models.CharField(max_length=30)

    class Meta:
        ordering = ["order_no"]
    def __str__(self):
        return self.title

"""
table 7 : Question Option
ID : Primary Key
Question : Foreign key, references to question id in table 5
Title/Description : The textual information about each options
Is correct : Ture/False about this option
Order no : Sequence of these options
"""
class QuestionOption(models.Model):

    id = models.BigAutoField(primary_key=True)
    question = models.ForeignKey(
        Question,
        to_field="id",
        on_delete=models.CASCADE,
        related_name="options")
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    is_correct = models.BooleanField(default=False)
    order_no = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    