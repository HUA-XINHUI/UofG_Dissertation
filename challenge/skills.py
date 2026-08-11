from store.models import Skill
import random

# def process_at_beginning(session, character):

#     if character.skill

def process_manual_skill(session, character, current_question):

    if character.skill.trigger_time != Skill.TriggerTime.MANUAL:
        return

    match character.skill.name:
        case "Precision Shot":
            if session["current_mp"] > 0:
                removed_options_id = session.get("removed_options_id", [])
                wrong_options = list(
                    current_question.options
                    .filter(is_correct=False)
                    .exclude(id__in=removed_options_id)
                )
                if not wrong_options:
                    return
                removed_option = random.choice(wrong_options)
                removed_options_id.append(removed_option.id)
                session["removed_options_id"] = removed_options_id
                session["current_mp"] -= 1

        case "Cloak of Stealth":
            if session["current_mp"] > 0:
                removed_options_id = session.get("removed_options_id", [])
                wrong_options = list(
                    current_question.options
                    .filter(is_correct=False)
                    .exclude(id__in=removed_options_id)
                )
                if not wrong_options:
                    return
                removed_option = random.choice(wrong_options)
                removed_options_id.append(removed_option.id)
                session["removed_options_id"] = removed_options_id
                session["current_mp"] -= 1

def process_after_correct_skill(session, character):
    if character.skill.trigger_time != Skill.TriggerTime.AFTER_CORRECT:
        return
    match character.skill.name:
        case "Recover":
            if session["current_hp"] < character.max_hp:
                session["current_hp"] += 1
            return

def process_after_wrong(session, character):
    if character.skill.trigger_time != Skill.TriggerTime.AFTER_CORRECT:
        return

# def after_wrong():
# def challenge_end():
# def skill_1(current_hp):
#     after_correct():