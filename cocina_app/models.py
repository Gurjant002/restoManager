# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from restoManager_app.models import Camarero, Mesa, Plato, Bebida

class Camarero_Mesa(models.Model):
    camarero = models.ForeignKey(Camarero, on_delete=models.DO_NOTHING)
    mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Camarero_Mesa'
        verbose_name_plural = 'Camarero_Mesas'

class Servicio_Cocina(models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.DO_NOTHING)
    servido = models.BooleanField(default=False)
    camarero_mesa = models.ForeignKey(Camarero_Mesa, on_delete=models.DO_NOTHING)
    hora_dia = models.DateTimeField()

    def __str__(self):
        pass
 
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Servicio_Cocina'
        verbose_name_plural = 'Servicio_Cocinas'

class Servicio_Barra(models.Model):
    bebida = models.ForeignKey(Bebida, on_delete=models.DO_NOTHING)
    servido = models.BooleanField(default=False)
    camarero_mesa = models.ForeignKey(Camarero_Mesa, on_delete=models.DO_NOTHING)
    hora_dia = models.DateTimeField()

    def __str__(self):
        pass
 
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Servicio_Barra'
        verbose_name_plural = 'Servicio_Barras'