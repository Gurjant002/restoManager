from django.http import HttpRequest

from ...service.bebida.bebida_service import *
class BebidaController:
    _bebidaService: BebidaService
    req: HttpRequest
    def __init__(self, request: HttpRequest):
        self._bebidaService = BebidaService()
        self.req = request

    def peticiones(self):
        peticion = self.req.POST
        
        # Crear
        if peticion.get('new-bebida'):
            self.crear_bebida(peticion)
        
        # Actualizar
        elif peticion.get('update-bebida'):
            self.actualizar_bebida(peticion)
        # Eliminar
        elif peticion.get('delete-bebida'):
            self.eliminar_bebida(peticion)

    def crear_bebida(self, peticion):
        nombre = peticion.get('nombre')
        descripcion = peticion.get('descripcion')
        estado = peticion.get('estado')
        alcohol = str(peticion.get('alcohol'))

        bebida = self.get_bebida_by_name(nombre)
        if not bebida:
            bebida = self._bebidaService.crear_bebida(nombre, alcohol, estado, descripcion)
        return bebida

    def actualizar_bebida(self, peticion):
        nombre = peticion.get('nombre')
        descripcion = peticion.get('descripcion')
        estado = peticion.get('estado')
        alcohol = str(peticion.get('alcohol'))

    def eliminar_bebida(self, peticion):
        pass

    def get_bebidas(self):
        return self._bebidaService.get_bebidas()

    def get_bebida_by_id(self, id_bebida):
        return self._bebidaService.get_bebida_by_id(id_bebida)

    def get_bebida_by_name(self, nombre_bebida):
        return self._bebidaService.get_bebida_by_name(nombre_bebida)