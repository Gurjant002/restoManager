from django.http import HttpRequest
from ...service.trabajadores.camarero_service import CamareroService
from ...service.trabajadores.trabajador_service import TrabajadorService
import logging
logger = logging.getLogger(__name__)

class CamareroController:
    _camareroService: CamareroService
    _trabajadorService: TrabajadorService
    req: HttpRequest
    def __init__(self, request: HttpRequest = None):
        self._camareroService = CamareroService()
        self._trabajadorService = TrabajadorService()
        self.req = request

    def peticiones(self):
        peticion = self.req.POST
        errores = ''
        
        if 'add_camarero' in peticion:
            id_trabajador = int(peticion.get('add_camarero'))
            trabajdor = self._trabajadorService.get_trabajador_by_id(id_trabajador)
            errores = self.crear_camarero(trabajdor)
        elif 'eliminar' in peticion:
            id_camarero = int(peticion.get('eliminar'))
            errores = self.eliminar_camarero(id_camarero)

        if errores == '':
            return self.get_response()
        return self.get_response(error=errores)

    def crear_camarero(self, trabajador):
        return self._camareroService.crear_camarero(trabajador)

    def eliminar_camarero(self, id_camarero: int):
        return self._camareroService.eliminar_camarero(id_camarero)

    def get_response(self, error: str = '', warning: str = '') -> dict:
        trabajdores = self._trabajadorService.get_trabajadores()
        camareros = self._camareroService.get_camareros()

        if isinstance(trabajdores, str):
            error = trabajdores
            trabajdores = []
        if isinstance(camareros, str):
            error = camareros
            camareros = []

        diccionario = {
            'error': error,
            'warning': warning,
            'trabajadores': trabajdores,
            'camareros': camareros,
        }
        return diccionario

    """ def get_camareros(self):
        lista = self._camareroService.get_camareros()
        if lista is None:
            return [] """