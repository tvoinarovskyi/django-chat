# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path("<str:room_name>/get_messages", views.get_messages, name="get_messages"),
    path("<str:room_name>/send_message", views.send_message, name="send_message"),
]
