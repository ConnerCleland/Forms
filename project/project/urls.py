# app/urls.py
from django.urls import path
from app.views import (
    front_times_view,
    no_teen_sum_view,
    xyz_there_view,
    centered_average_view,
)

urlpatterns = [
    path("front/", front_times_view, name="front_times"),
    path("no_teen/", no_teen_sum_view, name="no_teen_sum"),
    path("xyz_there/", xyz_there_view, name="xyz_there"),
    path("centered/", centered_average_view, name="centered_average"),
]
