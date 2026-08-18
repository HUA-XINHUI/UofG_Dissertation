from django.contrib import admin
from .models import Question, QuestionOption

class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption
    extra = 0

    fields = (
        "order_no",
        "title",
        "description",
        "is_correct",
    )

    ordering = ("order_no",)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "unit",
        "order_no",
        "question_type",
        "available_for_daily",
    )

    list_filter = (
        "question_type",
        "available_for_daily",
        "unit",
    )

    search_fields = (
        "title",
        "description",
        "explanation",
    )

    ordering = (
        "unit",
        "order_no",
    )

    inlines = [
        QuestionOptionInline,
    ]

@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):

    list_display = (
        "question_title",
        "title",
        "order_no",
        "is_correct",
    )

    list_filter = (
        "is_correct",
        "question__unit",
    )

    search_fields = (
        "title",
        "question__title",
    )

    ordering = (
        "question",
        "order_no",
    )

    list_select_related = (
        "question",
    )

    @admin.display(description="Question")
    def question_title(self, obj):
        return obj.question.title