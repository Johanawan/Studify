from django.urls import path
from .views import calculator

urlpatterns = [
    path("calculate/", calculator, name="calculator"),
]