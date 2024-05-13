from django.http import HttpRequest
from django.shortcuts import render
from asgiref.sync import sync_to_async

# Create your views here.
@sync_to_async
def home(request: HttpRequest):
    return render(request, "camarero/home.html", {})