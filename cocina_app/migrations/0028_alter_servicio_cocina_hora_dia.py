# Generated by Django 5.0.6 on 2024-05-29 21:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocina_app', '0027_alter_servicio_cocina_hora_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio_cocina',
            name='hora_dia',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 21, 37, 46, 444085, tzinfo=datetime.timezone.utc)),
        ),
    ]
