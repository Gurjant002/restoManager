"""
Controlador de la aplicación Camarero
"""

import logging
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .controller.camarero_controller import CamareroController

logger = logging.getLogger(__name__)


@login_required
def home(request: HttpRequest):
    """
    Renderiza la página de inicio del camarero
    """
    camarero = CamareroController(request)
    diccionario = camarero.peticiones()
    if request.method == 'POST':
        return redirect('camarero_home')
    else:
        return render(request, "camarero/camarero.html", diccionario)


@login_required
def platos(request: HttpRequest):
    """
    Devuelve una lista de platos en formato JSON
    """
    camarero = CamareroController(request)
    platos = camarero.lista_platos()
    datos = []
    for plato in platos:
        plato_dict = {
            'id': plato.id,
            'numero_menu': plato.numero_menu,
            'nombre': plato.plato.nombre,
            'descripcion': plato.plato.descripcion,
            'categoria': plato.categoria.nombre
        }
        datos.append(plato_dict)
    return JsonResponse(datos, safe=False)
