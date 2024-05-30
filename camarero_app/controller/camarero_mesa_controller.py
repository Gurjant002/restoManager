from ..service.camarero_mesa_service import CamareroMesaService
import logging

logger = logging.getLogger(__name__)


class CamareroMesaController:
    """
    Controlador para gestionar las relaciones entre camarero y mesa.
    """
    def __init__(self) -> None:
        """
        Inicializa el controlador.
        """
        self.camarero_mesa_service = CamareroMesaService()

    def get_relaciones(self) -> list:
        """
        Devuelve todas las relaciones entre camarero y mesa.

        Returns:
            list: Lista de relaciones.
        """
        return self.camarero_mesa_service.get_relaciones()

    def get_relacion_by_id(self, id_relacion: int) -> object:
        """
        Devuelve la relacion entre camarero y mesa segun su id.

        Args:
            id_relacion (int): El id de la relacion.

        Returns:
            object: La relacion segun su id.
                    Si no se encuentra la relacion devuelve un mensaje de error.
        """
        return self.camarero_mesa_service.get_relacion_by_id(id_relacion)

    def get_relacion_by_camarero(self, id_camarero: int) -> list:
        """
        Devuelve todas las relaciones entre camarero y mesa segun un id de camarero.

        Args:
            id_camarero (int): El id del camarero.

        Returns:
            list: Lista de relaciones segun el id del camarero.
        """
        return self.camarero_mesa_service.get_relacion_by_rol(id_camarero)

    def crear_mesa(self, numero_mesa: int, camarero, ubicacion) -> str:
        """
        Crea una relacion entre camarero y mesa.

        Args:
            numero_mesa (int): El numero de la mesa.
            camarero (str): El rol del camarero.
            ubicacion (str): La ubicacion de la mesa.

        Returns:
            str: Si hay algun error devuelve un mensaje de error.
        """
        return self.camarero_mesa_service.crear_relacion(numero_mesa, camarero, ubicacion)
