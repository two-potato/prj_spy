from django.contrib import admin
from django.urls import include, path
from .views import TeletestView

app_name = "teletest"

urlpatterns = [
    path("teletest/", TeletestView.as_view(), name="index"),
]
