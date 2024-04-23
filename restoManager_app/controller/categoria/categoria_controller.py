from django.http import HttpRequest

from ...models import Categoria
from ...service.categoria.categoria_services import CategoriaService

class CategoriaController:
    _categoria_service: CategoriaService

    def __init__(self):
        self._categoria_service=CategoriaService()

    def get_categoria_by_name(self, nombre_categoria: str) -> Categoria | None:
        categoria=self._categoria_service.get_categoria_by_name(nombre_categoria)
        return categoria

    def get_categoria_by_id(self, id) -> Categoria | None:
        categoria=self._categoria_service.get_categoria_by_id(id)
        return categoria

    def crear_categoria(self, nombre: str) -> Categoria | None:
        categoria = self._categoria_service.get_categoria_by_name(nombre)
        if not categoria:
            categoria=self._categoria_service.crear_categoria(nombre)
        return categoria

    def actualizar_categoria(self, id_categoria: int, nombre: str) -> Categoria | None:
        categoria=self._categoria_service.actualizar_categoria(id_categoria, nombre)
        return categoria
    
    def eliminar_categoria(self, id_categoria):
        categoria = self._categoria_service.eliminar_categoria(id_categoria)
        return categoria