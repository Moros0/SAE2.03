# Generated by Django 4.2.1 on 2023-05-28 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projetApp', '0028_machine_adresse_ip_machine_masque_alter_machine_mach'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='machine_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projetApp.machine'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('Mac', 'Mac - MacOS'), ('PC', 'PC - Windows'), ('Switch', 'Switch'), ('Serveur', 'Serveur')], default='PC', max_length=32),
        ),
    ]
