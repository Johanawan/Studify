from django.urls import path
from .views import dictionaryView

urlpatterns = [
    path("", dictionaryView, name="dictionary"),
]