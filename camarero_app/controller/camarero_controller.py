from django.http import HttpRequest, response
from restoManager_app.controller.mesa.mesa_controller import MesaController
from cocina_app.models import Camarero_Mesa
import logging

logger = logging.getLogger(__name__)
class CamareroController:
    mesaController: MesaController
    req: HttpRequest
    def __init__(self, request: HttpRequest = None):
        self.req = request
        self.mesaController = MesaController()

    def peticiones(self) -> dict:
        if self.req.POST.get('mesas'):
            return self.respuestas(error=self.req.POST.get('mesas'))
        # return self.respuestas()

    def respuestas(self, error: str = None, warning: str = None) -> dict:
        mesasInterior = self.mesaController.get_mesas_interior()
        mesaTerraza = self.mesaController.get_mesas_terraza()
        mesasAsignadas = Camarero_Mesa.objects.all()
        diccionario = {
            'error': error,
            'warning': warning,
            'mesas_interior': mesasInterior,
            'mesas_terraza': mesaTerraza,
            'mesas_asignadas': mesasAsignadas,
        }
        return diccionario
