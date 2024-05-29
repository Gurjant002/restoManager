from django.http import HttpRequest
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from ...service.ubicacion.ubicacion_services import UbicacionService
import logging

logger = logging.getLogger(__name__)

class UbicacionController:
    _ubicacion_service: UbicacionService
    req: HttpRequest
    def __init__(self, request: HttpRequest = None):
        self._ubicacion_service=UbicacionService()
        self.req = request

    def peticiones(self):
        peticion = self.req.POST
        try:
            if 'crear' in peticion:
                ubicacion = self.crear_ubicacion(peticion.get('ubicacion'))
            elif 'eliminar' in peticion:
                ubicacion = self.eliminar_ubicacion(peticion.get('eliminar'))
            elif 'getById' in peticion:
                ubicacion = self.get_ubicacion_by_id(int(peticion.get('id')))
            elif 'getByLugar' in peticion:
                ubicacion = self.get_ubicacion_by_lugar(peticion.get('lugar'))
            elif 'getAll' in peticion:
                ubicacion = self.get_ubicaciones()
            elif 'update' in peticion:
                ubicacion = self.actualizar_ubicacion(int(peticion.get('update')), peticion.get('ubicacion'))
            else:
                ubicacion = ''
        except MultiValueDictKeyError:
            logger.error(f'Error al obtener la peticion en UbicacionController.peticiones: {peticion}')
            ubicacion = f'Error al obtener la peticion en UbicacionController.peticiones: {peticion}'

        if isinstance(ubicacion, str):
            return self.get_numero_de_ubicacion(errorMessage=ubicacion)
        return self.get_numero_de_ubicacion()

    def crear_ubicacion(self, ubicacion: str):
        return self._ubicacion_service.crear_ubicacion(ubicacion)

    def actualizar_ubicacion(self, id_ubicacion: int, ubicacion: str):
        return self._ubicacion_service.actualizar_ubicacion(id_ubicacion, ubicacion)

    def eliminar_ubicacion(self, idUbicacion: int):
        return self._ubicacion_service.eliminar_ubicacion(idUbicacion)

    def get_ubicacion_by_id(self, id_ubicacion: int):
        return self._ubicacion_service.get_ubicacion_by_id(id_ubicacion)

    def get_ubicacion_by_lugar(self, lugar: str):
        return self._ubicacion_service.get_ubicacion_by_lugar(lugar)

    def get_ubicaciones(self):
        return self._ubicacion_service.get_ubicaciones()

    def get_numero_de_ubicacion(self, errorMessage: str = '', warning: str = ''):
        lista = self._ubicacion_service.get_ubicaciones()
        if isinstance(lista, str):
            errorMessage = lista
            lista = None
        diccionario = {
            'ubicaciones': lista,
            'error': errorMessage,
            'warning': warning,
        }
        return diccionario