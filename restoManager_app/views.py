from django.http import HttpRequest
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

# from restoManager_app.models import Plato_Categoria
from .controller.relacion.relacion_plato_categoria_controller import RelacionController
from .controller.bebida.bebida_controller import BebidaController
from .controller.categoria.categoria_controller import CategoriaController
from .controller.ubicacion.ubicacion_controller import UbicacionController
from .controller.trabajadores.trabajador_controller import TrabajadorController
from .controller.trabajadores.rol_controller import CamareroController

import logging
logger = logging.getLogger(__name__)


def crear_alerta():
    ahora = datetime.utcnow()
    tiempo = ahora.strftime("%H:%M")
    return tiempo

 
@login_required
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
        return render(request, "restoManager_app/secciones/platos.html", diccionario)

    diccionario = relacionController.get_lista_relacion()
    # logger.info(diccionario)
    return render(request, "restoManager_app/secciones/platos.html", diccionario)

 
@login_required
def bebidas(request: HttpRequest):
    bebida_controller = BebidaController(request)
    diccionario = bebida_controller.peticiones()
    return render(request, "restoManager_app/secciones/bebidas.html", diccionario)

 
@login_required
def categorias(request: HttpRequest):
    categoria_controller = CategoriaController(request);
    diccionario = categoria_controller.peticiones()
    return render(request, "restoManager_app/secciones/categorias.html", diccionario)

 
@login_required
def ubicaciones(request: HttpRequest):
    ubicaciones_controller = UbicacionController(request)
    diccionario = ubicaciones_controller.peticiones()
    return render(request, "restoManager_app/secciones/ubicaciones.html", diccionario)

 
@login_required
def trabajadores(request: HttpRequest):
    trabajadores_controller = TrabajadorController(request)
    diccionario = trabajadores_controller.peticiones()
    return render(request, "restoManager_app/secciones/trabajadores.html", diccionario)

def camareros(request: HttpRequest):
    camareros_controller = CamareroController(request)
    diccionario = camareros_controller.peticiones()
    return render(request, "restoManager_app/secciones/trabajadores/camareros.html", diccionario)

 
@login_required
def home(request: HttpRequest):
    return render(request, "restoManager_app/config.html")