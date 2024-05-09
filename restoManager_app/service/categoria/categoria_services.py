from restoManager_app.models import Categoria
import logging
logger = logging.getLogger(__name__)
class CategoriaService:
    __categoria: Categoria
    
    def __init__(self):
        self.__categoria = Categoria

    def get_categoria_by_name(self, nombre_categoria: str) -> Categoria:
        categoria=Categoria.objects.filter(nombre=nombre_categoria).first()
        return categoria

    def get_categoria_by_id(self, id:int) -> Categoria | None:
        categoria=self.__categoria.objects.filter(id)
        return categoria

    def crear_categoria(self, nombre: str) -> Categoria | None:
        categoria=self.__categoria.objects.create(nombre=nombre)
        return categoria

    def actualizar_categoria(self, id_categoria: int, nombre: str) -> Categoria | None:
        logger.info(id_categoria)
        categoria=Categoria.objects.filter(id=id_categoria).update(nombre=nombre)
        return categoria

    def eliminar_categoria(self, id_categoria: int):
        categoria = Categoria.objects.filter(id=id_categoria).delete()
        return categoria
    
    def get_categorias(self):
        categorias = Categoria.objects.all()
        return categorias