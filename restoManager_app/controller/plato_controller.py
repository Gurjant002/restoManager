from django.http import HttpRequest
from datetime import datetime

from ..models import Categoria, Plato, Plato_Categoria
from ..service.plato_services import *
from ..service.categoria_services import *

class PlatoController:
    _platoService: PlatoService
    
    def __init__(self):
        self._platoService = PlatoService()

    def get_plato_by_name(self, nombre_plato: str) -> Plato | None:
        print(nombre_plato)
        plato = self._platoService.get_plato_by_name(nombre_plato)
        return plato

    def get_plato_by_id(self, idPlato):
        plato = self._platoService.get_plato_by_id(idPlato)
        return plato

    def crear_plato(self, nombrePlato, descripcion) -> Plato | None:
        plato = self._platoService.crear_plato(nombre=nombrePlato, descripcion=descripcion)
        return plato
    
    def actualizar_plato(self, id_plato: int,  nombre_plato: str, descripcion: str):
        plato=self._platoService.actualizar_plato(id_plato, nombre_plato, descripcion)
        return plato
    
    def dimeAlgo(self):
        return 'Hola Wacho'

""" 
def crear_platoXD(post_request:HttpRequest):
    new_plato = ""
    new_cat = ""
    result = ""
    
    nombrePlato = post_request.POST.get("nombre-plato")
    numeroPlato = post_request.POST.get("numero-plato")
    categoria = post_request.POST.get("categoria")
    estado = int(post_request.POST.get("estado"))
    descripcion = post_request.POST.get("descripcion")
    
    platoExiste = Plato.objects.filter(nombre=nombrePlato).first()

    if platoExiste is None:
        catExiste = Categoria.objects.filter(nombre=categoria).first()
        if catExiste is None:
            new_cat = crear_categoria(categoria)
        else:
            new_cat = catExiste
            
        new_plato = Plato.objects.create(nombre=nombrePlato, descripcion=descripcion)
        
        crear_plato_cat_relacion(new_plato, numeroPlato, new_cat, estado)
        result = "Nuevo plato creado:",new_plato.nombre
    else:
        result = "El plato que intentas crear, ya existe:",nombrePlato

    return result

def eliminar_plato_cat_relacion(post_request:HttpRequest):
    texto = post_request.POST.get("eliminar-btn")
    texto = texto.split("|")
    plat_cat_id = int(texto[1])
    result = ""
    
    platoExist = Plato_Categoria.objects.filter(id=plat_cat_id)
    if platoExist != None:
        print(plat_cat_id)
        Plato_Categoria.objects.filter(id=plat_cat_id).delete()
        result = "Plato eliminado."
    else: # Esta condicion es inecesaria.
        result = "El plato que intentas borrar, no existe"
    return result

 """