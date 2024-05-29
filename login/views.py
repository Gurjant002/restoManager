from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from restoManager_app.controller.trabajadores.trabajador_controller import TrabajadorController
from django.contrib import messages

import logging

logger = logging.getLogger(__name__)

# Create your views here.
 
def login_view(request: HttpRequest):
    # Check if there is any superuser in the user model
    if User.objects.filter(is_superuser=True).exists() or "registrar_admin" in request.POST:
        if "iniciar_sesion" in request.POST:
            username = request.POST.get('usuario')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciales incorrectas')
                return redirect('login')
        elif "registrar_admin" in request.POST:
            administrador = TrabajadorController(request)
            diccionario = administrador.peticiones()
            if diccionario['error']:
                return render(request, 'registration/registrar.html', diccionario)
            
        return render(request, 'registration/login.html')
    else:
        logger.warning('No hay superusuario en el sistema')
        return render(request, 'registration/registrar.html')

@login_required
def salir(request: HttpRequest):
    logout(request)
    messages.success(request, 'Sesión cerrada')
    return redirect('about')

