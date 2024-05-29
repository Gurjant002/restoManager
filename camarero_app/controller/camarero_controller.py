from django.http import HttpRequest
from django.utils.datastructures import MultiValueDictKeyError
from cocina_app.controller.servicio_cocina_controller import ServicioCocinaController
from cocina_app.models import Servicio_Cocina
from restoManager_app.service.trabajadores.rol_service import RolService

# Mesa
from restoManager_app.controller.ubicacion.ubicacion_controller import UbicacionController

# Cominda
from restoManager_app.service.relacion.relacion_plato_categoria_service import PlatoCategoriaService
from restoManager_app.service.categoria.categoria_services import CategoriaService
from restoManager_app.service.plato.plato_services import PlatoService

#  Bebida
from restoManager_app.service.bebida.bebida_service import BebidaService
from .camarero_mesa_controller import CamareroMesaController
from camarero_app.models import Camarero_Mesa
from cocina_app.service.servicio_cocina_service import ServicioCocinaService
import logging

logger = logging.getLogger(__name__)
class CamareroController:
    ubicacionController: UbicacionController
    req: HttpRequest
    def __init__(self, request: HttpRequest = None):
        self.req = request
        self.rolService = RolService()
        self.camareroMesaController = CamareroMesaController()
        self.servicioCocinaService = ServicioCocinaService()
        self.ubicacionController = UbicacionController()
        self.categoriaService = CategoriaService()
        self.relacionPlatoCategoria = PlatoCategoriaService()
        self.plato = PlatoService()
        self.servicioCocinaController = ServicioCocinaController()
        self.error = None

    def peticiones(self) -> dict:
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
                camarero = int(peticion.get('camarero'))
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
                    cantidad = int(peticion.get(f'catidad-bebidas-{id_bebida}'))
                    for i in range(cantidad):
                        bebida = self.ubicacionController.get_ubicacion_by_id(id_bebida)
                        bebidas.append(bebida)
                    
                if platos:
                    error = self.solicitar_pedido(id_mesa, platos, bebidas)
                    if isinstance(error, Servicio_Cocina):
                        return self.respuestas(error=None)
                    return self.respuestas(error=error)
        
        except MultiValueDictKeyError:
            logger.error(f'Error al obtener la peticion en CamareroController.peticiones: {peticion}')
            errores = f'Error al obtener la peticion en CamareroController.peticiones: {peticion}'

        return self.respuestas(error=errores)

    def solicitar_pedido(self, mesa_camarero, platos: list, servido: bool = False):
        instancia_mesa = self.camareroMesaController.get_relacion_by_id(mesa_camarero)
        for plato in platos:
            error = self.servicioCocinaService.crear_servicio(instancia_mesa, plato, servido)
        return error
    
    

    def crear_mesa(self, numero_mesa: int, camarero_id, ubicacion_id: int):
        camarero = self.rolService.get_rol_by_user_rol(camarero_id, 'Cocinero')
        if isinstance(camarero, str) or camarero is None:
            camarero = self.rolService.get_rol_by_user_rol(camarero_id, 'Administrador')
        if isinstance(camarero, str):
            logger.error('Ha habido un error al obtener el rol del usuario. Es probable que este usuaro no tenga ningun rol. Pero aun asi se ha saltado un paso de validacion de rol. Por lo tanto no se puede crear la mesa. Avise al administrador.')
            self.error = f'Ha habido un error al obtener el rol del usuario, {camarero_id}.Es probable que este usuaro no tenga ningun rol. Pero aun asi se ha saltado un paso devalidacion de rol. Por lo tanto no se crear la mesa. Avise al administrador.'
            return self.error
        else:
            ubicacion = self.ubicacionController.get_ubicacion_by_id(ubicacion_id)
            return self.camareroMesaController.crear_mesa(numero_mesa, camarero, ubicacion)

    def get_mesas(self):
        return self.camareroMesaController.get_relaciones()

    def check_isinstance(self, element_to_check):
        if isinstance(element_to_check, str):
            self.error = element_to_check
            element_to_check = False
        
        return element_to_check

    def agrupacion_pedidos(self):
        agrupaciones = self.servicioCocinaService.get_agrupaciones()
        return agrupaciones
    
    def get_pedidos_mesas(self, id_camarero_mesa: int):
        return self.servicioCocinaController.get_agrupaciones_by_camarero_mesa_id(id_camarero_mesa)

    def lista_platos(self):
        platos = PlatoCategoriaService().get_lista_relacion_plato_categoria()
        return platos

    def respuestas(self, error: str = None, warning: str = None, nota = None) -> dict:
        self.error = error
        usuario = self.req.user
        mesas = self.get_mesas()
        ubicaciones = UbicacionController().get_ubicaciones()
        
        camarero = self.rolService.get_rol_by_user_rol(usuario, "Administrador")
        if isinstance(camarero, str):
            camarero = self.rolService.get_rol_by_user_rol(usuario, "Camarero")
            
        platos = self.lista_platos()
        bebidas = BebidaService().get_bebidas()
        tapas = self.categoriaService.get_categorias()

        if self.error == '' or self.error is None:
            camarero = self.check_isinstance(camarero)
        if self.error is None or self.error == '':
            mesas = self.check_isinstance(mesas)
        if self.error is None or self.error == '':
            nota = self.check_isinstance(nota)
        
        pedidos_mesas = []
        if mesas is not None:
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
            'tapas': tapas,
            'pedidos': pedidos_mesas,
        }
        return diccionario
