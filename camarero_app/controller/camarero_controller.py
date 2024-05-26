from django.http import HttpRequest
from django.utils.datastructures import MultiValueDictKeyError
from restoManager_app.service.trabajadores.camarero_service import CamareroService

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
        self.camareroService = CamareroService()
        self.camareroMesaController = CamareroMesaController()
        self.servicioCocinaService = ServicioCocinaService()
        self.ubicacionController = UbicacionController()
        self.categoriaService = CategoriaService()
        self.relacionPlatoCategoria = PlatoCategoriaService()
        self.plato = PlatoService()

    def peticiones(self) -> dict:
        peticion = self.req.POST
        errores = ''
        try:
            if 'add-mesa' in peticion:
                numero_mesa = int(peticion.get('numero-mesa'))
                lugar = int(peticion.get('lugar'))
                camarero = int(peticion.get('camarero'))
                errores = self.crear_mesa(numero_mesa, camarero, lugar)
            elif 'borrar-mesa' in peticion:
                print(peticion)
                
            elif 'solicitar-cocina' in peticion:
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
        camarero = self.camareroService.get_camarero_by_user(camarero_id)
        ubicacion = self.ubicacionController.get_ubicacion_by_id(ubicacion_id)
        return self.camareroMesaController.crear_mesa(numero_mesa, camarero, ubicacion)

    def get_mesas(self):
        return self.camareroMesaController.get_relaciones()

    def chech_isinstance(self, element_to_check):
        error = ''
        if isinstance(element_to_check, str):
            error = element_to_check
            element_to_check = False
        
        return element_to_check, error

    def agrupacion_pedidos(self):
        agrupaciones = self.servicioCocinaService.get_agrupaciones()
        return agrupaciones

    def lista_platos(self):
        platos = PlatoCategoriaService().get_lista_relacion_plato_categoria()
        return platos

    def respuestas(self, error: str = None, warning: str = None, nota = None) -> dict:
        usuario = self.req.user
        mesas = self.get_mesas()
        ubicaciones = UbicacionController().get_ubicaciones()
        camarero = CamareroService().get_camarero_by_user(usuario)
        platos = self.lista_platos()
        bebidas = BebidaService().get_bebidas()
        tapas = self.categoriaService.get_categorias()

        camarero, error = self.chech_isinstance(camarero)
        mesas, error = self.chech_isinstance(mesas)
        nota, error = self.chech_isinstance(nota)

        pedidos = self.agrupacion_pedidos()
        pedidos, error = self.chech_isinstance(pedidos)

        diccionario = {
            'error': error,
            'warning': warning,
            'es_camarero': camarero,
            'mesas': mesas,
            'ubicaciones': ubicaciones,
            'platos': platos,
            'bebidas': bebidas,
            'nota': nota,
            'tapas': tapas,
            'pedidos': pedidos,
        }
        return diccionario
