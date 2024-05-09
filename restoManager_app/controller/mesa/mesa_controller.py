from django.http import HttpRequest
from django.shortcuts import render

from ...service.mesa.mesa_services import MesaService
import logging

logger = logging.getLogger(__name__)

class MesaController:
    _mesa_service: MesaService
    req: HttpRequest
    def __init__(self, request: HttpRequest = None):
        self._mesa_service=MesaService()
        self.req = request

    def peticiones(self):
        peticion = self.req.POST
        if peticion.get('btn') == 'IN':
            numero = int(peticion.get('numero_mesas'))
            self.modificar_mesa_interior(numero)
        
        if peticion.get('btn') == 'OUT':
            numero = int(peticion.get('numero_mesas'))
            self.modificar_mesa_terraza(numero)

        return self.get_numero_de_mesas()

    def modificar_mesa_terraza(self, numero: int):
        total_mesa_out = self.get_numero_de_mesas()['total_out']
        if total_mesa_out < numero:
            self.crear_mesas_terraza(numero - total_mesa_out)
        elif total_mesa_out > numero:
            self.eliminar_mesas_terraza(total_mesa_out - numero)

    def modificar_mesa_interior(self, numero: int):
        total_mesa_in = self.get_numero_de_mesas()['total_in']
        if total_mesa_in < numero:
            self.crear_mesas_interior(numero - total_mesa_in)
        elif total_mesa_in > numero:
            self.eliminar_mesas_interior(total_mesa_in - numero)

    def crear_mesas_interior(self, numero: int):
        logger.info(f"Creando mesas interior {numero}")
        self._mesa_service.crear_mesas_interior(numero)

    def eliminar_mesas_interior(self, numero: int):
        self._mesa_service.eliminar_mesas_interior(numero)

    def crear_mesas_terraza(self, numero: int):
        self._mesa_service.crear_mesas_terraza(numero)

    def eliminar_mesas_terraza(self, numero: int):
        self._mesa_service.eliminar_mesas_terraza(numero)

    def get_numero_de_mesas(self):
        lista = self._mesa_service.get_mesas()
        diccionario = {
            'mesa_id': [],
            'lugar': [],
            'total_in': 0,
            'total_out': 0
        }
        for mesa in lista:
            diccionario['mesa_id'].append(mesa.id)
            diccionario['lugar'].append(mesa.lugar)
            if mesa.lugar == 'Interior':
                diccionario['total_in'] += 1
            else:
                diccionario['total_out'] += 1
        return diccionario