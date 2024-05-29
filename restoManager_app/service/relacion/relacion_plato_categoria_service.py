from restoManager_app.admin import Plato_Categoria, Plato, Categoria
import logging
log = logging.getLogger(__name__)

class PlatoCategoriaService:
    __relacion: Plato_Categoria
    def __init__(self):
        self.__relacion=Plato_Categoria
    
    def get_lista_relacion_plato_categoria(self) -> Plato_Categoria | None:
        try:
            relacion = Plato_Categoria.objects.all()
            return relacion
        except Exception as e:
            log.error('Algo salio mal al obtener las relaciones', exc_info=True)
            return 'Algo salio mal al obtener las relaciones'
    
    def get_relacion_by_plato(self, plato: Plato) -> Plato_Categoria:
        relacion=Plato_Categoria.filter(plato=plato).first
        return relacion
    
    def get_relacion_by_categoria(self, categoria: Categoria) -> Plato_Categoria:
        relacion=Plato_Categoria.objects.filter(categoria).all()
        return relacion

    def get_relacion_by_id(self, id: int) -> Plato_Categoria | None:
        relacio=Plato_Categoria.objects.filter(id=id)
        if relacio.count() == 0:
            log.warning("service.get_relacion_by_id> VACIO")
            return None
        return relacio

    # ! Este metodo lanza un error.
    def get_relacion_by_numero_menu(self, numero_menu: int) -> Plato_Categoria:
        relacion=Plato_Categoria.objects.filter(id=33)
        return relacion

    def get_relacion_by_plato_and_categoria(self, plato: Plato, categorio: Categoria) -> Plato_Categoria | None:
        relacion=Plato_Categoria.objects.filter(plato=plato, categoria=categorio)
        return relacion

    """ def crear_relacion_plato_cat(plato, numero, categoria, estado) -> Plato_Categoria:
        relacion=Plato_Categoria.objects.create(plato=plato, numero_menu=numero, categoria=categoria, habilitado=estado)
        return relacion """

    def crear_relacion(self, plato: Plato, numero_menu: int, categoria: Categoria, estado: bool) -> Plato_Categoria:
        relacion=Plato_Categoria.objects.create(numero_menu=numero_menu, plato=plato, categoria=categoria, habilitado=estado)
        return relacion

    def actualizar_relacion(self, id_relacion:int ,numero_menu: int, estado) -> Plato_Categoria | None:
        try:
            log.info("service.actualizar_relacion> ACTUALIZANDO RELACION")
            relacion=Plato_Categoria.objects.filter(id=id_relacion).update(numero_menu=numero_menu, habilitado=estado)
        except Exception as e:
            log.error(e)
        # return relacion

    def eliminar_relacion(self, id_relacion) -> Plato_Categoria:
        relacion=Plato_Categoria.objects.filter(id=id_relacion).delete()
