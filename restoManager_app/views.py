from django.http import HttpRequest
from django.shortcuts import render
from datetime import datetime
from asgiref.sync import sync_to_async

# from restoManager_app.models import Plato_Categoria
from .controller.relacion.relacion_plato_categoria_controller import RelacionController
from .controller.bebida.bebida_controller import BebidaController


import logging
logger = logging.getLogger(__name__)
# Create your views here.

def crear_alerta():
    ahora = datetime.now()
    tiempo = ahora.strftime("%H:%M")
    return tiempo

@sync_to_async
def platos(request: HttpRequest):
    diccionario = {}
    relacionController = RelacionController()
    if request.method == "POST":
        if request.POST.get('new-plato-btn'):
            result = {}
            tiempo = crear_alerta()
            result = {
                'resultado':relacionController.tipos_de_peticiones(request),
                'tiempo':tiempo
            }
            logger.info("New Relation Created.")
            diccionario.update({'resultado_new_plato':result})
        
        elif request.POST.get('update-plate-btn'):
            relacionController.tipos_de_peticiones(request)
            
        elif request.POST.get('eliminar-btn'):
            result = relacionController.tipos_de_peticiones(request)
            diccionario.update({'resultado_plato_eliminado': result})
        
        diccionario.update(relacionController.get_lista_relacion())
        return render(request, "restoManager/secciones/platos.html", diccionario)

    diccionario = relacionController.get_lista_relacion()
    return render(request, "restoManager/secciones/platos.html", diccionario)

@sync_to_async
def test(request):
    print("Hola mundo")
    return render(request, "restoManager/base/base.html")

@sync_to_async
def bebidas(request: HttpRequest):
    bebida_controller = BebidaController(request)
    diccionario = bebida_controller.peticiones()
    # logger.info(diccionario)
    return render(request, "restoManager/secciones/bebidas.html", diccionario)