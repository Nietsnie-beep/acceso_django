# Generated by Django 4.1.7 on 2023-03-10 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0016_visitasprogramadas_persona_visita'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='foto_1',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='visitasprogramadas',
            name='Estatus',
            field=models.CharField(default='Pendiente', max_length=50),
        ),
    ]
