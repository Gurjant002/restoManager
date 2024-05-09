from restoManager_app.models import Mesa
import logging
logger = logging.getLogger(__name__)

class MesaService:
    __mesa: Mesa
    def __init__(self):
        self.__mesa = Mesa

    def get_mesas(self):
        mesas = Mesa.objects.all()
        return mesas
    
    def crear_mesas_interior(self, numero: int):
        for i in range(numero):
            logger.info(f"Creando mesa interior {i}")
            Mesa.objects.create(lugar="Interior")

    def crear_mesas_terraza(self, numero: int):
        for i in range(numero):
            Mesa.objects.create(lugar="Exterior")

    def eliminar_mesas_interior(self, numero: int):
        mesas = Mesa.objects.filter(lugar="Interior")
        for i in range(numero):
            mesas[i].delete()

    def eliminar_mesas_terraza(self, numero: int):
        mesas = Mesa.objects.filter(lugar="Exterior")
        for i in range(numero):
            mesas[i].delete()