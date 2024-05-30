"""
Módulo de modelos para la aplicación de cocina.
"""

from django.utils import timezone
from django.db import models

from restoManager_app.models import Ubicacion, Plato, Bebida
from camarero_app.models import Camarero_Mesa


class Servicio_Cocina(models.Model):
    """
    Modelo para un servicio de cocina.
    """
    plato = models.ForeignKey(Plato, null=True, default=None, on_delete=models.DO_NOTHING)
    servido = models.BooleanField(null=True, default=None)
    camarero_mesa = models.ForeignKey(Camarero_Mesa, on_delete=models.DO_NOTHING)
    hora_dia = models.DateTimeField(null=False, default=timezone.now())

    def __str__(self):
        """
        Devuelve una cadena con la representación en string del servicio de cocina.
        """
        return f'plato {self.plato} servido: {self.servido} mesa: {self.camarero_mesa} hora: {self.hora_dia}'

    class Meta:
        db_table = 'servicio_cocina'
        managed = True
        verbose_name = 'Servicio_Cocina'
        verbose_name_plural = 'Servicio_Cocinas'


class Servicio_Barra(models.Model):
    """
    Modelo para un servicio en la barra.
    """
    bebida = models.ForeignKey(Bebida, on_delete=models.DO_NOTHING)
    servido = models.BooleanField(default=None, null=True)
    camarero_mesa = models.ForeignKey(Camarero_Mesa, on_delete=models.DO_NOTHING)
    hora_dia = models.DateTimeField()

    def __str__(self):
        """
        Devuelve una cadena con la representación en string del servicio en la barra.
        """
        return f'bebida {self.bebida} servido: {self.servido} mesa: {self.camarero_mesa} hora: {self.hora_dia}'

    class Meta:
        db_table = 'servicio_barra'
        managed = True
        verbose_name = 'Servicio_Barra'
        verbose_name_plural = 'Servicio_Barras'
