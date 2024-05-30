from django.db.models import QuerySet
from restoManager_app.models import Bebida

class BebidaService:
    """
    Servicio para las bebidas del restaurante
    """
    def __init__(self):
        pass

    def get_bebida_by_name(self, nombre_bebida: str) -> QuerySet:
        """
        Obtiene una bebida por su nombre

        :param nombre_bebida: El nombre de la bebida
        :type nombre_bebida: str
        :return: Un objeto de la clase Bebida
        :rtype: Bebida
        """
        bebida = Bebida.objects.filter(nombre=nombre_bebida).first()
        return bebida

    def get_bebidas(self) -> QuerySet:
        """
        Obtiene todas las bebidas del restaurante

        :return: Una lista de objetos de la clase Bebida
        :rtype: list(Bebida)
        """
        bebidas = Bebida.objects.all()
        return bebidas

    def get_bebida_by_id(self, id_bebida: str) -> QuerySet:
        """
        Obtiene una bebida por su id

        :param id_bebida: El id de la bebida
        :type id_bebida: str
        :return: Un objeto de la clase Bebida
        :rtype: Bebida
        """
        bebida = Bebida.objects.filter(id=id_bebida).first()
        return bebida

    def crear_bebida(self, nombre_bebida: str, contiene_alcohol: int, estado: int, descripcion: str) -> Bebida:
        """
        Crea una nueva bebida en la base de datos

        :param nombre_bebida: El nombre de la bebida
        :type nombre_bebida: str
        :param contiene_alcohol: Si la bebida contiene alcohol
        :type contiene_alcohol: int
        :param estado: El estado de la bebida
        :type estado: int
        :param descripcion: La descripcion de la bebida
        :type descripcion: str
        :return: Un objeto de la clase Bebida
        :rtype: Bebida
        """
        bebida = Bebida.objects.create(
            nombre=nombre_bebida,
            contiene_alcohol=contiene_alcohol,
            estado=estado,
            descripcion=descripcion
            )
        return bebida
    
    def actualizar_bebida(self, id_bebida: str, nombre_bebida: str, contiene_alcohol: int, estado: int, descripcion: str) -> int:
        """
        Actualiza una bebida en la base de datos

        :param id_bebida: El id de la bebida
        :type id_bebida: str
        :param nombre_bebida: El nombre de la bebida
        :type nombre_bebida: str
        :param contiene_alcohol: Si la bebida contiene alcohol
        :type contiene_alcohol: int
        :param estado: El estado de la bebida
        :type estado: int
        :param descripcion: La descripcion de la bebida
        :type descripcion: str
        :return: El numero de filas afectadas
        :rtype: int
        """
        bebida = Bebida.objects.filter(id=id_bebida).update(
            nombre=nombre_bebida,
            contiene_alcohol=contiene_alcohol,
            estado=estado,
            descripcion=descripcion
            )
        return bebida

    def eliminar_bebida(self, id_bebida) -> int:
        """
        Elimina una bebida de la base de datos

        :param id_bebida: El id de la bebida
        :type id_bebida: str
        :return: El numero de filas afectadas
        :rtype: int
        """
        bebida = Bebida.objects.filter(id=id_bebida).delete()
        return bebida

