from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request: HttpRequest):
    return render(request, "restoManager/home.html", {})

 
@login_required
def puestos(request: HttpRequest):
    return render(request, "restoManager/puestos.html", {})

def about(request: HttpRequest):
    return render(request, "restoManager/about.html", {})