from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q

from . import skills
from challenge.models import QuestionOption
from mainquest.models import Unit

def initialise_challenge_sessions(request, questions, character):

    request.session["challenge_activate"] = True
    request.session["is_end"] = False
    request.session["is_win"] = None
    request.session["current_index"] = 0
    request.session["total_questions"] = questions.count()
    request.session["total_correct"] = 0
    request.session["total_wrong"] = 0

    request.session["character_id"] = character.id
    request.session["current_hp"] = character.max_hp
    request.session["current_mp"] = character.max_mp
    request.session["buffs"] = skills.challenge_buffs_initialising(request)

def clear_challenge_sessions(request):

    request.session["challenge_activate"] = False
    request.session.pop("is_end", None)
    request.session.pop("is_win", None)
    request.session.pop("current_index", None)
    request.session.pop("total_questions", None)
    request.session.pop("total_correct", None)
    request.session.pop("total_wrong", None)

    request.session.pop("character_id", None)
    request.session.pop("current_hp", None)
    request.session.pop("current_mp", None)
    request.session.pop("buffs", None)

def initialise_question_sessions(request):
    request.session["removed_options_id"] = []

def clear_question_sessions(request):
    request.session.pop("removed_options_id", None)

def get_next_unit(current_unit):
        return (
        Unit.objects
        .filter(
            Q(
                section__order_no=current_unit.section.order_no,
                order_no__gt=current_unit.order_no,
            )
            |
            Q(
                section__order_no__gt=current_unit.section.order_no
            )
        )
        .order_by(
            "section__order_no",
            "order_no",
        )
        .first()
    )

def pack_challenge_data(request, unit_id):
    challenge_data = {
        "playerAlias" : request.user.user_profile.alias,
        "characterId" : request.session["character_id"],
        "currentHp" : request.session["current_hp"],
        "currentMp" : request.session["current_mp"],
        "buffs" : request.session["buffs"],
        "bossName" : Unit.objects.get(id=unit_id).boss.name,
        "bossMaxHp" : request.session["total_questions"],
        "bossCurrentHp" : request.session["total_questions"] - request.session["total_correct"],
    }
    return challenge_data

def pack_question_data(request, current_question):
    question_data = {
        "id" : current_question.id,
        "orderNo" : current_question.order_no,
        "title" : current_question.title,
        "description" : current_question.description,
        "questionType" : current_question.question_type,
        "explanation" : current_question.explanation,
        "options" : [
            {
                "id" : option.id,
                "orderNo" : option.order_no,
                "title" : option.title,
                "description" : option.description,
            }
            for option in current_question.options.all()
        ],
        "removedOptionsId" : request.session["removed_options_id"]
    }
    return question_data

def check_ending_or_not(request):
    if request.session["current_hp"] <= 0:
        request.session["is_win"] = False
        return True
    if request.session["total_correct"] == request.session["total_questions"]:
        request.session["is_win"] = True
        return True
    return False

def fetch_next_question(request, questions):
    request.session["current_index"] += 1
    current_question = questions[request.session["current_index"]]
    question_data = pack_question_data(request, current_question)
    return question_data