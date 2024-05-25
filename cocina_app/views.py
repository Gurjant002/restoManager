from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from asgiref.sync import sync_to_async

from cocina_app.controller.servicio_cocina_controller import ServicioCocinaController

import logging
 
logger = logging.getLogger(__name__)

@sync_to_async
@login_required
def cocina(request):
    cocina = ServicioCocinaController()
    diccionario = cocina.peticiones(request)
    return render(request, 'cocina/pedidos.html', diccionario)