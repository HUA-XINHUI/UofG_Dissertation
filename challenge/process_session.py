def challenge_session_initialising(request, character):

    request.session["challenge_activate"] = True
    request.session["is_win"] = False
    request.session["current_index"] = 0
    request.session["total_correct"] = 0
    request.session["total_wrong"] = 0

    request.session["character_id"] = character.id
    request.session["current_hp"] = character.max_hp
    request.session["current_mp"] = character.max_mp
    request.session["current_buff"] = []


def challenge_session_clearing(request):

    request.session["challenge_activate"] = False
    request.session.pop("is_win", None)
    request.session.pop("current_index", None)
    request.session.pop("total_correct", None)
    request.session.pop("total_wrong", None)

    request.session.pop("character_id", None)
    request.session.pop("current_hp", None)
    request.session.pop("current_mp", None)
    request.session.pop("current_buff", None)

def question_session_initialising(request):

    request.session["removed_options_id"] = []

def question_session_clearing(request):

    request.session.pop("removed_options_id", None)
