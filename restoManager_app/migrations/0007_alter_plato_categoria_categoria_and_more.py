# Generated by Django 5.0.1 on 2024-03-16 00:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoManager_app', '0006_remove_categoria_descripcion_alter_plato_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato_categoria',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='restoManager_app.categoria'),
        ),
        migrations.AlterField(
            model_name='plato_categoria',
            name='plato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='restoManager_app.plato'),
        ),
    ]
