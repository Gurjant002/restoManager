from django.db import models
from restoManager_app.models import Camarero, Ubicacion
# Create your models here.

class Camarero_Mesa(models.Model):
    camarero = models.ForeignKey(Camarero, on_delete=models.DO_NOTHING)
    mesa = models.ForeignKey(Ubicacion, on_delete=models.DO_NOTHING)
    numero_mesa = models.IntegerField(null=True, default=None, blank=True)

    def __str__(self):
        return f'camarero: {self.camarero} mesa: {self.mesa}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Camarero_Mesa'
        verbose_name_plural = 'Camarero_Mesas'
