import logging
from django.utils import timezone
from django.http import HttpRequest

from restoManager_app.service.trabajadores.rol_service import RolService
from cocina_app.service.servicio_cocina_service import ServicioCocinaService

utc_dt = timezone.now()
logger = logging.getLogger(__name__)

class ServicioCocinaController:
  """
  Controlador para ServicioCocina. Proporciona métodos para realizar
  operaciones sobre la entidad ServicioCocina.
  """
  def __init__(self, request: HttpRequest = None):
    """
    Constructor de la clase ServicioCocinaController.

    Args:
        request (HttpRequest, opcional): La petición HTTP asociada a la
            instancia.
    """
    self.servicioCocina = ServicioCocinaService()
    self.rolService = RolService()
    self.request = request
    self.error = None
    self.listarMesa = None
    self.platos = None

  def peticiones(self, req: HttpRequest):
    """
    Método que gestiona las peticiones realizadas por el usuario.

    Args:
        req (HttpRequest): La petición HTTP.

    Returns:
        Una respuesta con información sobre los cambios realizados en
        ServicioCocina.

    Raises:
        Exception: Si ocurre un error durante la gestión de la petición.
    """
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
    """
    Obtiene un servicio de cocina por su id.

    Args:
      id (int): El id del servicio de cocina

    Returns:
      ServicioCocina: El servicio de cocina correspondiente al id proporcionado
    """
    return self.servicioCocina.get_servicio_cocina_by_id(id)
  
  def get_servicio_by_camarero(self, camarero):
    """
    Obtiene un servicio de cocina por su camarero.

    Args:
      camarero: El camarero del servicio de cocina

    Returns:
      Una lista de servicios de cocina asociados al camarero proporcionado
    """
    return self.servicioCocina.get_servicio_by_camarero(camarero)
    
  def get_servicio_by_mesa(self, mesa):
    """
    Obtiene un servicio de cocina por su mesa.

    Args:
      mesa: La mesa del servicio de cocina

    Returns:
      Una lista de servicios de cocina asociados a la mesa proporcionada
    """
    return self.servicioCocina.get_servicio_by_mesa(mesa)
      
  def get_servicio_by_hora(self, hora: timezone):
    """
    Obtiene un servicio de cocina por su hora.

    Args:
      hora (timezone): La hora del servicio de cocina

    Returns:
      Una lista de servicios de cocina asociados a la hora proporcionada
    """
    return self.servicioCocina.get_servicio_by_hora(hora)
  
  def crear_servicio(self, mesa, camarero, plato, servido: bool = None , hora: timezone = utc_dt):
    """
    Crea un nuevo servicio de cocina.

    Args:
      mesa: La mesa del servicio de cocina
      camarero: El camarero del servicio de cocina
      plato: El plato del servicio de cocina
      servido (bool, opcional): El estado del servicio de cocina. Por defecto es None
      hora (timezone, opcional): La hora del servicio de cocina. Por defecto es la hora actual

    Returns:
      El servicio de cocina creado
    """
    return self.servicioCocina.crear_servicio(mesa, camarero, plato, servido, hora)
  
  def crear_actualizar_servicio(self, id: int, mesa_camarero, plato, servido: bool = None , date: timezone = utc_dt):
    """
    Crea un nuevo servicio de cocina o actualiza uno existente.

    Args:
      id (int): El id del servicio de cocina a actualizar
      plato: El plato del servicio de cocina
      servido (bool, opcional): El estado del servicio de cocina. Por defecto es None
      mesa_camarero: La mesa y camarero del servicio de cocina
      date (timezone, opcional): La fecha del servicio de cocina. Por defecto es la fecha actual

    Returns:
      El servicio de cocina creado o actualizado
    """
    return self.servicioCocina.crear_actualizar_servicio(id, plato, servido, mesa_camarero, date)
  
  def get_servicio_mesa_cantidad_pedidos(self):
    """
    Obtiene una lista de servicios de cocina ordenados por mesa con la cantidad de pedidos asociados a cada mesa.

    Returns:
      Una lista de servicios de cocina ordenados por mesa con la cantidad de pedidos asociados a cada mesa
    """
    return self.servicioCocina.get_servicio_mesa_cantidad_pedidos()

  def get_agrupaciones_by_camarero_mesa_id(self, id_camarero_mesa: int):
    """
    Obtiene un listado de servicios de cocina agrupados por camarero y mesa.

    Args:
      id_camarero_mesa (int): El id de la asociación entre camarero y mesa

    Returns:
      Una lista de servicios de cocina agrupados por camarero y mesa
    """
    pedidos =  self.servicioCocina.get_agrupaciones_by_camarero_mesa(id_camarero_mesa = id_camarero_mesa)
    return pedidos

  def cambiar_estado_servicio(self, id: int, estado: bool):
    """
    Cambia el estado de un servicio de cocina.

    Args:
      id (int): El id del servicio de cocina
      estado (bool): El nuevo estado del servicio de cocina

    Returns:
      El estado actualizado del servicio de cocina
    """
    return self.servicioCocina.cambiar_estado(id, estado)

  def check_isinstance(self, element_to_check):
    """
    Verifica si el elemento a verificar es una cadena de texto.
    Si es una cadena de texto, asigna el valor de la cadena a la variable 'error'
    y devuelve False.

    Args:
      element_to_check: El elemento a verificar.

    Returns:
      El elemento a verificar si no es una cadena de texto, de lo contrario
      devuelve False.
    """
    if isinstance(element_to_check, str):
        self.error = element_to_check
        element_to_check = False
    return element_to_check

  def respuesta(self, error: str = None):
    """
    Genera un diccionario con información sobre el usuario, las mesas y los platos
    disponibles.

    Args:
      error (str, opcional): Un mensaje de error. Por defecto es None.

    Returns:
      Un diccionario con la información solicitada.
    """
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
