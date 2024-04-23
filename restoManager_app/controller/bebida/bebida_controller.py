from django.http import HttpRequest
from django.shortcuts import render

from ...service.bebida.bebida_service import *

import logging
logger = logging.getLogger(__name__)

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
        elif peticion.get('eliminar'):
            self.eliminar_bebida(peticion)
        return self.get_lista_bebidas()

    def crear_bebida(self, peticion):
        nombre = peticion.get('nombre')
        descripcion = peticion.get('descripcion')
        estado = peticion.get('estado')
        alcohol = peticion.get('alcohol')
        logger.info(f'Nombre bebida: {nombre}, Alcohol: {alcohol}, Estado: {estado}, Descripcion: {descripcion}')
        bebida = self.get_bebida_by_name(nombre)
        if not bebida:
            bebida = self._bebidaService.crear_bebida(nombre, alcohol, estado, descripcion)
        
        logger.info(bebida)
        return bebida

    def actualizar_bebida(self, peticion):
        id_bebida = peticion.get('update-bebida')
        id_bebida = id_bebida.split('_')[2]
        nombre = peticion.get('nombre')
        descripcion = peticion.get('descripcion')
        estado = peticion.get('estado')
        alcohol = peticion.get('alcohol')
        bebida = self._bebidaService.actualizar_bebida(id_bebida, nombre, alcohol, estado, descripcion)
        logger.info(bebida)

    def eliminar_bebida(self, peticion):
        id_bebida = peticion.get('eliminar')
        id_bebida = id_bebida.split('|')[1]
        bebida = self._bebidaService.eliminar_bebida(id_bebida)
        logger.info(bebida)

    def get_bebidas(self):
        return self._bebidaService.get_bebidas()

    def get_bebida_by_id(self, id_bebida):
        return self._bebidaService.get_bebida_by_id(id_bebida)

    def get_bebida_by_name(self, nombre_bebida):
        return self._bebidaService.get_bebida_by_name(nombre_bebida)

    def get_lista_bebidas(self) -> dict:
        lista = self._bebidaService.get_bebidas()
        
        if lista is None:
            return render(self.req, 'error.html', {'error': 'No se encontraron bebidas'})
        
        diccionario = {
            'bebidas': lista
        }
        
        return diccionario