# Generated by Django 4.1.1 on 2024-07-23 14:45

from django.db import migrations, models
import AppJuegos.choices as ch

class Migration(migrations.Migration):

    dependencies = [
        ('AppJuegos', '0008_alter_gameimageupload_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(choices=ch.GAME_CHOICES, default='Dados', max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='historicalgame',
            name='name',
            field=models.CharField(choices=ch.GAME_CHOICES, default='Dados', max_length=50, verbose_name='Nombre'),
        ),
    ]
