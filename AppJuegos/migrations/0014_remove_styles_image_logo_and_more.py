# Generated by Django 4.1.1 on 2024-08-13 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppJuegos', '0013_rename_image_logo_tragamoneda_styles_image_logo_tragamonedas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='styles',
            name='image_logo',
        ),
        migrations.AddField(
            model_name='styles',
            name='image_background_kiosco',
            field=models.ImageField(null=True, upload_to='design/', verbose_name='imagen fondo Kiosco'),
        ),
        migrations.AddField(
            model_name='styles',
            name='image_logo_kiosco',
            field=models.ImageField(null=True, upload_to='design/', verbose_name='imagen logo Kiosco'),
        ),
        migrations.AlterField(
            model_name='styles',
            name='description_winner',
            field=models.CharField(default='¡HAS GANADO!', max_length=200, null=True, verbose_name='descripción ganador juego'),
        ),
        migrations.AlterField(
            model_name='styles',
            name='image_machine_game',
            field=models.ImageField(null=True, upload_to='design/', verbose_name='imagen máquina tragamonedas'),
        ),
        migrations.AlterField(
            model_name='styles',
            name='scan_code_description',
            field=models.CharField(default='Puedes escanear el código QR de tu ticket', max_length=200),
        ),
        migrations.AlterField(
            model_name='styles',
            name='scan_code_title',
            field=models.CharField(default='Escanear Código', max_length=200),
        ),
        migrations.AlterField(
            model_name='styles',
            name='title_button_screensaver',
            field=models.CharField(max_length=100, null=True, verbose_name='título botón salvapantallas'),
        ),
        migrations.AlterField(
            model_name='styles',
            name='title_winner',
            field=models.CharField(default='¡JUEGA OTRA VEZ!', max_length=150, null=True, verbose_name='título del ganador'),
        ),
    ]
