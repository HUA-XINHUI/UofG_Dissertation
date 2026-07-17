from django.conf import settings
from django.db import models


class Section(models.Model):
    """编程课程的大章节，例如 Python Basics。"""

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order_no = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order_no", "id"]

    def __str__(self):
        return self.title


class Unit(models.Model):
    """Section 下的小单元，例如 Variables。"""

    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="units",
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    unit_type = models.CharField(max_length=30, blank=True)
    order_no = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["section", "order_no", "id"]

        constraints = [
            models.UniqueConstraint(
                fields=["section", "order_no"],
                name="unique_unit_order_in_section",
            )
        ]

    def __str__(self):
        return f"{self.section.title} - {self.title}"


class Question(models.Model):
    """Unit 中的题目。"""

    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name="questions",
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    question_type = models.CharField(
        max_length=30,
        default="single_choice",
    )

    explanation = models.TextField(blank=True)
    order_no = models.PositiveIntegerField(default=1)
    available_for_daily = models.BooleanField(default=False)

    # 创建题目的教师或管理员
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_questions",
    )

    category = models.CharField(
        max_length=30,
        blank=True,
    )

    class Meta:
        ordering = ["unit", "order_no", "id"]

        constraints = [
            models.UniqueConstraint(
                fields=["unit", "order_no"],
                name="unique_question_order_in_unit",
            )
        ]

    def __str__(self):
        return self.title


class QuestionOption(models.Model):
    """一道题目的选项。"""

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="options",
    )

    # 例如 A、B、C、D
    title = models.CharField(max_length=100)

    # 选项的实际内容
    description = models.TextField()

    is_correct = models.BooleanField(default=False)

    order_no = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["question", "order_no", "id"]

        constraints = [
            models.UniqueConstraint(
                fields=["question", "order_no"],
                name="unique_option_order_in_question",
            )
        ]

    def __str__(self):
        return f"{self.question.title} - {self.title}"