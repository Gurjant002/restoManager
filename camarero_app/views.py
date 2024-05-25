from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from asgiref.sync import sync_to_async
from .controller.camarero_controller import CamareroController
import logging
 
logger = logging.getLogger(__name__)

# Create your views here.
@sync_to_async
@login_required
def home(request: HttpRequest):
    camarero = CamareroController(request)
    diccionario = camarero.peticiones()
    return render(request, "camarero/camarero.html", diccionario)

@sync_to_async
@login_required
def platos(request: HttpRequest):
    camarero = CamareroController()
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