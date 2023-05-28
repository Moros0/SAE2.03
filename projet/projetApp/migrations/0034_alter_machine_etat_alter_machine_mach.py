# Generated by Django 4.2.1 on 2023-05-28 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetApp', '0033_alter_machine_etat_alter_machine_mach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='etat',
            field=models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], default='Offline', max_length=32),
        ),
        migrations.AlterField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('Mac', 'Mac - MacOS'), ('Serveur', 'Serveur'), ('Switch', 'Switch'), ('PC', 'PC - Windows')], default='PC', max_length=32),
        ),
    ]
