# Generated by Django 4.1.7 on 2023-02-16 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Correctif', '0003_ordre_pointage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Avis',
        ),
        migrations.DeleteModel(
            name='Ordre',
        ),
        migrations.DeleteModel(
            name='Pointage',
        ),
    ]