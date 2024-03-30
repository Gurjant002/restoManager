from django.http import HttpRequest

from ..models import Categoria, Plato_Categoria
from ..service.platoServices import *
from ..service.categoriaServices import *

class CategoriaController:
    def get_categoria_by_name(nombre_categoria):
        categoria = CategoriaService.get_categoria_by_name(nombre_categoria)
        return categoria