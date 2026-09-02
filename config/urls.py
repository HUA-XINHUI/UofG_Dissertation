from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("accounts.urls")),
    path("mainquest/", include("mainquest.urls")),
    path("challenge/", include("challenge.urls")),
    path("dailyquest/", include("dailyquest.urls")),
    path("userprofile", include("userprofile.urls")),
    path("store/", include("store.urls")),
]
