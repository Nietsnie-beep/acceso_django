# Generated by Django 4.1.7 on 2023-03-09 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0010_remove_visita_persona_actual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='placa',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
