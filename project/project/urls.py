from django.urls import path
from app.views import (
    front_times_view,
    no_teen_sum_view,
    xyz_there_view,
    centered_average_view,
)

urlpatterns = [
    path("warmup-2/font-times/", front_times_view, name="front_times"),
    path("logic-2/no-teen-sum/", no_teen_sum_view, name="no_teen_sum"),
    path("string-2/xyz-there/", xyz_there_view, name="xyz_there"),
    path("list-2/centered-average/", centered_average_view, name="centered_average"),
]
