# Generated by Django 4.1.7 on 2023-03-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0007_visita_persona_visita'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='persona_actual',
            field=models.CharField(default='', max_length=50),
        ),
    ]