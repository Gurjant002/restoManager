from django.http import HttpRequest
from django.shortcuts import render
from datetime import datetime

# from restoManager_app.models import Plato_Categoria
from .controller.relacion_plato_categoria_controller import RelacionController

# Create your views here.

import logging
logger = logging.getLogger(__name__)

def crear_alerta():
    ahora = datetime.now()
    tiempo = ahora.strftime("%H:%M")
    return tiempo

def actualizar_cat_plato(post_request: HttpRequest):
    idPlato = post_request.POST.get("id-plato")
    numeroPlato = post_request.POST.get("numero-plato")
    nombrePlato = post_request.POST.get("nombre-plato")
    categoria = post_request.POST.get("categoria")
    descripcion = post_request.POST.get("descripcion")
    estado = int(post_request.POST.get("estado"))
    
def crear_plato(request):
    print("Hola")

# Views
def platos(request):
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

def test(request):
    print("Hola mundo")
    return render(request, "restoManager/base/base.html")