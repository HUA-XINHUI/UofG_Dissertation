from django.shortcuts import render

def home(request):
    user = request.user
    user_profile = user.user_profile
    user_task_data = user.user_task_data

    accuracy = round( user_task_data.total_correct_answered / user_task_data.total_questions_answered * 100, 2)
    
    context={
        "user_profile" : user_profile,
        "user_task_data" : user_task_data,
        "accuracy" : accuracy
    }
    return render(request, "userprofile/userprofile.html", context)