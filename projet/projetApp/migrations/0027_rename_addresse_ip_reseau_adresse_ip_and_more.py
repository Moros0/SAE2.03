# Generated by Django 4.2.1 on 2023-05-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetApp', '0026_reseau_masque_alter_machine_etat_alter_machine_mach'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reseau',
            old_name='addresse_ip',
            new_name='adresse_ip',
        ),
        migrations.AlterField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('Switch', 'Switch'), ('Serveur', 'Serveur'), ('Mac', 'Mac - MacOS'), ('PC', 'PC - Windows')], default='PC', max_length=32),
        ),
    ]
