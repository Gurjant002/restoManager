from cocina_app.service.servicio_cocina_service import ServicioCocinaService
import logging

from datetime import datetime
from django.utils import timezone as jango
#
utc_dt = jango.now()
logger = logging.getLogger(__name__)
class ServicioCocinaController:
  def get_servicio_cocina_by_id(self, id: int):
    return ServicioCocinaService.get_servicio_cocina_by_id(id)
  def get_servicio_by_camarero(self, camarero):
    return ServicioCocinaService.get_servicio_by_camarero(camarero)
    
  def get_servicio_by_mesa(self, mesa):
    return ServicioCocinaService.get_servicio_by_mesa(mesa)
      
  def get_servicio_by_hora(self, hora: datetime):
    return ServicioCocinaService.get_servicio_by_hora(hora)
  def crear_servicio(self, mesa, camarero, plato, servido: bool = None , hora: datetime = utc_dt):
    return ServicioCocinaService.crear_servicio(mesa, camarero, plato, servido, hora)
  
  def crear_actualizar_servicio(
    self,
    id: int,
    mesa_camarero,
    plato,
    servido: bool = None ,
    date: datetime = utc_dt
    ):
    return ServicioCocinaService.crear_actualizar_servicio(id, plato, servido, mesa_camarero, date)