from django.db import IntegrityError
from restoManager_app.models import Ubicacion
import logging

logger = logging.getLogger(__name__)

class UbicacionService:
    """
    Clase que abstrae la logica de negocio para la gestion de ubicaciones.
    """
    def get_ubicaciones(self) -> str | Ubicacion:
        """
        Retorna todas las ubicaciones registradas.

        Returns:
            str | Ubicacion: Lista de ubicaciones o mensaje de error.
        """
        try:
            ubicacion = Ubicacion.objects.all()
            if not ubicacion:
                logger.warning("No se encontro ninguna ubicacion")
                return "No se encontro ninguna ubicacion"
            
            return ubicacion
        except Ubicacion.DoesNotExist:
            logger.error("No se encontro ninguna ubicacion")
            return None

    def get_ubicacion_by_id(self, id_ubicacion: int) -> str | Ubicacion:
        """
        Retorna la ubicacion con el id ingresado.

        Args:
            id_ubicacion (int): ID de la ubicacion.

        Returns:
            str | Ubicacion: La ubicacion o mensaje de error.
        """
        try:
            ubicacion = Ubicacion.objects.filter(id=id_ubicacion).first()
            return ubicacion
        except Ubicacion.DoesNotExist:
            logger.error(f"No se encontro la ubicacion '{id_ubicacion}'")
            return f"No se encontro la ubicacion '{id_ubicacion}'"

    def get_ubicacion_by_lugar(self, lugar: str) -> str | Ubicacion:
        """
        Retorna la ubicacion con el lugar ingresado.

        Args:
            lugar (str): Nombre de la ubicacion.

        Returns:
            str | Ubicacion: La ubicacion o mensaje de error.
        """
        try:
            ubicacion = Ubicacion.objects.get(lugar=lugar)
            return ubicacion
        except Ubicacion.DoesNotExist:
            logger.error(f"No se encontro la ubicacion '{lugar}'")
            return f"No se encontro la ubicacion '{lugar}'"

    def crear_ubicacion(self, ubicacion: str) -> str | Ubicacion:
        """
        Crea una nueva ubicacion con el nombre ingresado.

        Args:
            ubicacion (str): Nombre de la ubicacion.

        Returns:
            str | Ubicacion: La ubicacion creada o mensaje de error.
        """
        try:
            Ubicacion.objects.create(lugar=ubicacion)
        except IntegrityError:
            logger.error(f"No se puedo crear la ubicacion '{ubicacion}' porque ya existe")
            return f"No se puedo crear la ubicacion '{ubicacion}' porque ya existe"

    def eliminar_ubicacion(self, idUbicacion: int) -> str | None:
        """
        Elimina la ubicacion con el id ingresado.

        Args:
            idUbicacion (int): ID de la ubicacion.

        Returns:
            str | None: Mensaje de error si no se encuentra la ubicacion o None si se elimina.
        """
        try:
            Ubicacion.objects.filter(id=idUbicacion).delete()
        except Ubicacion.DoesNotExist:
            logger.error(f"No se encontro la ubicacion '{idUbicacion}' para eliminar")
            return f"No se encontro la ubicacion '{idUbicacion}' para eliminar"

    def actualizar_ubicacion(self, id_ubicacion: int, lugar: str):
        """
        Actualiza la ubicacion con el id ingresado con el nuevo nombre.

        Args:
            id_ubicacion (int): ID de la ubicacion.
            lugar (str): Nuevo nombre de la ubicacion.

        Returns:
            str | None: Mensaje de error si no se encuentra la ubicacion o None si se actualiza.
        """
        try:
            ubicacion = Ubicacion.objects.get(id=id_ubicacion)
            ubicacion.lugar = lugar
            ubicacion.save()
        except Ubicacion.DoesNotExist:
            logger.error(f"No se encontro la ubicacion '{id_ubicacion}' para actualizar")
            return f"No se encontro la ubicacion '{id_ubicacion}' para actualizar"
        except IntegrityError:
            logger.error(f"No se puedo actualizar la ubicacion '{lugar}' porque esta en uso")
            return f"No se puedo actualizar la ubicacion '{lugar}' porque esta en uso"
        except Exception as e:
            logger.error(f"Ocurrio un error al actualizar la ubicacion '{lugar}': {str(e)}")
            return f"Ocurrio un error al actualizar la ubicacion '{lugar}': {str(e)}"

