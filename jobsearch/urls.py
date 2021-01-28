from django.urls import path
from .views import jobSearch

urlpatterns = [
    path("", jobSearch, name="job-search"),
]