# Generated by Django 4.1.7 on 2023-03-10 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0014_alter_visita_fecha_alter_visitasprogramadas_placa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitasprogramadas',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='visitasprogramadas',
            name='placa',
            field=models.CharField(default='', max_length=50),
        ),
    ]