import logging
from django.utils import timezone
from django.db import IntegrityError, models
from django.db.models import Count, Max, Min, Sum

from camarero_app.models import Camarero_Mesa
from restoManager_app.models import Plato
from cocina_app.models import Servicio_Cocina

utc_dt = timezone.now()

logger = logging.getLogger(__name__)
class ServicioCocinaService:
    """
    Esta clase encapsula la lógica de negocio para el modelo ServicioCocina.
    Proporciona métodos para obtener un servicio por id, por camarero y por mesa.
    """

    def get_servicio_cocina_by_id(self, id: int):
        """
        Obtiene un servicio por su id.

        Args:
            id (int): El id del servicio.

        Returns:
            ServicioCocina: El objeto de servicio.

        Raises:
            Exception: Si el servicio no se encuentra o ocurre un error.
        """
        try:
            servicio = Servicio_Cocina.objects.get(id=id)
            if not servicio:
                logger.warning('No se encontró ningún servicio de cocina')
                return 'No se encontró ningún servicio de cocina'
            return servicio
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.get_servicio_cocina_by_id: {e}')
            return 'Ocurrió un error inesperado.'

    def get_servicio_by_camarero(self, camarero):
        """
        Obtiene un servicio por camarero.

        Args:
            camarero: El camarero asociado al servicio.

        Returns:
            ServicioCocina: El objeto de servicio.

        Raises:
            Exception: Si el servicio no se encuentra o ocurre un error.
        """
        try:
            servicio = Servicio_Cocina.objects.get(camarero=camarero)
            if not servicio:
                logger.warning(f'No se encontró ningún servicio de cocina de este {camarero}')
                return 'No se encontró ningún servicio de cocina'
            return servicio
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.get_servicio_by_camarero: {e}')
            return 'Ocurrió un error inesperado.'
    
    def get_servicio_by_mesa(self, mesa):
        """
        Obtiene un servicio por mesa.

        Args:
            mesa: La mesa asociada al servicio.

        Returns:
            QuerySet: El QuerySet que contiene los objetos de servicio.

        Raises:
            Exception: Si el servicio no se encuentra o ocurre un error.
        """
        try:
            servicio = Servicio_Cocina.objects.filter(camarero_mesa=mesa)
            if not servicio:
                logger.warning(f'No se encontró ningún servicio de cocina de esta {mesa}')
                return 'No se encontró ningún servicio de cocina'
            return servicio
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.get_servicio_by_mesa: {e}')
            return 'Ocurrió un error inesperado.'
    
    def get_servicio_by_hora(self, hora):
        """
        Obtiene un servicio por hora.

        Args:
            hora: La hora asociada al servicio.

        Returns:
            ServicioCocina: El objeto de servicio.

        Raises:
            Exception: Si el servicio no se encuentra o ocurre un error.
        """
        try:
            servicio = Servicio_Cocina.objects.get(hora=hora)
            if not servicio:
                logger.warning(f'No se encontró ningún servicio de cocina de esta {hora}')
                return 'No se encontró ningún servicio de cocina'
            return servicio
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.get_servicio_by_hora: {e}')
            return 'Ocurrió un error inesperado.'
    
    def crear_servicio(self, mesa_camarero= None, plato = None, servido: bool = None , date: timezone = utc_dt):
        """
        Crea un servicio.

        Args:
            mesa_camarero: El mesa_camarero asociado al servicio.
            plato: El plato asociado al servicio.
            servido: El servido asociado al servicio.
            date: La fecha asociada al servicio.

        Returns:
            ServicioCocina: El objeto de servicio creado.

        Raises:
            Exception: Si el servicio no puede ser creado o ocurre un error.
        """
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
        date: timezone = timezone.now()
        ):
        """
        Crea o actualiza un servicio de cocina.

        Args:
            id (int): El ID del servicio a actualizar.
            plato: El plato asociado al servicio.
            servido (bool, optional): El estado de servido del servicio.
            mesa_camarero: El mesero asociado al servicio.
            date (timezone, optional): La fecha y hora del servicio.

        Returns:
            str: El mensaje de éxito o de error.

        Raises:
            Exception: Si el servicio no se puede crear o actualizar o ocurre un error.
        """
        try:
            servicio: Servicio_Cocina = Servicio_Cocina.objects.get(id=id)
            if not servicio:
                logger.warning(f'No se encontró ningún servicio de cocina con este {id}')
                return 'No se encontró ningún servicio de cocina'
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
        """
        Obtiene todas las agrupaciones de servicios de cocina.

        Returns:
            list: Lista de agrupaciones de servicios de cocina.

        Raises:
            Exception: Si ocurre un error al obtener las agrupaciones.
        """
        try:
            agrupaciones = list(
                Servicio_Cocina.objects
                .values('plato', 'servido', 'camarero_mesa')
                .annotate(total=Count('id'), tiempo=Max('hora_dia'))
                )
            for agrupacion in agrupaciones:
                agrupacion['plato'] = Plato.objects.get(pk=agrupacion['plato'])
                agrupacion['camarero_mesa'] = Camarero_Mesa.objects.get(pk=agrupacion['camarero_mesa'])
                # agrupacion['camarero_mesa'] = camarero_mesa
            return agrupaciones
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.get_agrupaciones: {e}')
            return 'Ha ocurrido un error inesperado.'

    def get_agrupaciones_by_camarero_mesa(self, id_camarero_mesa: int):
        """
        Obtiene las agrupaciones de servicios de cocina por camarero de mesa.

        Args:
            id_camarero_mesa (int): El ID del camarero de mesa.

        Returns:
            dict: Diccionario de agrupaciones de servicios de cocina por camarero de mesa.

        Raises:
            Exception: Si ocurre un error al obtener las agrupaciones.
        """
        try:
            servicio_Cocina = list(Servicio_Cocina.objects.filter(camarero_mesa=id_camarero_mesa).values('plato', 'servido', 'id').annotate(total=Count('id'), tiempo=Max('hora_dia')))
            agrupacion = []
            for agrupacion_db in servicio_Cocina:
                if agrupacion_db['plato'] is not None:
                    plato = Plato.objects.get(pk=agrupacion_db['plato'])
                    agrupacion_db['plato'] = plato
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
        """
        Cambia el estado de servicio de cocina.

        Args:
            id (int): El ID del servicio de cocina.
            servido (bool): El estado del servicio de cocina.

        Returns:
            str: Mensaje de exito o error.

        Raises:
            Exception: Si ocurre un error al cambiar el estado.
        """
        try:
            if servido == 'Null':
                servido = None
            servicio: Servicio_Cocina = Servicio_Cocina.objects.filter(id=id).first()
            if not servicio:
                logger.warning(f'No se encontro ningun servicio de cocina con este {id}')
                return 'No se encontro ningun servicio de cocina'
            servicio.servido = servido
            servicio.save()
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.cambiar_estado: {e}')
            return 'Ha ocurrido un error inesperado.'

    def get_servicio_mesa_cantidad_pedidos(self):
        """
        Obtiene la agrupación de servicios de cocina por mesa con la cantidad de pedidos por plato.

        Returns:
            list: Lista de agrupaciones de servicios de cocina por mesa con la cantidad de pedidos por plato.

        Raises:
            Exception: Si ocurre un error al obtener las agrupaciones.
        """
        try:
            agrupacion_platos_mesa = list(
                Servicio_Cocina.objects
                .values('camarero_mesa', 'camarero_mesa__numero_mesa', 'camarero_mesa__ubicacion__lugar')
                .annotate(
                    pedidos_total_plato=Count('plato'),
                    hora_dia=Min('hora_dia')
                )
                .order_by('camarero_mesa__numero_mesa')
                )
            return agrupacion_platos_mesa
        except Exception as e:
            logger.error(f'Error en ServicioCocinaService.get_servicio_mesa_cantidad_pedidos: {e}')
            return 'Ha ocurrido un error inesperado.'

