from django.utils import timezone
from restoManager_app.models import Categoria
import logging

logger = logging.getLogger(__name__)

class CategoriaService:
    """
    Clase que implementa servicios para el modelo Categoria
    """
    __categoria: Categoria
    
    def __init__(self):
        """
        Inicializa el objeto
        """
        self.__categoria = Categoria

    def get_categoria_by_name(self, nombre_categoria: str) -> Categoria:
        """
        Obtiene una categoria por su nombre

        Args:
            nombre_categoria (str): nombre de la categoria

        Returns:
            Categoria: la categoria obtenida o None si no existe
        """
        categoria=Categoria.objects.filter(nombre=nombre_categoria).first()
        return categoria

    def get_categoria_by_id(self, id:int) -> Categoria | None:
        """
        Obtiene una categoria por su id

        Args:
            id (int): id de la categoria

        Returns:
            Categoria | None: la categoria obtenida o None si no existe
        """
        categoria=Categoria.objects.filter(id=id).first()
        return categoria

    def crear_categoria(self, nombre: str) -> Categoria | None:
        """
        Crea una nueva categoria

        Args:
            nombre (str): nombre de la categoria

        Returns:
            Categoria: la categoria creada
        """
        categoria=self.__categoria.objects.create(nombre=nombre)
        return categoria

    def actualizar_categoria(self, id_categoria: int, nombre: str) -> Categoria | None:
        """
        Actualiza una categoria

        Args:
            id_categoria (int): id de la categoria
            nombre (str): nuevo nombre de la categoria

        Returns:
            Categoria | None: la categoria actualizada o None si no existe
        """
        logger.info(id_categoria)
        categoria=Categoria.objects.filter(id=id_categoria).update(nombre=nombre)
        return categoria

    def eliminar_categoria(self, id_categoria: int):
        """
        Elimina una categoria

        Args:
            id_categoria (int): id de la categoria
        """
        categoria = Categoria.objects.filter(id=id_categoria).delete()
        return categoria
    
    def get_categorias(self):
        """
        Obtiene todas las categorias

        Returns:
            QuerySet[Categoria]: lista de categorias
        """
        categorias = Categoria.objects.all()
        return categorias
