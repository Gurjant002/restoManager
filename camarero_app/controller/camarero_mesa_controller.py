from ..service.camarero_mesa_service import CamareroMesaService
import logging

logger = logging.getLogger(__name__)

class CamareroMesaController:
    def __init__(self) -> None:
        self.camarero_mesa_service = CamareroMesaService()

    def get_relaciones(self):
        return self.camarero_mesa_service.get_relaciones()

    def get_relacion_by_id(self, id_relacion: int):
        return self.camarero_mesa_service.get_relacion_by_id(id_relacion)

    def get_relacion_by_camarero(self, id_camarero: int):
        return self.camarero_mesa_service.get_relacion_by_camarero(id_camarero)

    def crear_mesa(self, numero_mesa: int, camarero, ubicacion):
        return self.camarero_mesa_service.crear_relacion(numero_mesa, camarero, ubicacion)