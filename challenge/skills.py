from store.models import Skill
from django.contrib import messages
import random

# def process_at_beginning(session, character):

#     if character.skill

def process_manual_skill(request, character, current_question):

    if character.skill.trigger_time != Skill.TriggerTime.MANUAL:
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
            if request.session["current_mp"] > 0:
                removed_options_id = request.session.get("removed_options_id", [])
                wrong_options = list(
                    current_question.options
                    .filter(is_correct=False)
                    .exclude(id__in=removed_options_id)
                )
                if not wrong_options:
                    return
                removed_option = random.choice(wrong_options)
                removed_options_id.append(removed_option.id)
                request.session["removed_options_id"] = removed_options_id
                request.session["current_mp"] -= 1

def process_after_correct_skill(request, character):
    if character.skill.trigger_time != Skill.TriggerTime.AFTER_CORRECT:
        return
    match character.skill.name:
        case "Recover":
            if request.session["current_hp"] < character.max_hp:
                request.session["current_hp"] += 1
            return

def process_after_wrong(request, character):
    if character.skill.trigger_time != Skill.TriggerTime.AFTER_CORRECT:
        return

# def after_wrong():
# def challenge_end():
# def skill_1(current_hp):
#     after_correct():