from django.http import HttpRequest
from django.shortcuts import render
from asgiref.sync import sync_to_async

@sync_to_async
def home(request: HttpRequest):
    return render(request, "restoManager/home.html", {})

@sync_to_async
def puestos(request: HttpRequest):
    return render(request, "restoManager/puestos.html", {})