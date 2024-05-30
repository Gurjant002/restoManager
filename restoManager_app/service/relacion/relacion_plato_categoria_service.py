from django.db.models import QuerySet
from restoManager_app.models import Categoria, Plato, Plato_Categoria
import logging

log = logging.getLogger(__name__)

class PlatoCategoriaService:
    """Servicio para gestionar las relaciones entre Plato y Categoria
    """

    __relacion: Plato_Categoria
    def __init__(self):
        self.__relacion=Plato_Categoria

    def get_lista_relacion_plato_categoria(self) -> QuerySet[Plato_Categoria] | None:
        """Obtiene todas las relaciones entre Plato y Categoria

        Returns:
            QuerySet[Plato_Categoria] | None: las relaciones entre Plato y Categoria o None en caso de error
        """
        try:
            relacion = Plato_Categoria.objects.all()
            return relacion
        except Exception as e:
            log.error('Algo salio mal al obtener las relaciones', exc_info=True)
            return 'Algo salio mal al obtener las relaciones'

    def get_lista_relacion_plato_categoria_por_habilitado(self, habilitado: bool = True) -> QuerySet[Plato_Categoria] | None:
        """Obtiene las relaciones entre Plato y Categoria filtradas por habilitado

        Args:
            habilitado (bool, optional): valor de habilitado para filtrar las relaciones. Defaults to True.

        Returns:
            QuerySet[Plato_Categoria] | None: las relaciones entre Plato y Categoria filtradas por habilitado o None en caso de error
        """
        try:
            relacion = Plato_Categoria.objects.filter(habilitado=habilitado)
            return relacion
        except Exception as e:
            log.error('Algo salio mal al obtener las relaciones', exc_info=True)
            return 'Algo salio mal al obtener las relaciones'

    def get_relacion_by_plato(self, plato: Plato) -> Plato_Categoria | None:
        """Obtiene la relacion entre Plato y Categoria por Plato

        Args:
            plato (Plato): Plato del que se obtiene la relacion

        Returns:
            Plato_Categoria | None: la relacion entre Plato y Categoria o None si no existe
        """
        relacion=Plato_Categoria.objects.filter(plato=plato).first()
        return relacion

    def get_relacion_by_categoria(self, categoria: Categoria) -> QuerySet[Plato_Categoria]:
        """Obtiene las relaciones entre Plato y Categoria por Categoria

        Args:
            categoria (Categoria): Categoria del que se obtienen las relaciones

        Returns:
            QuerySet[Plato_Categoria]: las relaciones entre Plato y Categoria
        """
        relacion=Plato_Categoria.objects.filter(categoria=categoria)
        return relacion

    def get_relacion_by_id(self, id: int) -> Plato_Categoria | None:
        """Obtiene la relacion entre Plato y Categoria por id

        Args:
            id (int): id de la relacion entre Plato y Categoria

        Returns:
            Plato_Categoria | None: la relacion entre Plato y Categoria o None si no existe
        """
        relacio=Plato_Categoria.objects.filter(id=id)
        if relacio.count() == 0:
            log.warning("service.get_relacion_by_id> VACIO")
            return None
        return relacio

    def get_relacion_by_plato_and_categoria(self, plato: Plato, categorio: Categoria) -> Plato_Categoria | None:
        """Obtiene la relacion entre Plato y Categoria por Plato y Categoria

        Args:
            plato (Plato): Plato de la relacion
            categorio (Categoria): Categoria de la relacion

        Returns:
            Plato_Categoria | None: la relacion entre Plato y Categoria o None si no existe
        """
        relacion=Plato_Categoria.objects.filter(plato=plato, categoria=categorio)
        return relacion

    def crear_relacion(self, plato: Plato, numero_menu: int, categoria: Categoria, estado: bool) -> Plato_Categoria:
        """Crea una relacion entre Plato y Categoria

        Args:
            plato (Plato): Plato de la relacion
            numero_menu (int): numero de menu de la relacion
            categoria (Categoria): Categoria de la relacion
            estado (bool): estado de la relacion

        Returns:
            Plato_Categoria: la relacion creada
        """
        relacion=Plato_Categoria.objects.create(numero_menu=numero_menu, plato=plato, categoria=categoria, habilitado=estado)
        return relacion

    def actualizar_relacion(self, id_relacion:int ,numero_menu: int, estado) -> Plato_Categoria | None:
        """Actualiza una relacion entre Plato y Categoria

        Args:
            id_relacion (int): id de la relacion
            numero_menu (int): numero de menu de la relacion
            estado (bool): estado de la relacion

        Returns:
            Plato_Categoria | None: la relacion actualizada o None en caso de error
        """
        try:
            log.info("service.actualizar_relacion> ACTUALIZANDO RELACION")
            relacion=Plato_Categoria.objects.filter(id=id_relacion).update(numero_menu=numero_menu, habilitado=estado)
        except Exception as e:
            log.error(e)
        # return relacion

    def eliminar_relacion(self, id_relacion) -> Plato_Categoria:
        """Elimina una relacion entre Plato y Categoria

        Args:
            id_relacion (int): id de la relacion

        Returns:
            Plato_Categoria: la relacion eliminada
        """
        relacion=Plato_Categoria.objects.filter(id=id_relacion).delete()

