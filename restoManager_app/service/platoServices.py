from restoManager_app.models import Plato, Plato_Categoria

class PlatoService:
    _platos: Plato

    def __init__(self):
       self._platos = Plato.objects.all() 

    def crear_plato_cat_relacion(plato, numero, categoria, estado): # MOVER ESTA FUNCION DONDE SE LE CORRESPONDA...
        relacion = Plato_Categoria.objects.create(plato=plato, numero_menu=numero, categoria=categoria, habilitado=estado)
        return relacion
    
    def get_plato_by_name(self, nombre_plato:str):
        # plato = Plato.objects.filter(nombre=nombre_plato).first
        plato = self._platos.filter(nombre=nombre_plato).first
        return plato
    
    def get_plato_by_id(self, idPlato):
        plato = self._platos.filter(id=idPlato)
        return plato

    def crear_plato(nombrePlato, numeroPlato, categoria, estado, descripcion):
        plato = Plato.objects.create(nombre=nombrePlato, descripcion=descripcion)
        return plato