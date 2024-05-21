from django.http import HttpRequest

from ...service.trabajadores.trabajador_service import TrabajadorService
import logging
import re
logger = logging.getLogger(__name__)

regex = r"^[a-zA-Z0-9].[a-zA-Z0-9\._%\+\-]{0,63}@[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,30}$"

class TrabajadorController:
    _trabajadorService: TrabajadorService
    req: HttpRequest

    def __init__(self, request: HttpRequest = None):
        self._trabajadorService = TrabajadorService()
        self.req = request

    def peticiones(self):
        peticion = self.req.POST
        if peticion.get('registrar'):
            usuario = peticion.get('usuario')
            nombre = peticion.get('nombre')
            apellido = peticion.get('apellido')
            email = peticion.get('email')
            password1 = peticion.get('password1')
            password2 = peticion.get('password2')
            is_staff = peticion.get('is_staff')
            if password1 != password2:
                return self.response(error="Las contraseñas no coinciden")
            if not re.search(regex, email):
                return self.response(error="El correo no es valido")
            if self.get_trabajadores().filter(username=usuario).exists():
                return self.response(error="El usuario ya existe")

            self.crear_usuario(usuario, nombre, apellido, email, password1, is_staff)
        
        return self.response()

    def crear_usuario(self, usuario: str, nombre: str, apellido: str, email: str, password: str, is_staff: bool):
        return self._trabajadorService.crear_trabajador(usuario, nombre, apellido, email, password, is_staff)
    
    def get_trabajadores(self):
        return self._trabajadorService.get_trabajadores()

    def response(self, error: str = None, warning: str = None) -> dict:
        diccionario = {
            'error': error,
            'warning': warning,
            'trabajadores': self.get_trabajadores()
        }
        return diccionario