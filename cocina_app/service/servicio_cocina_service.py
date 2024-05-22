from django.db import IntegrityError
from cocina_app.models import Servicio_Cocina
import logging
import datetime

logger = logging.getLogger(__name__)
class ServicioCocinaController:
    def get_servicio_cocina_by_id(self, id):
        try:
            servicio = Servicio_Cocina.objects.get(id=id)
            if not servicio:
                logger.warning('No se encontro ningun servicio de cocina')
                return 'No se encontro ningun servicio de cocina'
            return servicio
        except Exception as e:
            logger.error(f'Error en ServicioCocinaController.get_servicio_cocina_by_id: {e}')
            return 'Ha ocurrido un error inesperado.'

    def get_servicio_by_camarero(self, camarero):
        try:
            servicio = Servicio_Cocina.objects.get(camarero=camarero)
            if not servicio:
                logger.warning(f'No se encontro ningun servicio de cocina de este {camarero}')
                return 'No se encontro ningun servicio de cocina'
            return servicio
        except Exception as e:
            logger.error(f'Error en ServicioCocinaController.get_servicio_by_camarero: {e}')
            return 'Ha ocurrido un error inesperado.'
    
    def get_servicio_by_mesa(self, mesa):
        try:
            servicio = Servicio_Cocina.objects.get(mesa=mesa)
            if not servicio:
                logger.warning(f'No se encontro ningun servicio de cocina de esta {mesa}')
                return 'No se encontro ningun servicio de cocina'
            return servicio
        except Exception as e:
            logger.error(f'Error en ServicioCocinaController.get_servicio_by_mesa: {e}')
            return 'Ha ocurrido un error inesperado.'
    
    def get_servicio_by_hora(self, hora):
        try:
            servicio = Servicio_Cocina.objects.get(hora=hora)
            if not servicio:
                logger.warning(f'No se encontro ningun servicio de cocina de esta {hora}')
                return 'No se encontro ningun servicio de cocina'
            return servicio
        except Exception as e:
            logger.error(f'Error en ServicioCocinaController.get_servicio_by_hora: {e}')
            return 'Ha ocurrido un error inesperado.'

    def crear_servicio(self, mesa, camarero, plato, servido: bool = False , hora: datetime = datetime.datetime.now()):
        try:
            Servicio_Cocina.objects.create(mesa=mesa, camarero=camarero, plato=plato, servido=servido, hora=hora)
        except IntegrityError:
            logger.error(f'No se puedo crear el servicio de cocina porque ya existe')
            return f'No se puedo crear el servicio de cocina porque ya existe'
        except Exception as e:
            logger.error(f'Error en ServicioCocinaController.crear_servicio: {e}')
            return 'Ha ocurrido un error inesperado.'