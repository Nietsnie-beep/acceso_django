# Generated by Django 4.1.7 on 2023-03-09 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0009_alter_visita_persona_actual'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visita',
            name='persona_actual',
        ),
    ]
