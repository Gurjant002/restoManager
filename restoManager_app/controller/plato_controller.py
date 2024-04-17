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
        plato: Plato
        plato = self._platoService.get_plato_by_name(nombre_plato)
        return plato

    def get_plato_by_id(self, idPlato):
        plato = self._platoService.get_plato_by_id(idPlato)
        return plato

    def crear_plato(self, nombrePlato, descripcion) -> Plato | None:
        plato = self._platoService.get_plato_by_name(nombrePlato)
        if plato is not None:
            return plato
        else:
            plato = self._platoService.crear_plato(nombrePlato, descripcion)
        return plato
    
    def actualizar_plato(self, id_plato: int, nombre_plato: str, descripcion: str):
        plato=self._platoService.actualizar_plato(id_plato, nombre_plato, descripcion)
        return plato

    def eliminar_plato(self, id_plato):
        plato = self._platoService.eliminar_plato(id_plato)
        return plato