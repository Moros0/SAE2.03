# Generated by Django 4.2.1 on 2023-06-07 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projetApp', '0044_alter_machine_mach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('Switch', 'Switch'), ('PC', 'PC - Windows'), ('Routeur', 'Routeur'), ('Serveur', 'Serveur'), ('Mac', 'Mac - MacOS')], default='PC', max_length=32),
        ),
        migrations.AlterField(
            model_name='machine',
            name='personnel_assoc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetApp.personnel'),
        ),
        migrations.RemoveField(
            model_name='personnel',
            name='machine_assoc',
        ),
        migrations.AddField(
            model_name='personnel',
            name='machine_assoc',
            field=models.ManyToManyField(to='projetApp.machine'),
        ),
    ]
