# Generated by Django 4.2.1 on 2023-05-28 11:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetApp', '0025_alter_machine_mach'),
    ]

    operations = [
        migrations.AddField(
            model_name='reseau',
            name='masque',
            field=models.CharField(default=0, max_length=15, validators=[django.core.validators.validate_ipv4_address]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='machine',
            name='etat',
            field=models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], default='Offline', max_length=32),
        ),
        migrations.AlterField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('Mac', 'Mac - MacOS'), ('Switch', 'Switch'), ('PC', 'PC - Windows'), ('Serveur', 'Serveur')], default='PC', max_length=32),
        ),
    ]
