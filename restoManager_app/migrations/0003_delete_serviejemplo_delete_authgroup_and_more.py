# Generated by Django 5.0.1 on 2024-03-10 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restoManager_app', '0002_rename_camarero_serviejemplo_camarero'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServiEjemplo',
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='BebidasNoAlcoholicas',
        ),
        migrations.DeleteModel(
            name='Camarero',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='Mesa',
        ),
        migrations.DeleteModel(
            name='Platos',
        ),
        migrations.DeleteModel(
            name='Servicio',
        ),
    ]
