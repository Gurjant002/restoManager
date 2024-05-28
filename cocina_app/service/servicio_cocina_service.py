from django.db import IntegrityError
from django.db.models import Count, Max, Min
from cocina_app.models import Servicio_Cocina
from restoManager_app.models import Plato
from camarero_app.models import Camarero_Mesa
import logging
from datetime import datetime

utc_dt = datetime.utcnow()

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

    def crear_servicio(self, mesa_camarero= None, plato = None, servido: bool = None , date: datetime = utc_dt):
        try:
            return Servicio_Cocina.objects.create( plato=plato, servido=servido, camarero_mesa=mesa_camarero, hora_dia=date)
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
        date: datetime = utc_dt
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

    def get_agrupaciones(self):
        try:
            agrupaciones = list(Servicio_Cocina.objects.values('plato', 'servido', 'camarero_mesa')
                                .annotate(total=Count('id'), tiempo=Max('hora_dia')))
            for agrupacion in agrupaciones:
                agrupacion['plato'] = Plato.objects.get(pk=agrupacion['plato'])
                agrupacion['camarero_mesa'] = Camarero_Mesa.objects.get(pk=agrupacion['camarero_mesa'])
                # agrupacion['camarero_mesa'] = camarero_mesa
            return agrupaciones
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.get_agrupaciones: {e}')
            return 'Ha ocurrido un error inesperado.'

    def get_agrupaciones_by_camarero_mesa(self, id_camarero_mesa: int):
        try:
            servicio_Cocina = list(Servicio_Cocina.objects.filter(camarero_mesa=id_camarero_mesa).values('plato', 'servido', 'id').annotate(total=Count('id'), tiempo=Max('hora_dia')))
            agrupacion = []
            for agrupacion_db in servicio_Cocina:
                agrupacion_db['plato'] = Plato.objects.get(pk=agrupacion_db['plato'])
                agrupacion.append(agrupacion_db)

            camarero_mesa = Camarero_Mesa.objects.get(pk=id_camarero_mesa)
            agrupacion = {
                'camarero_mesa': {
                    'numero_mesa': camarero_mesa.numero_mesa,
                    'ubicacion__lugar': camarero_mesa.ubicacion.lugar
                },
                'platos': agrupacion,
                'id': id_camarero_mesa
            }
            return agrupacion
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.get_agrupaciones_by_camarero_mesa: {e}')
            return 'Ha ocurrido un error inesperado.'

    def cambiar_estado(self, id: int, servido: bool):
        try:
            servicio: Servicio_Cocina = Servicio_Cocina.objects.filter(id=id).first()
            if not servicio:
                logger.warning(f'No se encontro ningun servicio de cocina con este {id}')
                return 'No se encontro ningun servicio de cocina'
            servicio.servido = servido
            servicio.save()
            return 'Servicio de cocina actualizado'
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.cambiar_estado: {e}')
            return 'Ha ocurrido un error inesperado.'

    def get_servicio_mesa_cantidad_pedidos(self):
        try:
            agrupaciones = Servicio_Cocina.objects.values('camarero_mesa__numero_mesa', 'camarero_mesa__ubicacion__lugar', 'camarero_mesa__id').annotate(total=Count('plato'), tiempo=Min('hora_dia')).order_by('hora_dia')
            pedidos_total_mesa = []
            for agrupacion in agrupaciones:
                pedidos_total_mesa.append({
                    'mesa_id': agrupacion['camarero_mesa__id'],
                    'mesa': agrupacion['camarero_mesa__numero_mesa'],
                    'mesa_ubicacion': agrupacion['camarero_mesa__ubicacion__lugar'],
                    'pedidosTotal': agrupacion['total'],
                    'tiempo': agrupacion['tiempo']
                })
            return pedidos_total_mesa
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.get_servicio_mesa_cantidad_pedidos: {e}')
            return 'Ha ocurrido un error inesperado.'