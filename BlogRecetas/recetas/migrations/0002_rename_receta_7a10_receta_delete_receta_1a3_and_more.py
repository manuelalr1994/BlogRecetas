# Generated by Django 4.0.5 on 2022-07-03 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='receta_7a10',
            new_name='Receta',
        ),
        migrations.DeleteModel(
            name='receta_1a3',
        ),
        migrations.DeleteModel(
            name='receta_4a6',
        ),
    ]
