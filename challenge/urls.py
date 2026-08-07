from django.urls import path
from . import views

app_name = "challenge"

urlpatterns = [
    path(
        "unit/<int:unit_id>/",
        views.home,
        name="home"),
    path(
        "finish/",
        views.finish,
        name="finish"
    )
]