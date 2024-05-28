from django.http import HttpRequest
from ...service.trabajadores.rol_service import RolService
from ...service.trabajadores.trabajador_service import TrabajadorService
import logging
logger = logging.getLogger(__name__)

class CamareroController:
    _rolService: RolService
    _trabajadorService: TrabajadorService
    req: HttpRequest
    def __init__(self, request: HttpRequest = None):
        self._rolService = RolService()
        self._trabajadorService = TrabajadorService()
        self.req = request

    def peticiones(self):
        peticion = self.req.POST
        errores = ''
        
        if 'add_rol' in peticion:
            id_trabajador = int(peticion.get('add_rol'))
            trabajdor = self._trabajadorService.get_trabajador_by_id(id_trabajador)
            errores = self.crear_rol(trabajdor)
        elif 'eliminar' in peticion:
            id_rol = int(peticion.get('eliminar'))
            errores = self.eliminar_rol(id_rol)

        if errores == '':
            return self.get_response()
        return self.get_response(error=errores)

    def crear_rol(self, trabajador):
        return self._rolService.crear_rol(trabajador)

    def eliminar_rol(self, id_rol: int):
        return self._rolService.eliminar_rol(id_rol)

    def get_response(self, error: str = '', warning: str = '') -> dict:
        trabajdores = self._trabajadorService.get_trabajadores()
        rol = self._rolService.get_rols()

        if isinstance(trabajdores, str):
            error = trabajdores
            trabajdores = []
        if isinstance(rol, str):
            error = rol
            rol = []

        diccionario = {
            'error': error,
            'warning': warning,
            'trabajadores': trabajdores,
            'rol': rol,
        }
        return diccionario

    """ def get_rols(self):
        lista = self._rolService.get_rols()
        if lista is None:
            return [] """