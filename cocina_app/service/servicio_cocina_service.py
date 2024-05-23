from django.db import IntegrityError
from cocina_app.models import Servicio_Cocina
import logging
import datetime

logger = logging.getLogger(__name__)
class ServicioCocinaService:
    def get_servicio_cocina_by_id(self, id: int):
        try:
            servicio = Servicio_Cocina.objects.get(id=id)
            if not servicio:
                logger.warning('No se encontro ningun servicio de cocina')
                return 'No se encontro ningun servicio de cocina'
            return servicio
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.get_servicio_cocina_by_id: {e}')
            return 'Ha ocurrido un error inesperado.'

    def get_servicio_by_camarero(self, camarero):
        try:
            servicio = Servicio_Cocina.objects.get(camarero=camarero)
            if not servicio:
                logger.warning(f'No se encontro ningun servicio de cocina de este {camarero}')
                return 'No se encontro ningun servicio de cocina'
            return servicio
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.get_servicio_by_camarero: {e}')
            return 'Ha ocurrido un error inesperado.'
    
    def get_servicio_by_mesa(self, mesa):
        try:
            servicio = Servicio_Cocina.objects.get(mesa=mesa)
            if not servicio:
                logger.warning(f'No se encontro ningun servicio de cocina de esta {mesa}')
                return 'No se encontro ningun servicio de cocina'
            return servicio
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.get_servicio_by_mesa: {e}')
            return 'Ha ocurrido un error inesperado.'
    
    def get_servicio_by_hora(self, hora):
        try:
            servicio = Servicio_Cocina.objects.get(hora=hora)
            if not servicio:
                logger.warning(f'No se encontro ningun servicio de cocina de esta {hora}')
                return 'No se encontro ningun servicio de cocina'
            return servicio
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.get_servicio_by_hora: {e}')
            return 'Ha ocurrido un error inesperado.'

    def crear_servicio(
        self,
        mesa_camarero= None,
        plato = None,
        servido: bool = None ,
        date: datetime = datetime.datetime.now()
        ):
        try:
            return Servicio_Cocina.objects.create(
            plato=plato,
            servido=servido,
            camarero_mesa=mesa_camarero,
            hora_dia=date
            )
        except IntegrityError:
            logger.error(f'No se puedo crear el servicio de cocina porque ya existe')
            return f'No se puedo crear el servicio de cocina porque ya existe'
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.crear_servicio: {e}')
            return 'Ha ocurrido un error inesperado.'
        
    def crear_actualizar_servicio(
        self,
        id: int,
        plato,
        servido: bool = None ,
        mesa_camarero = None,
        date: datetime = datetime.datetime.now()
        ):
        try:
            servicio: Servicio_Cocina = Servicio_Cocina.objects.get(id=id)
            if not servicio:
                logger.warning(f'No se encontro ningun servicio de cocina con este {id}')
                return 'No se encontro ningun servicio de cocina'
            servicio.camarero_mesa = mesa_camarero
            servicio.plato = plato
            servicio.servido = servido
            servicio.hora_dia = date
            servicio.save()
            return 'Servicio de cocina actualizado'
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.crear_actualizar_servicio: {e}')
            return 'Ha ocurrido un error inesperado.'