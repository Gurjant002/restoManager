from camarero_app.models import Camarero_Mesa
import logging
logger = logging.getLogger(__name__)

class CamareroMesaService:
    def get_relaciones(self):
        try:
            relaciones = Camarero_Mesa.objects.all()
            if not relaciones:
                return "No se encontro ninguna relacion"
            
            return relaciones
        except Camarero_Mesa.DoesNotExist:
            logger.error("No se encontro ninguna relacion")
            return None
        except Exception as e:
            logger.error(f'Ocurrio un error inesperado. {e}')
            return 'Ocurrio un error inesperado.'

    def get_relacion_by_id(self, id_relacion: int):
        try:
            relacion = Camarero_Mesa.objects.filter(id=id_relacion).first()
            if not relacion:
                logger.error(f"No se encontro la relacion '{id_relacion}'")
                return f"No se encontro la relacion '{id_relacion}'"
            return relacion
        except Camarero_Mesa.DoesNotExist:
            logger.error(f"No se encontro la relacion '{id_relacion}'")
            return f"No se encontro la relacion '{id_relacion}'"
        except Exception as e:
            logger.error(f'Ocurrio un error inesperado. {e}')
            return 'Ocurrio un error inesperado.'

    def get_relacion_by_camarero(self, camarero):
        try:
            relacion = Camarero_Mesa.objects.filter(camarero=camarero)
            return relacion
        except Camarero_Mesa.DoesNotExist:
            logger.error(f"No se encontro la relacion '{camarero}'")
            return f"No se encontro la relacion '{camarero}'"
        except Exception as e:
            logger.error(f'Ocurrio un error inesperado. {e}')
            return 'Ocurrio un error inesperado.'

    def crear_relacion(self, numero_mesa: int, camarero, ubicacion):
        try:
            Camarero_Mesa.objects.create(numero_mesa=numero_mesa, camarero=camarero, ubicacion=ubicacion)
        except Exception as e:
            logger.error(f'Ocurrio un error inesperado. {e}')
            return 'Ocurrio un error inesperado.'