# Generated by Django 5.0.1 on 2024-05-19 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restoManager_app', '0011_alter_camarero_id_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='camarero',
            old_name='id_user',
            new_name='user',
        ),
    ]
