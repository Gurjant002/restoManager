from django.http import HttpRequest

from ..models import Categoria
from ..service.categoria_services import CategoriaService

class CategoriaController:
    __categoria_service: CategoriaService

    def __init__(self):
        self.__categoria_service=CategoriaService()

    def get_categoria_by_name(nombre_categoria) -> Categoria | None:
        categoria=CategoriaService.get_categoria_by_name(nombre_categoria)
        return categoria

    def get_categoria_by_id(self, id) -> Categoria | None:
        categoria=self.__categoria_service.get_categoria_by_id(id)
        return categoria

    def crear_categoria(self, nombre: str) -> Categoria | None:
        categoria=self.__categoria_service.crear_categoria(nombre)
        return categoria

    def actualizar_categoria(self, id_categoria, nombre: str) -> Categoria | None:
        categoria=self.__categoria_service.actualizar_categoria(id_categoria, nombre)
        return categoria