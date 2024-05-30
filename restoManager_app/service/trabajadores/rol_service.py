from django.db import IntegrityError
from ...models import Rol
import logging


logger = logging.getLogger(__name__)


class RolService:
    """
    Clase que proporciona funciones para gestionar los roles de los usuarios
    """

    def get_roles(self) -> list or str:
        """
        Obtiene todos los roles existentes

        Returns:
            list: lista de todos los roles existentes
            str: mensaje de error si no existen roles
        """
        try:
            roles = Rol.objects.all()
            if not roles:
                logger.warning("No se encontraron roles")
                return "No se encontraron roles"
            return roles
        except Exception as e:
            logger.error(f"Error al obtener los roles: {e}")
            return f"Error al obtener los roles: {e}"

    def get_rol_by_user(self, usuario: int) -> Rol or str:
        """
        Obtiene el rol de un usuario

        Args:
            usuario (int): id del usuario

        Returns:
            Rol: rol del usuario
            str: mensaje de error si no existe el rol
        """
        try:
            return Rol.objects.get(user=usuario)
        except Rol.DoesNotExist:
            logger.error(f"No se encontro el rol para el usuario '{usuario}'")
            return f"No se encontro el rol '{usuario}'"
        except Exception as e:
            logger.error(f"Ocurrio un error al obtener el rol '{usuario}': {str(e)}")
            return f"Ocurrio un error al obtener el rol '{usuario}'"

    def get_rol_by_user_rol(self, usuario: int, rol: str) -> Rol or str:
        """
        Obtiene el rol de un usuario segun su rol

        Args:
            usuario (int): id del usuario
            rol (str): rol del usuario

        Returns:
            Rol: rol del usuario
            str: mensaje de error si no existe el rol
        """
        try:
            return Rol.objects.filter(user=usuario, rol=rol).first()
        except Rol.DoesNotExist:
            logger.error(f"No se encontro el rol '{rol}' para el usuario '{usuario}'")
            return f"El rol de '{rol}' no existe para el usuario '{usuario}'"
        except Exception as e:
            logger.error(f"Ocurrio un error al obtener el rol '{rol}' para el usuario '{usuario}': {str(e)}")
            return f"Ocurrio un error al obtener el rol '{rol}' para el usuario '{usuario}'"

    def crear_rol(self, rol: str, user: int) -> Rol or str:
        """
        Crea un nuevo rol para un usuario

        Args:
            rol (str): rol del usuario
            user (int): id del usuario

        Returns:
            Rol: rol creado
            str: mensaje de error si el rol ya existe para el usuario
        """
        try:
            return Rol.objects.create(user=user, rol=rol)
        except IntegrityError as e:
            logger.error(f"Error al crear el rol: {e}")
            return "Este trabajador ya es un rol"
        except Exception as e:
            logger.error(f"Error al crear el rol: {e}")
            return f"Error al crear el rol."

    def actualizar_rol(self, id_rol: int, trabajador: int) -> Rol or str:
        """
        Actualiza el usuario de un rol

        Args:
            id_rol (int): id del rol
            trabajador (int): id del nuevo usuario

        Returns:
            Rol: rol actualizado
            str: mensaje de error si no existe el rol
        """
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

    def eliminar_rol(self, id_rol: int) -> bool or str:
        """
        Elimina un rol

        Args:
            id_rol (int): id del rol

        Returns:
            bool: True si se elimino el rol
            str: mensaje de error si no existe el rol
        """
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
