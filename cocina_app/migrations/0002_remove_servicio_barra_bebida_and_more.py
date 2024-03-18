# Generated by Django 5.0.1 on 2024-03-15 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocina_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio_barra',
            name='bebida',
        ),
        migrations.RemoveField(
            model_name='camarero_mesa',
            name='camarero',
        ),
        migrations.RemoveField(
            model_name='camarero_mesa',
            name='mesa',
        ),
        migrations.RemoveField(
            model_name='servicio_barra',
            name='camarero_mesa',
        ),
        migrations.RemoveField(
            model_name='servicio_cocina',
            name='camarero_mesa',
        ),
        migrations.RemoveField(
            model_name='servicio_cocina',
            name='plato',
        ),
        migrations.DeleteModel(
            name='Bebida',
        ),
        migrations.DeleteModel(
            name='Camarero',
        ),
        migrations.DeleteModel(
            name='Mesa',
        ),
        migrations.DeleteModel(
            name='Servicio_Barra',
        ),
        migrations.DeleteModel(
            name='Camarero_Mesa',
        ),
        migrations.DeleteModel(
            name='Plato',
        ),
        migrations.DeleteModel(
            name='Servicio_Cocina',
        ),
    ]
