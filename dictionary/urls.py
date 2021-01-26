from django.urls import path
from .views import dictionaryView

urlpatterns = [
    path("dictionary/", dictionaryView, name="dictionary"),
]