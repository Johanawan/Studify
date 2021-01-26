from django.urls import path
from .views import timer

urlpatterns = [
    path("", timer, name="timer"),
]