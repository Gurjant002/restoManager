from django.http import HttpRequest

from ...service.trabajadores.trabajador_service import TrabajadorService
from ...service.trabajadores.rol_service import RolService
import logging
import re
logger = logging.getLogger(__name__)

emailValidador = r"^[a-zA-Z0-9].[a-zA-Z0-9\._%\+\-]{0,63}@[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,30}$"
passwordValidador = r"(?=^.{10,}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^a-zA-Z\d])"

class TrabajadorController:
    _trabajadorService: TrabajadorService
    _rolService: RolService
    req: HttpRequest

    def __init__(self, request: HttpRequest = None):
        self._trabajadorService = TrabajadorService()
        self._rolService = RolService()
        self.req = request
        self.error: str = None

    def peticiones(self):
        peticion = self.req.POST
        if peticion.get('registrar'):
            usuario = peticion.get('usuario')
            nombre = peticion.get('nombre').capitalize()
            apellido = peticion.get('apellido').capitalize()
            email = peticion.get('email')
            password1 = peticion.get('password1')
            password2 = peticion.get('password2')
            rol = peticion.get('rol')
            if password1 != password2:
                logger.error("Las contraseñas no coinciden")
                return self.response(error="Las contraseñas no coinciden")
            elif not re.search(passwordValidador, password1):
                logger.error("La contraseña no es valida: Debe contener al menos 1 mayuscula, 1 minuscula, 1 numero, 1 caracter especial y una longitud minima de 10 caracteres")
                return self.response(error="La contraseña no es valida: Debe contener al menos 1 mayuscula, 1 minuscula, 1 numero, 1 caracter especial y una longitud minima de 10 caracteres")
            if not re.search(emailValidador, email):
                logger.error("El correo no es valido")
                return self.response(error="El correo no es valido")
            trabajadores = self.get_trabajadores()
            if any(t.username == usuario for t in trabajadores):
                logger.error("El usuario ya existe")
                return self.response(error="El usuario ya existe")
                return self.response(error="El usuario ya existe")

            self.crear_usuario(usuario, nombre, apellido, email, password1, rol)

        if "registrar_admin" in peticion:
            try:
                usuario = peticion.get('username')
                nombre = peticion.get('first_name').capitalize()
                apellido = peticion.get('last_name').capitalize()
                email = peticion.get('email')
                password1 = peticion.get('password1')
                password2 = peticion.get('password2')
                rol = "Administrador"
                is_Superuser = True
                if password1 != password2:
                    logger.error("Las contraseñas no coinciden")
                    return self.response(error="Las contraseñas no coinciden")
                elif not re.search(passwordValidador, password1):
                    logger.error("La contraseña no es valida: Debe contener al menos 1 mayuscula, 1 minuscula, 1 numero, 1 caracter especial y una longitud minima de 10 caracteres")
                    return self.response(error="La contraseña no es valida: Debe contener al menos 1 mayuscula, 1 minuscula, 1 numero, 1 caracter especial y una longitud minima de 10 caracteres")
                if not re.search(emailValidador, email):
                    logger.error("El correo no es valido")
                    return self.response(error="El correo no es valido")
                if self.get_trabajadores().filter(username=usuario).exists():
                    logger.error("El usuario ya existe")
                    return self.response(error="El usuario ya existe")
                
                self.error = self.crear_usuario(usuario, nombre, apellido, email, password1, rol)
            except Exception as e:
                logger.error(f"Error al registrar administrador: {e}")
                error = f"Algo salio mal, vuelva a intenterlo."
                return self.response(error=error)
        return self.response()

    def crear_usuario(self, usuario: str, nombre: str, apellido: str, email: str, password: str, rol: str):
        if rol == "Administrador":
            is_Superuser = True
            trabajador = self._trabajadorService.crear_trabajador(usuario, nombre, apellido, email, password, is_Superuser)
            if isinstance(trabajador, str):
                self.error = trabajador
                return
            else:
                if rol in ['Camarero', 'Cocinero', 'Cajero', 'Barman', 'Administrador']:
                    self._rolService.crear_rol(rol, trabajador)
        else:
            is_Superuser = False
            trabajador = self._trabajadorService.crear_trabajador(usuario, nombre, apellido, email, password, is_Superuser)
            if isinstance(trabajador, str):
                self.error = trabajador
                return
            else:
                if rol in ['Camarero', 'Cocinero', 'Cajero', 'Barman', 'Administrador']:
                    self._rolService.crear_rol(rol, trabajador)
    
    def get_trabajadores(self):
        return self._trabajadorService.get_trabajadores()

    def response(self, error: str = None, warning: str = None) -> dict:
        if isinstance(error, str):
            self.error = error
        
        diccionario = {
            'error': self.error,
            'warning': warning,
            'trabajadores': self.get_trabajadores()
        }
        return diccionario