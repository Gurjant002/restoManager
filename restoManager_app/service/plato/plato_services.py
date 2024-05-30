from django.db.models import QuerySet
from restoManager_app.models import Plato

class PlatoService:
    """Clase que implementa servicios para el modelo Plato
    
    """
    _platos: QuerySet[Plato]

    def __init__(self):
        self._platos = Plato.objects.all()

    def get_platos(self) -> QuerySet[Plato]:
        """Obtiene todos los platos
        
        Returns:
            QuerySet[Plato]: lista de platos
        """
        return self._platos.order_by('nombre')

    def get_plato_by_name(self, nombre_plato: str) -> Plato | None:
        """Obtiene un plato por su nombre
        
        Args:
            nombrePlato (str): nombre del plato
        
        Returns:
            Plato | None: el plato o None si no existe
        """
        return self._platos.filter(nombre=nombre_plato).first()
    
    def get_plato_by_id(self, id_plato) -> Plato | None:
        """Obtiene un plato por su id
        
        Args:
            id_plato: id del plato
        
        Returns:
            Plato | None: el plato o None si no existe
        """
        return self._platos.filter(id=id_plato).first()

    def crear_plato(self, nombrePlato: str, descripcion: str) -> Plato:
        """Crea un nuevo plato
        
        Args:
            nombrePlato (str): nombre del plato
            descripcion (str): descripcion del plato
        
        Returns:
            Plato: el plato creado
        """
        return Plato.objects.create(nombre=nombrePlato, descripcion=descripcion)

    def actualizar_plato(self, id_plato: int, nombre_plato: str, descripcion_plato: str) -> int:
        """Actualiza un plato
        
        Args:
            id_plato (int): id del plato
            nombre_plato (str): nuevo nombre del plato
            descripcion_plato (str): nueva descripcion del plato
        
        Returns:
            int: numero de filas afectadas
        """
        return Plato.objects.filter(id=id_plato).update(nombre=nombre_plato, descripcion=descripcion_plato)

    def eliminar_plato(self, id_plato) -> int:
        """Elimina un plato
        
        Args:
            id_plato: id del plato
        
        Returns:
            int: numero de filas afectadas
        """
        return Plato.objects.filter(id=id_plato).delete()
