from restoManager_app.models import Plato, Plato_Categoria

class PlatoService:
    _platos: Plato

    def __init__(self):
    #    self._platos = Plato.objects.all()
       self._platos = Plato()
       
    def get_platos(self) -> Plato:
        return self._platos.objects.all()

    def get_plato_by_name(self, nombre_plato:str) -> Plato:
        plato: Plato = Plato.objects.filter(nombre=nombre_plato).first()
        return plato
    
    def get_plato_by_id(self, id_plato) -> Plato:
        plato = Plato.objects.filter(id=id_plato).first()
        return plato

    def crear_plato(self, nombrePlato: str, descripcion: str) -> Plato:
        plato = Plato.objects.create(nombre=nombrePlato, descripcion=descripcion)
        return plato

    def actualizar_plato(self, id_plato: int, nombre_plato: str, descripcion_plato: str) -> Plato:
        plato = Plato.objects.filter(id=id_plato).update(nombre=nombre_plato, descripcion=descripcion_plato)
        return plato

    def eliminar_plato(self, id_plato) -> Plato:
        plato = Plato.objects.filter(id=id_plato).delete()