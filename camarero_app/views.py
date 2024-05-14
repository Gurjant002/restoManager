from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from asgiref.sync import sync_to_async

# Create your views here.
@sync_to_async
@login_required
def home(request: HttpRequest):
    
    return render(request, "camarero/camarero.html", {})