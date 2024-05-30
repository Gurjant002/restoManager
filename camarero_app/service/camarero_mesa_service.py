"""
Servicio para la gestion de relaciones entre camareros y mesas
"""

from django.db import IntegrityError
from camarero_app.models import Camarero_Mesa

import logging
logger = logging.getLogger(__name__)

class CamareroMesaService:
    """
    Clase para la gestion de relaciones entre camareros y mesas
    """
    def get_relaciones(self) -> list:
        """
        Devuelve todas las relaciones entre camareros y mesas.

        Devuelve:
            list: Lista de relaciones entre camareros y mesas.
                  Si no hay relaciones devuelve un mensaje de error.
        """
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

    def get_relacion_by_id(self, id_relacion: int) -> object:
        """
        Devuelve la relacion entre camarero y mesa segun su id.

        Args:
            id_relacion (int): El id de la relacion.

        Devuelve:
            object: La relacion segun su id.
                    Si no se encuentra la relacion devuelve un mensaje de error.
        """
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

    def get_relacion_by_rol(self, rol: str) -> list:
        """
        Devuelve las relaciones entre camarero y mesa segun su rol.

        Args:
            rol (str): El rol del camarero.

        Devuelve:
            list: Lista de relaciones entre camarero y mesa segun su rol.
                  Si no se encuentra la relacion devuelve un mensaje de error.
        """
        try:
            relacion = Camarero_Mesa.objects.filter(rol=rol)
            return relacion
        except Camarero_Mesa.DoesNotExist:
            logger.error(f"No se encontro la relacion '{rol}'")
            return f"No se encontro la relacion '{rol}'"
        except Exception as e:
            logger.error(f'Ocurrio un error inesperado. {e}')
            return 'Ocurrio un error inesperado.'

    def crear_relacion(self, numero_mesa: int, rol: str, ubicacion: str) -> str:
        """
        Crea una relacion entre camarero y mesa.

        Args:
            numero_mesa (int): El numero de la mesa.
            rol (str): El rol del camarero.
            ubicacion (str): La ubicacion de la mesa.

        Devuelve:
            str: Si hay algun error devuelve un mensaje de error.
        """
        if not numero_mesa or not rol or not ubicacion:
            logger.error(f"Ha habido un problema al recibir los parametros: {numero_mesa}, {rol}, {ubicacion}")
            return 'Error al obtener parametros: Pongase en contacto con el administrador.'
        try:
            Camarero_Mesa.objects.create(numero_mesa=numero_mesa, rol=rol, ubicacion=ubicacion)
        except Exception as e:
            logger.error(f'Ocurrio un error inesperado. {e}')
            return 'Ocurrio un error inesperado.'
