# Generated by Django 4.2.1 on 2023-05-28 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projetApp', '0022_alter_machine_etat_alter_machine_mach_and_more'),
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
            field=models.CharField(choices=[('Serveur', 'Serveur'), ('Switch', 'Switch'), ('PC', 'PC - Windows'), ('Mac', 'Mac - MacOS')], default='PC', max_length=32),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenance_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
