from django.urls import path
from . import views

app_name = "dailyquest"

urlpatterns = [
    path("", views.home, name="home"),
]