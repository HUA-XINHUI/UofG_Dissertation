from django.db import models

"""
table 10 : Character
ID : Primary Key
Character class : the class of this character
Name/Description : the textual information about this character
Max hp : max health point of this character
Max mp : max mana point of this character, can be none
Attack type : melee or ranged attack
Skill : Foreign key, references to skill id in table 11
Unlock price : gold price of this character to unlock
Is default : True/False about the character is default starter character
Asset key : a key references to character animation assets
"""
class Character(models.Model):

    id = models.BigAutoField(primary_key=True)
    class CharacterClass(models.TextChoices):
        WARRIOR = "warrior"
        ARCHER = "archer"
        ROGUE = "rogue"
        MAGE = "mage"
        ALCHEMIST = "alchemist"
    character_class = models.CharField(
        max_length=30,
        choices=CharacterClass.choices,
    )
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    max_hp = models.PositiveIntegerField()
    max_mp = models.PositiveIntegerField(blank=True, null=True)

    class AttackType(models.TextChoices):
        MELEE = "melee"
        RANGED = "ranged"
    attack_type = models.CharField(
        max_length=10,
        choices=AttackType.choices)

    skill = models.ForeignKey(
        "store.Skill",
        to_field="id",
        on_delete=models.PROTECT,
        related_name="characters",
        blank=True,
    )

    unlock_price = models.PositiveIntegerField()
    is_default = models.BooleanField(default=False)
    asset_key = models.CharField(max_length=30, blank=True,)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["is_default"],
                condition=models.Q(is_default=True),
                name="unique_default_character",
            )
        ]

    def __str__(self):
        return f"No{self.id} : {self.name}"
"""
table 11 : Skill
ID : Primary Key
Name/Description : the textual information about this skill
TriggerTime : active skill or passive skill
Effect value : The value of this effect
Resource type : none, mana or limited use
Max uses count : if item, the max uses count in one challenge
Resource cost : if mana, the mana cost
"""
class Skill(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    class TriggerTime(models.TextChoices):
        MANUAL = "manual"
        AFTER_CORRECT = "after_correct"
        AFTER_WRONG = "after_wrong"
        CHALLENGE_END = "challenge_end"
    trigger_time = models.CharField(
        max_length=30,
        choices=TriggerTime.choices,
    )

    effect_value = models.IntegerField()

    class ResourceType(models.TextChoices):
        NONE = "none"
        MANA = "mana"
        LIMITED_USE = "limited_use"
    resource_type = models.CharField(
        max_length=20,
        choices=ResourceType.choices,
    )

    max_uses_count = models.PositiveIntegerField(blank=True, null=True)
    resource_cost = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} : {self.name}"