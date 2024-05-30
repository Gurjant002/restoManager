from django.db import models
from restoManager_app.models import Rol, Ubicacion

"""
Clase Camarero_Mesa
"""
class Camarero_Mesa(models.Model):
    """
    Clase que representa la relación entre un camarero y una mesa.
    """
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True)
    numero_mesa = models.IntegerField(null=True, blank=False, unique=False)

    def __str__(self):
        """
        Método que devuelve una representación en string de la instancia.
        """
        return f'rol: {self.rol} ubicacion: {self.ubicacion} numero_mesa: {self.numero_mesa}'

    class Meta:
        db_table = 'camarero_mesa'
        managed = True
        verbose_name = 'Camarero_Mesa'
        verbose_name_plural = 'Camarero_Mesas'

