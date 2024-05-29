# Cocina_App
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from cocina_app.controller.servicio_cocina_controller import ServicioCocinaController

import logging
 
logger = logging.getLogger(__name__)

@login_required
def cocina(request: HttpRequest):
    cocina = ServicioCocinaController(request)
    diccionario = cocina.peticiones(request)
    if request.method == 'POST':
        return redirect(reverse('cocina')+f'?listar_mesa={diccionario["listar_mesa"]}')
    else:
        return render(request, 'cocina/pedidos.html', diccionario)


@login_required
def mesas_pedidos(request):
    cocina = ServicioCocinaController()
    lista = cocina.get_servicio_mesa_cantidad_pedidos()
    diccionario = {
        'pedidos_lista':lista
        }
    return JsonResponse(diccionario)