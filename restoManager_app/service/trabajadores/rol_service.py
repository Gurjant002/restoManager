from django.db import IntegrityError
from ...models import Rol
import logging

logger = logging.getLogger(__name__)


class RolService:

    def get_roles(self):
        try:
            roles = Rol.objects.all()
            if not roles:
                logger.warning("No se encontraron roles")
                return "No se encontraron roles"
            return roles
        except Exception as e:
            logger.error(f"Error al obtener los roles: {e}")
            return f"Error al obtener los roles: {e}"

    def get_rol_by_user(self, usuario: int):
        try:
            return Rol.objects.get(user=usuario)
        except Rol.DoesNotExist:
            logger.error(f"No se encontro el rol para el usuario '{usuario}'")
            return f"No se encontro el rol '{usuario}'"
        except Exception as e:
            logger.error(f"Ocurrio un error al obtener el rol '{usuario}': {str(e)}")
            return f"Ocurrio un error al obtener el rol '{usuario}'"
        
    def get_rol_by_user_rol(self, usuario: int, rol: str):
        try:
            return Rol.objects.get(user=usuario, rol=rol)
        except Rol.DoesNotExist:
            logger.error(f"No se encontro el rol '{rol}' para el usuario '{usuario}'")
            return f"No tienes ningun rol asignado, debes avisar al administrador."
        except Exception as e:
            logger.error(f"Ocurrio un error al obtener el rol '{rol}' para el usuario '{usuario}': {str(e)}")
            return f"Ocurrio un error al obtener el rol '{rol}' para el usuario '{usuario}'"

    def crear_rol(self, rol, user):
        try:
            return Rol.objects.create(user=user, rol=rol)
        except IntegrityError as e:
            logger.error(f"Error al crear el rol: {e}")
            return "Este trabajador ya es un rol"
        except Exception as e:
            logger.error(f"Error al crear el rol: {e}")
            return f"Error al crear el rol."

    def actualizar_rol(self, id_rol: int, trabajador):
        try:
            rol = Rol.objects.get(id=id_rol)
            rol.user = trabajador
            rol.save()
            return rol
        except Rol.DoesNotExist:
            logger.error(f"No se encontro el rol '{id_rol}' para actualizar")
            return f"No se encontro el rol '{id_rol}' para actualizar"
        except Exception as e:
            logger.error(f"Ocurrio un error al actualizar el rol '{id_rol}': {str(e)}")
            return f"Ocurrio un error al actualizar el rol '{id_rol}': {str(e)}"

    def eliminar_rol(self, id_rol: int):
        try:
            rol = Rol.objects.get(id=id_rol)
            rol.delete()
            return True
        except Rol.DoesNotExist:
            logger.error(f"No se encontro el rol '{id_rol}' para eliminar")
            return f"No se encontro el rol '{id_rol}' para eliminar"
        except Exception as e:
            logger.error(f"Ocurrio un error al eliminar el rol '{id_rol}': {str(e)}")
            return f"Ocurrio un error al eliminar el rol '{id_rol}': {str(e)}"