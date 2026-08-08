from store.models import Skill

def manual_skill(character):
    if character.skill.trigger_time != Skill.TriggerTime.MANUAL:
        return
    match character.skill.name:
        case "Precision Shot":
            return

def process_after_correct_skill(session, character):
    if character.skill.trigger_time != Skill.TriggerTime.AFTER_CORRECT:
        return
    match character.skill.name:
        case "Recover":
            if session["current_hp"] < character.max_hp:
                session["current_hp"] += 1
            return


# def after_wrong():
# def challenge_end():
# def skill_1(current_hp):
#     after_correct():