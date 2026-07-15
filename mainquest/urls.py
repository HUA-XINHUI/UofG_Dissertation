from django.urls import path
from . import views

app_name = "mainquest"

urlpatterns = [
    path("", views.home, name="home"),
]