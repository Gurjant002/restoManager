# Generated by Django 5.0.1 on 2024-05-18 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camarero_app', '0002_remove_camarero_mesa_mesa_camarero_mesa_ubicacion_and_more'),
        ('restoManager_app', '0005_alter_ubicacion_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camarero_mesa',
            name='camarero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restoManager_app.camarero'),
        ),
        migrations.AlterField(
            model_name='camarero_mesa',
            name='ubicacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restoManager_app.ubicacion'),
        ),
    ]