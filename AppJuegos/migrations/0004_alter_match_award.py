# Generated by Django 4.1.1 on 2022-12-31 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppJuegos', '0003_remove_match_date_modified_remove_match_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='award',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='award', to='AppJuegos.award'),
        ),
    ]