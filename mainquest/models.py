from django.conf import settings
from django.db import models
"""
Table 3 : Section
ID : Primary key
Title : The title of section
Description : The description of section
Order no : Sequence of section
"""
class Section(models.Model):

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order_no = models.PositiveIntegerField(unique=True,)

    class Meta:
        ordering = ["order_no"]
    def __str__(self):
        return self.title
"""
Table 4 : Unit
ID : Primary key
Section : Foreign key, references to section id in table 3
Title/Description : textual information of unit
Type : common or Boss unit
Order no : Sequence of units within a section
Boss id : Foreign key, references to boss id in table 5
"""
class Unit(models.Model):

    id = models.BigAutoField(primary_key=True)
    section = models.ForeignKey(
        Section,
        to_field="id",
        on_delete=models.CASCADE,
        related_name="units",
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order_no = models.PositiveIntegerField()

    class UnitType(models.TextChoices):
        COMMON = "common"
        BOSS = "boss"
    unit_type = models.CharField(
        max_length=10,
        choices=UnitType.choices,
        default=UnitType.COMMON,
    )

    boss = models.ForeignKey(
        "Boss",
        to_field="id",
        on_delete=models.SET_NULL,
        related_name="units",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["section", "order_no"]

        constraints = [
            models.UniqueConstraint(
                fields=["section", "order_no"],
                name="unique_unit_order_in_section",
            )
        ]

    def __str__(self):
        return f"{self.section.title} - {self.title}"
"""
Table 5 : Boss
ID : Primary key
Name : Name of the Boss
Description : Description of Boss
Asset key : a key references to boss animation assets
"""
class Boss(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    asset_key = models.CharField(max_length=100)

    def __str__(self):
        return self.name
