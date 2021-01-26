from django.urls import path
from .views import todo, updateTask, deleteTask

urlpatterns = [
    path("", todo, name="todo"),
    path("update-task/<str:pk>/", updateTask, name="update-task"),
    path("delete-task/<str:pk>/", deleteTask, name="delete-task"),
]