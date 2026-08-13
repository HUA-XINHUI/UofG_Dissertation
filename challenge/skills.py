from store.models import Skill
from django.contrib import messages
import random

def challenge_buffs_initialising(request, character):
    buffs = []
    if character.skill.trigger_type != Skill.TriggerType.PASSIVE:
        return buffs
    match character.skill.name:
        case "Recover":
            buffs.append("Recover")
            return buffs
        case "Greeding":
            buffs.append("Greeding")
            return buffs
    return buffs

def process_after_correct_skill(request, character):
    buffs = request.session["buffs"]
    if "Recover" in buffs:
        if request.session["current_hp"] < character.max_hp:
            request.session["current_hp"] += 1
            messages.success(
                request,
                f"Recover 1 HP!"
            )
        else:
            messages.success(
                request,
                f"Recover 0 HP! HP is full"
            )
        return

def process_after_wrong_skill(request, character):
    buffs = request.session["buffs"]
    if "Cloak of Stealth" in buffs:
        request.session["current_hp"] += 1
        buffs.remove("Cloak of Stealth")
        request.session["buffs"] = buffs
        messages.success(
            request,
            f"Cloak of Stealth activate, you havw resist a hurt"
        )
        return

def process_manual_skill(request, character, current_question):
    buffs = request.session["buffs"]

    if character.skill.trigger_type != Skill.TriggerType.ACTIVE:
        return

    match character.skill.name:
        case "Precision Shot":
            if request.session["current_mp"] > 0:
                removed_options_id = request.session.get("removed_options_id", [])
                wrong_options = list(
                    current_question.options
                    .filter(is_correct=False)
                    .exclude(id__in=removed_options_id)
                )
                if not wrong_options:
                    messages.success(
                        request,
                        f"Failed! there is no more wrong option"
                    )
                    return
                messages.success(
                    request,
                    f"Success! a wrong option has been removed"
                )
                removed_option = random.choice(wrong_options)
                removed_options_id.append(removed_option.id)
                request.session["removed_options_id"] = removed_options_id
                request.session["current_mp"] -= 1
            else:
                messages.success(
                    request,
                    f"Failed! No more mana"
                )

        case "Cloak of Stealth":
            if request.session["current_mp"] <= 0:
                return
            else:   
                if "Cloak of Stealth" in buffs:
                    messages.success(
                        request,
                        f"Failed! You have cloak of stealth now!"
                    )
                    return
                else:
                    buffs.append("Cloak of Stealth")
                    request.session["buffs"] = buffs
                    request.session["current_mp"] -= 1
                    messages.success(
                        request,
                        f"Cloak of Stealth activated"
                    )
                    return