from django.http import HttpRequest

from .plato_controller import *
from .categoria_controller import *

def crear_plato_categoria(req: HttpRequest):
    nombre_plato = req.POST.get("nombre-plato")
    numero_plato = req.POST.get("numero-plato")
    nombre_categoria = req.POST.get("categoria")
    estado = int(req.POST.get("estado"))
    descripcion = req.POST.get("descripcion")
    
    plato=PlatoController.get_plato_by_name(nombre_plato)
    if plato is None:
        plato=PlatoController.crear_plato(nombre_plato, descripcion)

    categoria = CategoriaController.get_categoria_by_name(nombre_categoria)
    if categoria is None:
        categoria=CategoriaController.crear_categoria(nombre_categoria)

    relacion_plato_cat = get_relacion_by_plato_cat(plato, categoria)
    
    if relacion_plato_cat is None:
        relacion_plato_cat


def get_relacion_by_plato_cat(plato: Plato, categoria: Categoria):
    relacion = Plato_Categoria.objects.filter(plato=plato, categoria=categoria)
    return relacion