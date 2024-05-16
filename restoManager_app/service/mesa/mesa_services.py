from restoManager_app.models import Ubicacion
import logging
logger = logging.getLogger(__name__)

class MesaService:
    __mesa: Ubicacion
    def __init__(self):
        self.__mesa = Ubicacion

    def get_mesas(self):
        mesas = Ubicacion.objects.all()
        return mesas
    
    def crear_mesas_interior(self, numero: int):
        for i in range(numero):
            logger.info(f"Creando mesa interior {i}")
            Ubicacion.objects.create(lugar="Interior")

    def crear_mesas_terraza(self, numero: int):
        for i in range(numero):
            Ubicacion.objects.create(lugar="Exterior")

    def get_mesas_interior(self):
        mesas = Ubicacion.objects.filter(lugar="Interior")
        return mesas

    def get_mesas_terraza(self):
        mesas = Ubicacion.objects.filter(lugar="Exterior")
        return mesas

    def eliminar_mesas_interior(self, numero: int):
        mesas = Ubicacion.objects.filter(lugar="Interior")
        for i in range(numero):
            mesas[i].delete()

    def eliminar_mesas_terraza(self, numero: int):
        mesas = Ubicacion.objects.filter(lugar="Exterior")
        for i in range(numero):
            mesas[i].delete()