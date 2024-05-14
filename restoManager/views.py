from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from asgiref.sync import sync_to_async

@sync_to_async
@login_required
def home(request: HttpRequest):
    return render(request, "restoManager/home.html", {})

@sync_to_async
@login_required
def puestos(request: HttpRequest):
    return render(request, "restoManager/puestos.html", {})