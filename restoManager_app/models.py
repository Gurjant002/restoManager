"""
Este es un módulo de modelo de Django generado automáticamente.
Tiene que ser limpiado manualmente:
    * Ordenar los modelos
    * Asegurarse de que cada modelo tenga un campo con primary_key=True
    * Asegurarse de que cada ForeignKey y OneToOneField tenga on_delete establecido en el comportamiento deseado
    * Quitar las líneas 'managed = False' si desea que Django cree, modifique y elimine la tabla
Feel free to rename the models, but don't rename db_table values or field names.
"""

from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    """
    Modelo de la categoría de los platos.
    """
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    def get_by_name(self, name:str):
        return self.objects.filter(nombre=name)

    def get_all_categorias(self):
        return self.objects.all()

    class Meta:
        db_table = 'categoria'
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Plato(models.Model):
    """
    Modelo de los platos.
    """
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    def get_by_name(self, name:str):
        return self.objects.filter(nombre=name)

    def get_all_plato():
        return Plato.objects.all()

    class Meta:
        db_table = 'plato'
        managed = True
        verbose_name = 'Plato'
        verbose_name_plural = 'Platos'

class Ubicacion(models.Model):
    """
    Modelo de la ubicación de los restaurantes.
    """
    lugar = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'Lugar: {self.lugar}'

    class Meta:
        db_table = 'ubicacion'
        managed = True
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'

class Bebida(models.Model):
    """
    Modelo de las bebidas.
    """
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField()
    contiene_alcohol = models.BooleanField(default=False)
    estado = models.BooleanField(blank=True, null=True, default=True)

    def __str__(self):
        return f'Nombre Categoria: {self.nombre}, Descripcion: {self.descripcion}, Contiene Alcohol: {self.contiene_alcohol}, Estado: {self.estado}'

    class Meta:
        db_table = 'bebida'
        managed = True
        verbose_name = 'Bebida'
        verbose_name_plural = 'Bebidas'

class Plato_Categoria(models.Model):
    """
    Modelo de la relación entre un plato y una categoría.
    """
    numero_menu = models.IntegerField(unique=True)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True)
    habilitado = models.BooleanField(blank=True, null=True, default=True)

    def __str__(self):
        return f'Numero de menu: {self.numero_menu}, Plato: {self.plato}, Categoría: {self.categoria}, Habilitado: {self.habilitado}'

    class Meta:
        db_table = 'plato_categoria'
        managed = True
        verbose_name = 'Plato_Categoria'
        verbose_name_plural = 'Plato_Categorias'

class Rol(models.Model):
    """
    Modelo del rol de usuario.
    """
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    rol = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'user {self.user} con rol {self.rol}'
    
    class Meta:
        db_table = 'rol'
        managed = True
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

