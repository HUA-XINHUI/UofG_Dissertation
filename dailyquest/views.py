from django.shortcuts import render



def home(request):

    # if request.session.get["last_dailyquest1_complete_date"] == today:

    # if request.session.get["last_dailyquest2_complete_date"]:

    # if request.session.get["last_dailyquest3_complete_date"]:

    # request.session["last_dailychallenge_complete_date"] = 0
    # request.session["progress_date"] = None
    # request.session["total_questions_finished_today"] = None
    # request.session["total_units_finished_today"] = None

    # daily_correct_count = request.session["daily_correct_count"]

    # context = {
    #     "daily_correct_count" : daily_correct_count
    # }

    return render(request, "dailyquest/dailyquest.html")