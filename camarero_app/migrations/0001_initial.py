# Generated by Django 5.0.1 on 2024-05-16 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restoManager_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camarero_Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_mesa', models.IntegerField(blank=True, default=None, null=True)),
                ('camarero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restoManager_app.camarero')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restoManager_app.mesa')),
            ],
            options={
                'verbose_name': 'Camarero_Mesa',
                'verbose_name_plural': 'Camarero_Mesas',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
