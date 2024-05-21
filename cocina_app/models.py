# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from restoManager_app.models import Camarero, Ubicacion, Plato, Bebida
from camarero_app.models import Camarero_Mesa

class Servicio_Cocina(models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.DO_NOTHING)
    servido = models.BooleanField(default=False)
    camarero_mesa = models.ForeignKey(Camarero_Mesa, on_delete=models.DO_NOTHING)
    hora_dia = models.DateTimeField()

    def __str__(self):
        return f'plato {self.plato} servido: {self.servido} mesa: {self.camarero_mesa} hora: {self.hora_dia}'
 
    class Meta:
        db_table = 'servicio_cocina'
        managed = True
        verbose_name = 'Servicio_Cocina'
        verbose_name_plural = 'Servicio_Cocinas'

class Servicio_Barra(models.Model):
    bebida = models.ForeignKey(Bebida, on_delete=models.DO_NOTHING)
    servido = models.BooleanField(default=False)
    camarero_mesa = models.ForeignKey(Camarero_Mesa, on_delete=models.DO_NOTHING)
    hora_dia = models.DateTimeField()

    def __str__(self):
        return f'bebida {self.bebida} servido: {self.servido} mesa: {self.camarero_mesa} hora: {self.hora_dia}'
 
    class Meta:
        db_table = 'servicio_barra'
        managed = True
        verbose_name = 'Servicio_Barra'
        verbose_name_plural = 'Servicio_Barras'