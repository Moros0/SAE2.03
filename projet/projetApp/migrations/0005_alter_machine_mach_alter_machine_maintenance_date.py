# Generated by Django 4.2.1 on 2023-05-15 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetApp', '0004_alter_machine_maintenance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('Switch', 'Switch'), ('Serveur', 'Serveur'), ('Mac', 'Mac - MacOS'), ('PC', 'PC - Windows')], default='PC', max_length=32),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenance_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 15, 18, 54, 18, 896039)),
        ),
    ]
