"""
Vistas para el manejo de las vistas de la aplicación.
"""

from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request: HttpRequest):
    """
    Vista para la página de inicio de la aplicación.

    Parameters:
        request (HttpRequest): La solicitud HTTP.

    Returns:
        HttpResponse: La respuesta HTTP con la página de inicio.
    """
    return render(request, "restoManager/home.html", {})


@login_required
def puestos(request: HttpRequest):
    """
    Vista para la página de puestos de la aplicación.

    Parameters:
        request (HttpRequest): La solicitud HTTP.

    Returns:
        HttpResponse: La respuesta HTTP con la página de puestos.
    """
    return render(request, "restoManager/puestos.html", {})


def about(request: HttpRequest):
    """
    Vista para la página de acerca de la aplicación.

    Parameters:
        request (HttpRequest): La solicitud HTTP.

    Returns:
        HttpResponse: La respuesta HTTP con la página de acerca de.
    """
    return render(request, "restoManager/about.html", {})
