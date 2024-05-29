from django.http import HttpRequest
from cocina_app.service.servicio_cocina_service import ServicioCocinaService
from restoManager_app.service.trabajadores.rol_service import RolService
import logging

from django.utils import timezone
#
utc_dt = timezone.now()
logger = logging.getLogger(__name__)

class ServicioCocinaController:
  def __init__(self, request: HttpRequest = None):
    self.servicioCocina = ServicioCocinaService()
    self.rolService = RolService()
    self.request = request
    self.error = None
    self.listarMesa = None
    self.platos = None

  def peticiones(self, req: HttpRequest):
    try:
      if 'cambiar-estado' in req.POST:
        id = int(req.POST['cambiar-estado'].split('-')[0])
        estado = req.POST['cambiar-estado'].split('-')[1]
        self.error = self.cambiar_estado_servicio(id, estado)
      if 'listar_mesa' in req.GET or 'listar_mesa' in req.POST:
        id_mesa = int(req.GET['listar_mesa'])
        self.listarMesa = id_mesa
        self.platos = self.get_agrupaciones_by_camarero_mesa_id(id_mesa)
        
      return self.respuesta()
    except Exception as e:
      return self.respuesta(error=f'Error en peticiones: {e}')

  def get_servicio_cocina_by_id(self, id: int):
    return self.servicioCocina.get_servicio_cocina_by_id(id)
  def get_servicio_by_camarero(self, camarero):
    return self.servicioCocina.get_servicio_by_camarero(camarero)
    
  def get_servicio_by_mesa(self, mesa):
    return self.servicioCocina.get_servicio_by_mesa(mesa)
      
  def get_servicio_by_hora(self, hora: timezone):
    return self.servicioCocina.get_servicio_by_hora(hora)
  def crear_servicio(self, mesa, camarero, plato, servido: bool = None , hora: timezone = utc_dt):
    return self.servicioCocina.crear_servicio(mesa, camarero, plato, servido, hora)
  
  def crear_actualizar_servicio(self, id: int, mesa_camarero, plato, servido: bool = None , date: timezone = utc_dt):
    return self.servicioCocina.crear_actualizar_servicio(id, plato, servido, mesa_camarero, date)
  
  def get_servicio_mesa_cantidad_pedidos(self):
    return self.servicioCocina.get_servicio_mesa_cantidad_pedidos()

  def get_agrupaciones_by_camarero_mesa_id(self, id_camarero_mesa: int):
    pedidos =  self.servicioCocina.get_agrupaciones_by_camarero_mesa(id_camarero_mesa = id_camarero_mesa)
    return pedidos

  def cambiar_estado_servicio(self, id: int, estado: bool):
    return self.servicioCocina.cambiar_estado(id, estado)

  def check_isinstance(self, element_to_check):
    if isinstance(element_to_check, str):
        self.error = element_to_check
        element_to_check = False
    return element_to_check

  def respuesta(self, error: str = None):
    usuario = self.request.user
    mesas = self.get_servicio_mesa_cantidad_pedidos()
    
    cocinero = self.rolService.get_rol_by_user_rol(usuario, 'Cocinero')
    if isinstance(cocinero, str) or cocinero is None:
      cocinero = self.rolService.get_rol_by_user_rol(usuario, 'Administrador')
    
    if self.error is None or self.error == '':
      mesas = self.check_isinstance(mesas)
    if self.error is None or self.error == '':
      self.platos = self.check_isinstance(self.platos)
    if self.error is None or self.error == '':
      cocinero = self.check_isinstance(cocinero)
    
    diccionario = {
        'error': self.error,
        'mesas': mesas,
        'platos': self.platos,
        'es_cocinero': cocinero,
        'listar_mesa': self.listarMesa
    }
    return diccionario