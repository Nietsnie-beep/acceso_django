# Generated by Django 4.1.7 on 2023-03-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0003_alter_persona_estatus_alter_visita_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='fecha',
            field=models.CharField(default='', max_length=50),
        ),
    ]
