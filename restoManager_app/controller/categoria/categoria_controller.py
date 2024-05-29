from django.http import HttpRequest
from django.shortcuts import render

from ...models import Categoria
from ...service.categoria.categoria_services import CategoriaService
import logging

logger = logging.getLogger(__name__)

class CategoriaController:
    _categoria_service: CategoriaService
    req: HttpRequest
    def __init__(self, request: HttpRequest = None):
        self._categoria_service=CategoriaService()
        self.req = request

    def peticiones(self):
        peticion = self.req.POST
        nombre = peticion.get('nombre')
        
        # Crear
        if peticion.get('new-categoria'):
            self.crear_categoria(nombre)
        
        # Actualizar
        elif peticion.get('update-categoria'):
            id_categoria = peticion.get('update-categoria').split('_')[2]
            self.actualizar_categoria(id_categoria,nombre)
            
        # Eliminar
        elif peticion.get('eliminar'):
            id_categoria = peticion.get('eliminar').split('|')[1]
            self.eliminar_categoria(id_categoria)
        return self.get_lista_categorias()


    def get_categoria_by_name(self, nombre_categoria: str) -> Categoria | None:
        categoria=self._categoria_service.get_categoria_by_name(nombre_categoria)
        return categoria

    def get_categoria_by_id(self, id) -> Categoria | None:
        categoria=self._categoria_service.get_categoria_by_id(id)
        return categoria

    def crear_categoria(self, nombre: str) -> Categoria | None:
        logger.info(nombre)
        categoria = self._categoria_service.get_categoria_by_name(nombre)
        if not categoria:
            categoria=self._categoria_service.crear_categoria(nombre)
        return categoria

    def actualizar_categoria(self, id_categoria: int = None, nombre: str = '') -> Categoria | None:
        categoria=self._categoria_service.actualizar_categoria(id_categoria, nombre)
        return categoria
    
    def eliminar_categoria(self, id_categoria):
        categoria = self._categoria_service.eliminar_categoria(id_categoria)
        return categoria

    def get_lista_categorias(self) -> dict:
        lista = self._categoria_service.get_categorias()
        if lista is None:
            return render(self.req, 'error.html', {'error': 'No se encontraron bebidas'})
        diccionario = {
            'categorias': lista
        }
        return diccionario