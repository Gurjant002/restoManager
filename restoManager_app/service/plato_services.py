from restoManager_app.models import Plato, Plato_Categoria

class PlatoService:
    _platos: Plato

    def __init__(self):
    #    self._platos = Plato.objects.all()
       self._platos = Plato()
       
    def get_platos(self) -> Plato:
        return self._platos.objects.all()

    def crear_plato_cat_relacion(self, plato, numero, categoria, estado) -> Plato: # MOVER ESTA FUNCION DONDE SE LE CORRESPONDA...
        relacion = Plato_Categoria.objects.create(plato=plato, numero_menu=numero, categoria=categoria, habilitado=estado)
        return relacion
    
    def get_plato_by_name(self, nombre_plato:str) -> Plato | None:
        # print(Plato.get_all_plato())
        # plato = Plato.get_by_name(Plato, 'Test')
        plato = Plato.objects.filter(nombre=nombre_plato).first()
        print(plato)
        return plato
    
    def get_plato_by_id(self, id_plato) -> Plato:
        plato = self._platos.filter(id=id_plato)
        return plato

    def crear_plato(self, nombrePlato, numeroPlato, categoria, estado, descripcion) -> Plato:
        plato = Plato.objects.create(nombre=nombrePlato, descripcion=descripcion)
        return plato

    def actualizar_plato(self, id_plato: int, nombre_plato: str, descripcion_plato: str) -> Plato:
        plato = self._platos.objects.filter(id=id_plato).update(nombre=nombre_plato, descripcion=descripcion_plato)
        return plato

    def eliminar_plato(self, id_plato) -> Plato:
        plato = self._platos.objects.filter(id=id_plato).delete()