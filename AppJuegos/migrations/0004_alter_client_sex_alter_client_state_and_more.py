# Generated by Django 4.1.1 on 2022-10-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppJuegos', '0003_gamedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='sex',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=50, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='client',
            name='state',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=50, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='historicalclient',
            name='sex',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=50, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='historicalclient',
            name='state',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=50, verbose_name='Estado'),
        ),
    ]
