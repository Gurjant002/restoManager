from restoManager_app.admin import Plato_Categoria, Plato, Categoria

class PlatoCategoriaService:
    __relacion: Plato_Categoria
    def __init__(self):
        self.__relacion=Plato_Categoria
    
    def get_lista_relacion_plato_categoria(self) -> Plato_Categoria:
        print("Lol")
        return self.__relacion.objects.all()
    
    def get_relacion_by_plato(self, plato: Plato) -> Plato_Categoria:
        # plato=Plato.objects.filter(nombre=plato).first
        relacion=self.__relacion.filter(plato=plato).first
        return relacion
    
    def get_relacion_by_categoria(self, categoria: Categoria) -> Plato_Categoria:
        relacion=self.__relacion.objects.filter(categoria).all()
        return relacion

    def get_relacion_by_plato_and_categoria(self, plato: Plato, categorio: Categoria) -> Plato_Categoria | None:
        relacion=self.__relacion.objects.filter(plato, categorio)
        return relacion

    """ def crear_relacion_plato_cat(plato, numero, categoria, estado) -> Plato_Categoria:
        relacion=Plato_Categoria.objects.create(plato=plato, numero_menu=numero, categoria=categoria, habilitado=estado)
        return relacion """

    def crear_relacion(plato: Plato, numero_menu: int, categoria: Categoria, estado) -> Plato_Categoria:
        relacion=Plato_Categoria.objects.create(numero_menu, plato, categoria, habilitado=estado)
        return relacion

    def actualizar_relacion(self, id_relacion:int ,numero_menu: int, estado) -> Plato_Categoria | None:
        relacion=self.__relacion.objects.filter(id=id_relacion).update(numero_menu, habilitado=estado)
        return relacion

    def eliminar_relacion(self, id_relacion) -> Plato_Categoria:
        relacion=self.__relacion.objects.filter(id=id_relacion).delete()

""" 
    def get_platos(self) -> Plato:
        return self._platos.objects.all()

    def crear_plato_cat_relacion(plato, numero, categoria, estado) -> Plato: # MOVER ESTA FUNCION DONDE SE LE CORRESPONDA...
        relacion=Plato_Categoria.objects.create(plato=plato, numero_menu=numero, categoria=categoria, habilitado=estado)
        return relacion
    
    def get_plato_by_name(self, nombre_plato:str) -> Plato:
        # plato=Plato.objects.filter(nombre=nombre_plato).first
        plato=self._platos.filter(nombre=nombre_plato).first
        return plato
    
    def get_plato_by_id(self, id_plato) -> Plato:
        plato=self._platos.filter(id=id_plato)
        return plato

    def crear_plato(nombrePlato, numeroPlato, categoria, estado, descripcion) -> Plato:
        plato=Plato.objects.create(nombre=nombrePlato, descripcion=descripcion)
        return plato
    
    def actualizar_plato(self, id_plato, nombre_plato, descripcion_plato) -> Plato:
        plato=self._platos.objects.filter(id=id_plato).update(nombre=nombre_plato, descripcion=descripcion_plato)
        return plato
    def eliminar_plato(self, id_plato) -> Plato:
        plato=self._platos.objects.filter(id=id_plato).delete()
"""