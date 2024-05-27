from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cocina_app.controller.servicio_cocina_controller import ServicioCocinaController

import logging
 
logger = logging.getLogger(__name__)

@login_required
def cocina(request: HttpRequest):
    cocina = ServicioCocinaController()
    diccionario = cocina.peticiones(request)
    return render(request, 'cocina/pedidos.html', diccionario)
