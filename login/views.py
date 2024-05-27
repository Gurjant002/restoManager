from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

import logging

logger = logging.getLogger(__name__)

# Create your views here.
 
def login_view(request):
    # Check if there is any superuser in the user model
    if User.objects.filter(is_superuser=True).exists():
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
    else:
        logger.warning('There is no superuser registered in the system')
        return render(request, 'login/registrar.html')
