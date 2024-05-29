from django.db import models
from restoManager_app.models import Rol, Ubicacion
# Create your models here.

class Camarero_Mesa(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True)
    numero_mesa = models.IntegerField(null=True, blank=False, unique=False)

    def __str__(self):
        return f'rol: {self.rol} ubicacion: {self.ubicacion} numero_mesa: {self.numero_mesa}'

    class Meta:
        db_table = 'camarero_mesa'
        managed = True
        verbose_name = 'Camarero_Mesa'
        verbose_name_plural = 'Camarero_Mesas'
