# Generated by Django 5.0.6 on 2024-05-25 20:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocina_app', '0010_alter_servicio_cocina_hora_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio_cocina',
            name='hora_dia',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 25, 20, 11, 28, 753047)),
        ),
    ]
