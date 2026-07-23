from django.core.exceptions import ValidationError
from django.db import models

# class Boss(models.Model):
#     name = models.CharField(
#         max_length=30,
#     )

#     description = models.TextField(
#         blank=True,
#     )

#     asset_key = models.CharField(
#         max_length=100,
#     )

#     def __str__(self):
#         return self.name

# class Section(models.Model):

#     id = models.BigAutoField(primary_key=True)
#     title = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     order_no = models.PositiveIntegerField(unique=True,)

#     class Meta:
#         ordering = ["order_no"]
#     def __str__(self):
#         return self.title

# class Unit(models.Model):

#     id = models.BigAutoField(primary_key=True)
#     section = models.ForeignKey(
#         Section,
#         to_field="id",
#         on_delete=models.CASCADE,
#         related_name="units",
#     )

#     title = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     order_no = models.PositiveIntegerField()

#     class UnitType(models.TextChoices):
#         COMMON = "common"
#         BOSS = "boss"
#     unit_type = models.CharField(
#         max_length=10,
#         choices=UnitType.choices,
#         default=UnitType.COMMON,
#     )

#     boss = models.ForeignKey(
#         Boss,
#         on_delete=models.SET_NULL,
#         related_name="units",
#         null=True,
#         blank=True,
#     )

#     class Meta:
#         ordering = ["section", "order_no", "id"]

#         constraints = [
#             models.UniqueConstraint(
#                 fields=["section", "order_no"],
#                 name="unique_unit_order_in_section",
#             )
#         ]

#     def clean(self):
#         """检查 Unit 类型与 Boss 是否匹配。"""

#         if self.unit_type == self.UnitType.BOSS and self.boss is None:
#             raise ValidationError({
#                 "boss": "Boss unit must select a boss."
#             })

#         if self.unit_type == self.UnitType.COMMON and self.boss is not None:
#             raise ValidationError({
#                 "boss": "Common unit should not have a boss."
#             })

#     def __str__(self):
#         return f"{self.section.title} - {self.title}"
