import logging

from django.http import HttpRequest
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError

from restoManager_app.service.bebida.bebida_service import BebidaService
from restoManager_app.service.categoria.categoria_services import CategoriaService
from restoManager_app.service.plato.plato_services import PlatoService
from restoManager_app.service.relacion.relacion_plato_categoria_service import PlatoCategoriaService
from restoManager_app.service.trabajadores.rol_service import RolService

from cocina_app.controller.servicio_cocina_controller import ServicioCocinaController
from cocina_app.models import Servicio_Cocina, Servicio_Barra
from cocina_app.service.servicio_cocina_service import ServicioCocinaService

from camarero_app.models import Camarero_Mesa
from .camarero_mesa_controller import CamareroMesaController
from restoManager_app.controller.ubicacion.ubicacion_controller import UbicacionController

logger = logging.getLogger(__name__)


class CamareroController:
    """
    Controlador para el rol de Camarero.
    """

    ubicacionController: UbicacionController
    req: HttpRequest

    def __init__(self, request: HttpRequest = None):
        """
        Inicializa el controlador de Camarero.

        Args:
            request (HttpRequest, optional): La solicitud HTTP. Defaults to None.
        """
        self.req = request
        self.rolService = RolService()
        self.camareroMesaController = CamareroMesaController()
        self.servicioCocinaService = ServicioCocinaService()
        self.ubicacionController = UbicacionController()
        self.categoriaService = CategoriaService()
        self.bebidaService = BebidaService()
        self.relacionPlatoCategoria = PlatoCategoriaService()
        self.plato = PlatoService()
        self.servicioCocinaController = ServicioCocinaController()
        self.error = None

    def peticiones(self) -> dict:
        """
        Procesa las peticiones del rol de Camarero.

        Esta función se encarga de manejar las distintas peticiones realizadas por el
        Camarero, ya sean para cambiar el estado de un servicio de cocina, crear una
        nueva mesa, solicitar un nuevo pedido, entre otras.

        Retorna:
            dict: La respuesta con posibles errores.
        """
        peticion = self.req.POST
        errores = ''
        try:
            if 'cambiar-estado' in peticion:
                id = int(peticion['cambiar-estado'].split('-')[0])
                estado = peticion['cambiar-estado'].split('-')[1]
                self.error = self.servicioCocinaController.cambiar_estado_servicio(id, estado)
                
            if 'add-mesa' in peticion:
                numero_mesa = int(peticion.get('numero-mesa'))
                lugar = int(peticion.get('lugar'))
                camarero = self.req.user.id
                errores = self.crear_mesa(numero_mesa, camarero, lugar)
            if 'borrar-mesa' in peticion:
                print(peticion)
                
            if 'solicitar-cocina' in peticion:
                id_mesa = int(peticion.get('mesa-seleccionada'))
                id_platos = peticion.getlist('platos')
                id_bebidas = peticion.getlist('bebidas')
                platos = []
                bebidas = []
                for id_plato in id_platos:
                    cantidad = int(peticion.get(f'cantidad-platos-{id_plato}'))
                    for i in range(cantidad):
                        plato = self.plato.get_plato_by_id(id_plato)
                        platos.append(plato)

                for id_bebida in id_bebidas:
                    cantidad = int(peticion.get(f'cantidad-bebidas-{id_bebida}'))
                    for i in range(cantidad):
                        bebida = self.bebidaService.get_bebida_by_id(id_bebida)
                        bebidas.append(bebida)
                    
                if platos or bebidas:
                    self.error = self.solicitar_pedido(id_mesa, platos, bebidas)
                    if isinstance(self.error, Servicio_Cocina):
                        return self.respuestas()
                return self.respuestas()
        
        except MultiValueDictKeyError as e:
            logger.error(f'Error al obtener la peticion en CamareroController.peticiones: {peticion}')
            self.error = f'Error al obtener la peticion en CamareroController.peticiones: {peticion}'

        return self.respuestas()

    def solicitar_pedido(self, mesa_camarero, platos: list, bebidas: list, servido: bool = None):
        """
        Esta función se encarga de solicitar un pedido a la cocina.

        Args:
            mesa_camarero (int): El id de la mesa en la que se solicita el pedido.
            platos (list): La lista de platos que se van a solicitar.
            bebidas (list): La lista de bebidas que se van a solicitar.
            servido (bool, optional): Si el pedido ya se ha servido. Defaults to None.

        Returns:
            error (Servicio_Cocina|None): Si se ha encontrado un error al crear el servicio de cocina, devolverá el objeto Servicio_Cocina, de lo contrario, devolverá None.
        """
        instancia_mesa = self.camareroMesaController.get_relacion_by_id(mesa_camarero)
        bebida_servir = []
        for plato in platos:
            error = self.servicioCocinaService.crear_servicio(instancia_mesa, plato, servido)
        if isinstance(error, Servicio_Cocina):
            for bebida in bebidas:
                bebida_servir.append(Servicio_Barra.objects.create(bebida=bebida, servido=None, camarero_mesa=instancia_mesa, hora_dia=timezone.localtime()))

        return error

    def crear_mesa(self, numero_mesa: int, camarero_id, ubicacion_id: int):
        """
        Esta función se encarga de crear una relación entre un camarero y una ubicación en la base de datos.

        Args:
            numero_mesa (int): El número de la mesa que se va a crear.
            camarero_id (int): El id del camarero que se va a asignar a la mesa.
            ubicacion_id (int): El id de la ubicación donde se va a colocar la mesa.

        Returns:
            camarero_mesa (Camarero_Mesa|str): Si se ha creado la relación de manera exitosa, devolverá el objeto Camarero_Mesa, de lo contrario devolverá un mensaje de error.
        """
        camarero = self.rolService.get_rol_by_user_rol(camarero_id, 'Camarero')
        if isinstance(camarero, str) or camarero is None:
            camarero = self.rolService.get_rol_by_user_rol(camarero_id, 'Administrador')
        if isinstance(camarero, str):
            logger.error('Ha habido un error al obtener el rol del usuario. Es probable que este usuaro no tenga ningun rol. Pero aun así se ha saltado un paso de validación de rol. Por lo tanto no se puede crear la mesa. Avise al administrador.')
            self.error = f'Ha habido un error al obtener el rol del usuario, {camarero_id}. Es probable que este usuario no tenga ningún rol. Pero aún así se ha saltado un paso de validación de rol. Por lo tanto no se puede crear la mesa. Avise al administrador.'
            return self.error
        else:
            ubicacion = self.ubicacionController.get_ubicacion_by_id(ubicacion_id)
            return self.camareroMesaController.crear_mesa(numero_mesa, camarero, ubicacion)

    def get_mesas(self):
        return self.camareroMesaController.get_relaciones()

    def check_isinstance(self, element_to_check):
        """
        Esta función se encarga de verificar si un elemento es una instancia de una clase específica.

        Args:
            element_to_check (object): El elemento que se va a verificar.

        Returns:
            element_to_check (object|bool): Si el elemento es una instancia de la clase esperada, devolverá el objeto, de lo contrario devolverá False.
        """
        if isinstance(element_to_check, str):
            self.error = element_to_check
            element_to_check = False
        
        return element_to_check

    def agrupacion_pedidos(self):
        """
        Esta función se encarga de obtener las agrupaciones de pedidos en la base de datos.

        Returns:
            agrupaciones (list): Una lista de objetos de Servicio_Cocina que representan las agrupaciones de pedidos.
        """
        agrupaciones = self.servicioCocinaService.get_agrupaciones()
        return agrupaciones
    
    def get_pedidos_mesas(self, id_camarero_mesa: int):
        """
        Esta función se encarga de obtener los pedidos de una mesa específica.

        Args:
            id_camarero_mesa (int): El id de la relación entre la mesa y el camarero.

        Returns:
            agrupaciones (list): Una lista de objetos de Servicio_Cocina que representan los pedidos de la mesa.
        """
        return self.servicioCocinaController.get_agrupaciones_by_camarero_mesa_id(id_camarero_mesa)

    def lista_platos(self):
        """
        Esta función se encarga de obtener la lista de platos y categorías habilitados en la base de datos.

        Returns:
            platos (list): Una lista de objetos de PlatoCategoria que representan los platos y categorías habilitados.
        """
        platos = PlatoCategoriaService().get_lista_relacion_plato_categoria_por_habilitado()
        return platos

    def respuestas(self, error: str = None, warning: str = None, nota = None) -> dict:
        """
        Esta función se encarga de generar un diccionario con las respuestas necesarias para el controlador de Camarero.

        Args:
            error (str, optional): Un mensaje de error. Defaults to None.
            warning (str, optional): Un mensaje de advertencia. Defaults to None.
            nota (str, optional): Una nota. Defaults to None.

        Returns:
            diccionario (dict): Un diccionario con las respuestas necesarias para el controlador de Camarero.
        """
        if isinstance(error, str):
            self.error = error
        usuario = self.req.user
        mesas = self.get_mesas()
        ubicaciones = UbicacionController().get_ubicaciones()
        
        camarero = self.rolService.get_rol_by_user_rol(usuario, "Administrador")
        if isinstance(camarero, str) or camarero is None:
            camarero = self.rolService.get_rol_by_user_rol(usuario, "Camarero")

        platos = self.lista_platos()
        bebidas = BebidaService().get_bebidas()

        if self.error == '' or self.error is None:
            camarero = self.check_isinstance(camarero)
        if self.error is None or self.error == '':
            mesas = self.check_isinstance(mesas)
        if self.error is None or self.error == '':
            nota = self.check_isinstance(nota)
        if self.error is None or self.error == '':
            ubicaciones = self.check_isinstance(ubicaciones)

        if ubicaciones == 'No se encontro ninguna ubicacion':
            ubicaciones = None


        pedidos_mesas = []
        if mesas is not None and mesas is not False:
            for mesa in mesas:
                pedidos_mesas.append(self.get_pedidos_mesas(mesa.id))
        if self.error is None or self.error == '':
            pedidos_mesas = self.check_isinstance(pedidos_mesas)
        
        diccionario = {
            'error': self.error,
            'warning': warning,
            'es_camarero': camarero,
            'mesas': mesas,
            'ubicaciones': ubicaciones,
            'platos': platos,
            'bebidas': bebidas,
            'nota': nota,
            'pedidos': pedidos_mesas,
        }
        return diccionario

