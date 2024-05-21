from django.db import IntegrityError
from restoManager_app.models import Ubicacion
import logging
logger = logging.getLogger(__name__)

class UbicacionService:
    def get_ubicaciones(self) -> str | Ubicacion:
        try:
            ubicacion = Ubicacion.objects.all()
            if not ubicacion:
                return "No se encontro ninguna ubicacion"
            
            return ubicacion
        except Ubicacion.DoesNotExist:
            logger.error("No se encontro ninguna ubicacion")
            return None

    def get_ubicacion_by_id(self, id_ubicacion: int) -> str | Ubicacion:
        try:
            ubicacion = Ubicacion.objects.filter(id=id_ubicacion).first()
            return ubicacion
        except Ubicacion.DoesNotExist:
            logger.error(f"No se encontro la ubicacion '{id_ubicacion}'")
            return f"No se encontro la ubicacion '{id_ubicacion}'"

    def get_ubicacion_by_lugar(self, lugar: str) -> str | Ubicacion:
        try:
            ubicacion = Ubicacion.objects.get(lugar=lugar)
            return ubicacion
        except Ubicacion.DoesNotExist:
            logger.error(f"No se encontro la ubicacion '{lugar}'")
            return f"No se encontro la ubicacion '{lugar}'"

    def crear_ubicacion(self, ubicacion: str) -> str | Ubicacion:
        try:
            Ubicacion.objects.create(lugar=ubicacion)
        except IntegrityError:
            logger.error(f"No se puedo crear la ubicacion '{ubicacion}' porque ya existe")
            return f"No se puedo crear la ubicacion '{ubicacion}' porque ya existe"

    def eliminar_ubicacion(self, idUbicacion: int) -> str | None:
        try:
            Ubicacion.objects.filter(id=idUbicacion).delete()
        except Ubicacion.DoesNotExist:
            logger.error(f"No se encontro la ubicacion '{idUbicacion}' para eliminar")
            return f"No se encontro la ubicacion '{idUbicacion}' para eliminar"

    def actualizar_ubicacion(self, id_ubicacion: int, lugar: str):
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
