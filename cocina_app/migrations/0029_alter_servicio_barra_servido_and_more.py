# Generated by Django 5.0.6 on 2024-05-29 23:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocina_app', '0028_alter_servicio_cocina_hora_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio_barra',
            name='servido',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='servicio_cocina',
            name='hora_dia',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 23, 21, 25, 195074, tzinfo=datetime.timezone.utc)),
        ),
    ]
