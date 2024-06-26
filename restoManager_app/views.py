from django.http import HttpRequest
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from restoManager_app.controller.relacion.relacion_plato_categoria_controller import RelacionController
from restoManager_app.controller.bebida.bebida_controller import BebidaController
from restoManager_app.controller.categoria.categoria_controller import CategoriaController
from restoManager_app.controller.ubicacion.ubicacion_controller import UbicacionController
from restoManager_app.controller.trabajadores.trabajador_controller import TrabajadorController
from restoManager_app.controller.trabajadores.rol_controller import CamareroController
from restoManager_app.service.trabajadores.rol_service import RolService
import logging

logger = logging.getLogger(__name__)


def crear_alerta():
    """
    Crea una cadena con la hora actual en formato HH:MM.

    Returns:
        str: La hora actual en formato HH:MM.
    """
    ahora = timezone.now()
    tiempo = ahora.strftime("%H:%M")
    return tiempo

def validar_rol(request: HttpRequest):
    """
    Valida el rol del usuario que realiza la solicitud.

    Args:
        request (HttpRequest): El objeto de solicitud HTTP.

    Returns:
        bool: True si el usuario es un administrador, False de lo contrario.
    """
    rolService = RolService()
    usuario = request.user
    administrador = rolService.get_rol_by_user_rol(usuario, "Administrador")
    if isinstance(administrador, str) or administrador is None:
        administrador = False
    return administrador

@login_required
def platos(request: HttpRequest):
    """
    Maneja las peticiones de la sección de platos.

    Args:
        request (HttpRequest): La petición HTTP.

    Returns:
        HttpResponse: La respuesta HTTP con la plantilla de la sección de platos.
    """
    diccionario = {}
    relacionController = RelacionController(request)
    if request.method == "POST":
        if request.POST.get('new-plato-btn'):
            result = {}
            tiempo = crear_alerta()
            result = {
                'resultado': relacionController.tipos_de_peticiones(request),
                'tiempo': tiempo
            }
            logger.info("Nueva relación creada.")
            diccionario.update({'resultado_new_plato': result})

        elif request.POST.get('update-plate-btn'):
            relacionController.tipos_de_peticiones(request)

        elif request.POST.get('eliminar-btn'):
            result = relacionController.tipos_de_peticiones(request)
            diccionario.update({'resultado_plato_eliminado': result})

        diccionario.update(relacionController.get_lista_relacion())
        
        diccionario.update({'administrador': validar_rol(request)})
        return render(request, "restoManager_app/secciones/platos.html", diccionario)

    diccionario = relacionController.get_lista_relacion()
    diccionario.update({'administrador': validar_rol(request)})
    return render(request, "restoManager_app/secciones/platos.html", diccionario)


@login_required
def bebidas(request: HttpRequest):
    """
    Maneja las peticiones de la sección de bebidas.

    Args:
        request (HttpRequest): La petición HTTP.

    Returns:
        HttpResponse: La respuesta HTTP con la plantilla de la sección de bebidas.
    """
    bebida_controller = BebidaController(request)
    diccionario = bebida_controller.peticiones()
    diccionario.update({'administrador': validar_rol(request)})
    return render(request, "restoManager_app/secciones/bebidas.html", diccionario)


@login_required
def categorias(request: HttpRequest):
    """
    Maneja las peticiones de la sección de categorías.

    Args:
        request (HttpRequest): La petición HTTP.

    Returns:
        HttpResponse: La respuesta HTTP con la plantilla de la sección de categorías.
    """
    categoria_controller = CategoriaController(request)
    diccionario = categoria_controller.peticiones()
    diccionario.update({'administrador': validar_rol(request)})
    return render(request, "restoManager_app/secciones/categorias.html", diccionario)


@login_required
def ubicaciones(request: HttpRequest):
    """
    Maneja las peticiones de la sección de ubicaciones.

    Args:
        request (HttpRequest): La petición HTTP.

    Returns:
        HttpResponse: La respuesta HTTP con la plantilla de la sección de ubicaciones.
    """
    ubicaciones_controller = UbicacionController(request)
    diccionario = ubicaciones_controller.peticiones()
    diccionario.update({'administrador': validar_rol(request)})
    return render(request, "restoManager_app/secciones/ubicaciones.html", diccionario)


@login_required
def trabajadores(request: HttpRequest):
    """
    Maneja las peticiones de la sección de trabajadores.

    Args:
        request (HttpRequest): La petición HTTP.

    Returns:
        HttpResponse: La respuesta HTTP con la plantilla de la sección de trabajadores.
    """
    trabajadores_controller = TrabajadorController(request)
    diccionario = trabajadores_controller.peticiones()
    diccionario.update({'administrador': validar_rol(request)})
    return render(request, "restoManager_app/secciones/trabajadores.html", diccionario)
 
@login_required
def home(request: HttpRequest):
    """
    Muestra la página de configuración.

    Args:
        request (HttpRequest): La petición HTTP.

    Returns:
        HttpResponse: La respuesta HTTP con la plantilla de la página de configuración.
    """
    diccionario = {}
    diccionario.update({'administrador': validar_rol(request)})
    return render(request, "restoManager_app/config.html", diccionario)
