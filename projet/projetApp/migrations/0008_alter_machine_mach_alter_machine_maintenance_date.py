# Generated by Django 4.2.1 on 2023-05-21 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetApp', '0007_alter_machine_mach_alter_machine_maintenance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('Serveur', 'Serveur'), ('PC', 'PC - Windows'), ('Mac', 'Mac - MacOS'), ('Switch', 'Switch')], default='PC', max_length=32),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenance_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 21, 12, 58, 20, 226023)),
        ),
    ]
