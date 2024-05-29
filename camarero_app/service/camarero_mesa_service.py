from django.db import IntegrityError
from camarero_app.models import Camarero_Mesa

import logging
logger = logging.getLogger(__name__)

class CamareroMesaService:
    def get_relaciones(self):
        try:
            relaciones = Camarero_Mesa.objects.all()
            if not relaciones:
                logger.error('No se han encontrado ninguna mesa asignada a ningun camarero.')
                return 'No se han encontrado ninguna mesa asignada a ningun camarero. Intenta crear una mesa.'
            return relaciones
        except (Camarero_Mesa.DoesNotExist, IntegrityError, ValueError) as e:
            logger.error(f'Ocurrio un error inesperado. {e}')
            return 'Ocurrio un error inesperado.'
        except Exception as e:
            logger.error(f'Ocurrio un error desconocido. {e}')
            return 'Ocurrio un error desconocido.'

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

    def get_relacion_by_rol(self, rol):
        try:
            relacion = Camarero_Mesa.objects.filter(rol=rol)
            return relacion
        except Camarero_Mesa.DoesNotExist:
            logger.error(f"No se encontro la relacion '{rol}'")
            return f"No se encontro la relacion '{rol}'"
        except Exception as e:
            logger.error(f'Ocurrio un error inesperado. {e}')
            return 'Ocurrio un error inesperado.'

    def crear_relacion(self, numero_mesa: int, rol, ubicacion):
        if not numero_mesa or not rol or not ubicacion:
            logger.error(f"Ha habido un problema al recibir los parametros: {numero_mesa}, {rol}, {ubicacion}")
            return 'Error all obtener parametros: Ponga se en contacto con el administrador.'
        
        try:
            Camarero_Mesa.objects.create(numero_mesa=numero_mesa, rol=rol, ubicacion=ubicacion)
        except Exception as e:
            logger.error(f'Ocurrio un error inesperado. {e}')
            return 'Ocurrio un error inesperado.'