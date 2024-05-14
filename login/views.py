from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from asgiref.sync import sync_to_async
import logging

logger = logging.getLogger(__name__)

# Create your views here.
# @sync_to_async
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales incorrectas')
            return redirect('login')
    return render(request, 'login/login.html')