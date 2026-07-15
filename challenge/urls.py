from django.urls import path
from . import views

app_name = "challenge"

urlpatterns = [
    path("", views.home, name="home"),
]