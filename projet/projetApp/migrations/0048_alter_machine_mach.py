# Generated by Django 4.2.1 on 2023-06-07 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetApp', '0047_alter_machine_mach_alter_machine_personnel_assoc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('PC', 'PC - Windows'), ('Mac', 'Mac - MacOS'), ('Switch', 'Switch'), ('Routeur', 'Routeur'), ('Serveur', 'Serveur')], default='PC', max_length=32),
        ),
    ]
