"""
Define las vistas de inicio de sesión y cierre de sesión.
"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

import logging

from restoManager_app.controller.trabajadores.trabajador_controller import TrabajadorController

logger = logging.getLogger(__name__)

def login_view(request: HttpRequest):
    """
    Esta función maneja el inicio de sesión. Si hay un superusuario registrado
    o el formulario de registro se envía, se autentica el usuario y se redirige
    a la página de inicio. Si hay un error de autenticación, se muestra un mensaje
    de error y se redirige a la página de inicio de sesión. Si no hay un superusuario
    registrado, se registra un mensaje de advertencia y se redirige a la página de
    registro.
    """
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
    """
    Esta función maneja el cierre de sesión. Finaliza la sesión del usuario y
    muestra un mensaje de éxito. Luego redirige a la página de información.
    """
    logout(request)
    messages.success(request, 'Sesión cerrada')
    return redirect('about')

