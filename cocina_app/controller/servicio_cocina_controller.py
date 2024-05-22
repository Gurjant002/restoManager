from cocina_app.service.servicio_cocina_service import ServicioCocinaController
import logging
import datetime

logger = logging.getLogger(__name__)
class ServicioCocinaController:
  def get_servicio_cocina_by_id(self, id: int):
    return ServicioCocinaController.get_servicio_cocina_by_id(id)
  def get_servicio_by_camarero(self, camarero):
    return ServicioCocinaController.get_servicio_by_camarero(camarero)
    
  def get_servicio_by_mesa(self, mesa):
    return ServicioCocinaController.get_servicio_by_mesa(mesa)
      
  def get_servicio_by_hora(self, hora: datetime):
    return ServicioCocinaController.get_servicio_by_hora(hora)
  def crear_servicio(self, mesa, camarero, plato, servido: bool = None , hora: datetime = datetime.datetime.now()):
    return ServicioCocinaController.crear_servicio(mesa, camarero, plato, servido, hora)
  
  def crear_actualizar_servicio(
    self,
    id: int,
    mesa_camarero,
    plato,
    servido: bool = None ,
    date: datetime = datetime.datetime.now()
    ):
    return ServicioCocinaController.crear_actualizar_servicio(id, plato, servido, mesa_camarero, date)