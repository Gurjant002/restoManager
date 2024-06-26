# Generated by Django 5.0.1 on 2024-05-16 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField()),
                ('contiene_alcohol', models.BooleanField(default=False)),
                ('estado', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'verbose_name': 'Bebida',
                'verbose_name_plural': 'Bebidas',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Camarero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('fecha_alta_camarero', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Camarero',
                'verbose_name_plural': 'Camareros',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(choices=[('0', 'Interior'), ('1', 'Exterior')], max_length=20)),
            ],
            options={
                'verbose_name': 'Mesa',
                'verbose_name_plural': 'Mesas',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Plato',
                'verbose_name_plural': 'Platos',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Plato_Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_menu', models.IntegerField(unique=True)),
                ('habilitado', models.BooleanField(blank=True, default=True, null=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='restoManager_app.categoria')),
                ('plato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restoManager_app.plato')),
            ],
            options={
                'verbose_name': 'Plato_Categoria',
                'verbose_name_plural': 'Plato_Categorias',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
