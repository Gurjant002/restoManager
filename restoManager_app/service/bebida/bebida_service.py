from restoManager_app.models import Bebida

class BebidaService:
    def __init__(self):
        pass

    def get_bebida_by_name(self, nombre_bebida: str) -> list:
        bebida = Bebida.objects.filter(nombre=nombre_bebida).first()
        return bebida

    def get_bebidas(self) -> list:
        bebidas = Bebida.objects.all()
        return bebidas

    def get_bebida_by_id(self, id_bebida: str) -> list:
        bebida = Bebida.objects.filter(id=id_bebida).first()
        return bebida

    def crear_bebida(self, nombre_bebida: str, contiene_alcohol: int, estado: int, descripcion: str) -> list:
        bebida = Bebida.objects.create(
            nombre=nombre_bebida,
            contiene_alcohol=contiene_alcohol,
            estado=estado,
            descripcion=descripcion
            )
        return bebida
    
    def actualizar_bebida(self, id_bebida: str, nombre_bebida: str, contiene_alcohol: int, estado: int, descripcion: str) -> list:
        bebida = Bebida.objects.filter(id=id_bebida).update(
            nombre=nombre_bebida,
            contiene_alcohol=contiene_alcohol,
            estado=estado,
            descripcion=descripcion
            )
        return bebida

    def eliminar_bebida(self, id_bebida) -> list:
        bebida = Bebida.objects.filter(id=id_bebida).delete()
        return bebida
