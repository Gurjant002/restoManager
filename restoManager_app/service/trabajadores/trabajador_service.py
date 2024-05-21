from django.contrib.auth.models import User
import logging
logger = logging.getLogger(__name__)
class TrabajadorService:
    _trabajadores: User

    def __init__(self):
        self._trabajadores = User()

    def crear_trabajador(self, usuario: str, nombre: str, apellido: str, email: str, password: str, is_staff: bool):
        try:
            self._trabajadores = User.objects.create_user(password=password, email=email, first_name=nombre, last_name=apellido, username=usuario, is_staff=is_staff)
        except Exception as e:
            logger.error(f"Error al crear trabajador: {e}")
            return f"Error al crear trabajador: {e}"
        return self._trabajadores

    def get_trabajador_by_id(self, id_trabajador: int) -> User:
        try:
            return User.objects.get(id=id_trabajador)
        except User.DoesNotExist:
            logger.error(f"No se encontro el trabajador '{id_trabajador}'")
            return f"No se encontro el trabajador '{id_trabajador}'"
        except Exception as e:
            logger.error(f"Ocurrio un error al obtener el trabajador '{id_trabajador}': {str(e)}")
            return f"Ocurrio un error al obtener el trabajador '{id_trabajador}': {str(e)}"

    def get_trabajadores(self) -> User:
        try:
            return User.objects.all()
        except Exception as e:
            logger.error(f"Error al obtener trabajadores: {e}")
            return f"Error al obtener trabajadores: {e}"

