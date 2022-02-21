from django.urls import path

from . import views

appname = "dashboard"

urlpatterns = [
    # Home view
    path("", views.index, name="index"),
]

