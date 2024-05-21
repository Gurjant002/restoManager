from django.db import IntegrityError
from ...models import Camarero
import logging

logger = logging.getLogger(__name__)


class CamareroService:

    def get_camareros(self):
        try:
            camareros = Camarero.objects.all()
            if not camareros:
                logger.warning("No se encontraron camareros")
                return "No se encontraron camareros"
            return camareros
        except Exception as e:
            logger.error(f"Error al obtener los camareros: {e}")
            return f"Error al obtener los camareros: {e}"

    def get_camarero_by_user(self, usuario: int):
        try:
            return Camarero.objects.get(user=usuario)
        except Camarero.DoesNotExist:
            logger.error(f"No se encontro el camarero '{usuario}'")
            return f"No se encontro el camarero '{usuario}'"
        except Exception as e:
            logger.error(f"Ocurrio un error al obtener el camarero '{usuario}': {str(e)}")
            return f"Ocurrio un error al obtener el camarero '{usuario}'"

    def crear_camarero(self, trabajador):
        try:
            return Camarero.objects.create(user=trabajador)
        except IntegrityError as e:
            logger.error(f"Error al crear el camarero: {e}")
            return "Este trabajador ya es un camarero"
        except Exception as e:
            logger.error(f"Error al crear el camarero: {e}")
            return f"Error al crear el camarero."

    def actualizar_camarero(self, id_camarero: int, trabajador):
        try:
            camarero = Camarero.objects.get(id=id_camarero)
            camarero.id_user = trabajador
            camarero.save()
            return camarero
        except Camarero.DoesNotExist:
            logger.error(f"No se encontro el camarero '{id_camarero}' para actualizar")
            return f"No se encontro el camarero '{id_camarero}' para actualizar"
        except Exception as e:
            logger.error(f"Ocurrio un error al actualizar el camarero '{id_camarero}': {str(e)}")
            return f"Ocurrio un error al actualizar el camarero '{id_camarero}': {str(e)}"

    def eliminar_camarero(self, id_camarero: int):
        try:
            camarero = Camarero.objects.get(id=id_camarero)
            camarero.delete()
            return True
        except Camarero.DoesNotExist:
            logger.error(f"No se encontro el camarero '{id_camarero}' para eliminar")
            return f"No se encontro el camarero '{id_camarero}' para eliminar"
        except Exception as e:
            logger.error(f"Ocurrio un error al eliminar el camarero '{id_camarero}': {str(e)}")
            return f"Ocurrio un error al eliminar el camarero '{id_camarero}': {str(e)}"