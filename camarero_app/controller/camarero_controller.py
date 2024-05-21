from django.http import HttpRequest
from django.utils.datastructures import MultiValueDictKeyError
from restoManager_app.controller.ubicacion.ubicacion_controller import UbicacionController
from restoManager_app.service.trabajadores.camarero_service import CamareroService
from restoManager_app.service.relacion.relacion_plato_categoria_service import PlatoCategoriaService
from restoManager_app.service.bebida.bebida_service import BebidaService
from .camarero_mesa_controller import CamareroMesaController
from camarero_app.models import Camarero_Mesa
import logging

logger = logging.getLogger(__name__)
class CamareroController:
    ubicacionController: UbicacionController
    req: HttpRequest
    def __init__(self, request: HttpRequest = None):
        self.req = request
        self.camareroService = CamareroService()
        self.camareroMesaController = CamareroMesaController()
        self.ubicacionController = UbicacionController()

    def peticiones(self) -> dict:
        peticion = self.req.POST
        errores = ''
        try:
            if 'add-mesa' in peticion:
                numero_mesa = int(peticion.get('numero-mesa'))
                lugar = int(peticion.get('lugar'))
                camarero = int(peticion.get('camarero'))
                errores = self.crear_mesa(numero_mesa, camarero, lugar)
        except MultiValueDictKeyError:
            logger.error(f'Error al obtener la peticion en CamareroController.peticiones: {peticion}')
            errores = f'Error al obtener la peticion en CamareroController.peticiones: {peticion}'

        return self.respuestas(error=errores)

    def crear_mesa(self, numero_mesa: int, camarero_id, ubicacion_id: int):
        camarero = self.camareroService.get_camarero_by_user(camarero_id)
        ubicacion = self.ubicacionController.get_ubicacion_by_id(ubicacion_id)
        return self.camareroMesaController.crear_mesa(numero_mesa, camarero, ubicacion)

    def get_mesas(self):
        return self.camareroMesaController.get_relaciones()



    def respuestas(self, error: str = None, warning: str = None) -> dict:
        usuario = self.req.user
        mesas = self.get_mesas()
        ubicaciones = UbicacionController().get_ubicaciones()
        camarero = CamareroService().get_camarero_by_user(usuario)
        platos = PlatoCategoriaService().get_lista_relacion_plato_categoria()
        bebidas = BebidaService().get_bebidas()

        if isinstance(camarero, str):
            error = 'Usted no esta asignado como camarero.'
            camarero = False
        else:
            camarero = True

        if isinstance(mesas, str):
            warning = mesas
            mesas = []

        diccionario = {
            'error': error,
            'warning': warning,
            'es_camarero': camarero,
            'mesas': mesas,
            'ubicaciones': ubicaciones,
            'platos': platos,
            'bebidas': bebidas,
        }
        return diccionario
