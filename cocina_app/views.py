from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from asgiref.sync import sync_to_async

from cocina_app.controller.servicio_cocina_controller import ServicioCocinaController

import logging
 
logger = logging.getLogger(__name__)

@sync_to_async
@login_required
def cocina(request: HttpRequest):
    cocina = ServicioCocinaController()
    diccionario = cocina.peticiones(request)
    return render(request, 'cocina/pedidos.html', diccionario)

@sync_to_async
@login_required
def mesas_pedidos(request):
    cocina = ServicioCocinaController()
    lista = cocina.get_servicio_mesa_cantidad_pedidos()
    diccionario = {
        'pedidos_lista':lista
        }
    return JsonResponse(diccionario)

@sync_to_async
@login_required
def cambiar_estado(request: HttpRequest):
    cocina = ServicioCocinaController()
    id = int(request.POST['cambiar-estado'].split('-')[0])
    estado = request.POST['cambiar-estado'].split('-')[1]
    diccionario = cocina.cambiar_estado_servicio(id, estado)
    return render('puesto/cocina/',diccionario)

def listar(request: HttpRequest):
    cocina = ServicioCocinaController()
    lista = cocina.get_servicio_mesa_cantidad_pedidos()
    diccionario = {
        'pedidos_lista':lista
        }
    return render(request, 'cocina/lista_pedidos.html', diccionario)
    # return render(request, 'cocina/listar.html')