from django.http import HttpRequest
from cocina_app.service.servicio_cocina_service import ServicioCocinaService
import logging

from datetime import datetime
from django.utils import timezone as jango
#
utc_dt = jango.now()
logger = logging.getLogger(__name__)
class ServicioCocinaController:
  def __init__(self):
    self.servicioCocina = ServicioCocinaService()
    
  def peticiones(self, req: HttpRequest):
    pedidos = None
    if 'listar_mesa' in req.GET:
      id_mesa = int(req.GET['listar_mesa'])
      pedidos = self.get_agrupaciones_by_camarero_mesa_id(id_mesa)
      return self.respuesta(platos = pedidos)
    elif 'cambiar-estado' in req.POST:
      id = int(req.POST['cambiar-estado'].split('-')[0])
      estado = req.POST['cambiar-estado'].split('-')[1]
      print('cambiar-estado', id)
      error = self.cambiar_estado_servicio(id, estado)
      return self.respuesta(error=error)
    return self.respuesta()

  def get_servicio_cocina_by_id(self, id: int):
    return self.servicioCocina.get_servicio_cocina_by_id(id)
  def get_servicio_by_camarero(self, camarero):
    return self.servicioCocina.get_servicio_by_camarero(camarero)
    
  def get_servicio_by_mesa(self, mesa):
    return self.servicioCocina.get_servicio_by_mesa(mesa)
      
  def get_servicio_by_hora(self, hora: datetime):
    return self.servicioCocina.get_servicio_by_hora(hora)
  def crear_servicio(self, mesa, camarero, plato, servido: bool = None , hora: datetime = utc_dt):
    return self.servicioCocina.crear_servicio(mesa, camarero, plato, servido, hora)
  
  def crear_actualizar_servicio(self, id: int, mesa_camarero, plato, servido: bool = None , date: datetime = utc_dt):
    return self.servicioCocina.crear_actualizar_servicio(id, plato, servido, mesa_camarero, date)
  
  def get_servicio_mesa_cantidad_pedidos(self):
    return self.servicioCocina.get_servicio_mesa_cantidad_pedidos()

  def get_agrupaciones_by_camarero_mesa_id(self, id_camarero_mesa: int):
    pedidos =  self.servicioCocina.get_agrupaciones_by_camarero_mesa(id_camarero_mesa = id_camarero_mesa)
    return pedidos

  def cambiar_estado_servicio(self, id: int, estado: bool):
    return self.servicioCocina.cambiar_estado(id, estado)

  def chech_isinstance(self, element_to_check):
    error = ''
    if isinstance(element_to_check, str):
        error = element_to_check
        element_to_check = False
    return element_to_check, error

  def respuesta(self, error: str = None, platos = None):
    mesas = self.get_servicio_mesa_cantidad_pedidos()
    mesas, error = self.chech_isinstance(mesas)
    
    platos, error = self.chech_isinstance(platos)
    
    diccionario = {
        'error': error,
        'mesas': mesas,
        'platos': platos
    }
    return diccionario