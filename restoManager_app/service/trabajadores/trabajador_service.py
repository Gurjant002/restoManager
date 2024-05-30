from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger(__name__)


class TrabajadorService:
    """Clase que implementa métodos para manejar los trabajadores"""

    def __init__(self):
        """Inicializa el objeto"""
        self._trabajadores = User()

    def crear_trabajador(self, usuario: str, nombre: str, apellido: str, email: str, password: str, is_Superuser: bool) -> User:
        """Crea un trabajador y devuelve su instancia"""
        try:
            self._trabajadores = User.objects.create_user(password=password, email=email, first_name=nombre, last_name=apellido, username=usuario, is_staff=True, is_superuser=is_Superuser)
        except Exception as e:
            logger.error(f"Error al crear trabajador: {e}")
            return f"Error al crear trabajador: {e}"
        return self._trabajadores
   
    def crear_administrador(self, usuario: str, nombre: str, apellido: str, email: str, password: str, is_staff: bool, is_Superuser: bool) -> User:
        """Crea un administrador y devuelve su instancia"""
        try:
            self._trabajadores = User.objects.create_user(password=password, email=email, first_name=nombre, last_name=apellido, username=usuario, is_staff=is_staff, is_superuser=is_Superuser)
        except Exception as e:
            logger.error(f"Error al crear administrador: {e}")
            return f"Error al crear administrador: {e}"
        return self._trabajadores

    def get_trabajador_by_id(self, id_trabajador: int) -> User:
        """Obtiene un trabajador por su id y devuelve su instancia"""
        try:
            return User.objects.get(id=id_trabajador)
        except ObjectDoesNotExist:
            logger.error(f"No se encontro el trabajador '{id_trabajador}'")
            return f"No se encontro el trabajador '{id_trabajador}'"
        except Exception as e:
            logger.error(f"Ocurrio un error al obtener el trabajador '{id_trabajador}': {str(e)}")
            return f"Ocurrio un error al obtener el trabajador '{id_trabajador}': {str(e)}"

    def get_trabajadores(self) -> list:
        """Obtiene todos los trabajadores y devuelve una lista"""
        try:
            return list(User.objects.all())
        except Exception as e:
            logger.error(f"Error al obtener trabajadores: {e}")
            return f"Error al obtener trabajadores: {e}"

