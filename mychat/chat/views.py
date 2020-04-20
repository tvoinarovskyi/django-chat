import coolname
import json
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

ROOMS = {}


class Room:
    def __init__(self):
        self._create_time = datetime.now()
        self._history = []

    def add_message(self, message):
        self._history.append(message)

    def get_messages(self):
        return self._history


def get_room(room_name):
    if room_name not in ROOMS:
        ROOMS[room_name] = Room()
    return ROOMS[room_name]


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    if "user_name" not in request.session:
        first, last = coolname.generate(2)
        first = first.capitalize()
        last = last.capitalize()
        user_name = first + " " + last
        request.session["user_name"] = user_name
    user_name = request.session["user_name"]
    return render(
        request,
        "chat/room.html",
        {"chat_data": {"room_name": room_name, "user_name": user_name}},
    )


def get_messages(request, room_name):
    history = get_room(room_name).get_messages()
    return JsonResponse({"history": history})


@csrf_exempt
def send_message(request, room_name):
    message = json.loads(request.body.decode())
    room = get_room(room_name)
    room.add_message(message)
    history = room.get_messages()
    return JsonResponse({"history": history})
