from django.db import models
from .utils import get_filtered_image
from PIL import Image
import numpy as np
from django.core.files.base import ContentFile


from datetime import date

class Persona(models.Model):
    ESTADO = (
        ("ACTIVO", 'activo'),
        ("BETADO", 'Betado')
    )
    id = models.AutoField(primary_key=True)

    nombre = models.CharField(
        max_length=50,
        default='',
        null=True
    )
    apellido = models.CharField(
        max_length=50,
        default=''
    )
    empresa = models.CharField(
            max_length=50,
            default='',
            null=True
        )
    Estatus = models.CharField(
        max_length=50,
        choices=ESTADO,
        default='ACTIVO'
    )

    Solicitante = models.CharField(
        max_length=50,
        default='',
        null=True
    )

    foto_1 = models.ImageField(upload_to='uploads/', null=True, blank=True)


    def __str__(self):
        return self.nombre + ' ' + self.apellido
  

class Visita(models.Model):
    id = models.AutoField(primary_key=True)

    persona = models.ForeignKey(Persona, null=True, on_delete=models.SET_NULL)

    empresa = models.CharField(
        max_length=50,
        default='',
        null=True
    )

    carro = models.BooleanField(default=False   )

    motivo = models.CharField(
        max_length=50,
        default=''
    )
    Estatus = models.CharField(
        max_length=50,
        default='Entro'
    )

    placa = models.CharField(
        max_length= 50,
        default='',
        null=True,
        blank=True
    )

    fecha = models.CharField(
        max_length= 50,
        default=''
    )

    persona_visita = models.CharField(
        max_length= 50,
        default=''
    )

    
    empresa = models.CharField(max_length=50, default='', null=True)
    foto_1 = models.ImageField(upload_to='uploads/', null=True, blank=True)
    foto_2 = models.ImageField(upload_to='uploads/', null=True)


    def save(self,*args, **kwargs ):
        today = date.today()
        self.fecha = today
        super().save(*args, **kwargs)


    def __str__(self):
        return self.persona.nombre
    

class VisitasProgramadas(models.Model):
    id = models.AutoField(primary_key=True)

    persona = models.ForeignKey(Persona, null=True, on_delete=models.SET_NULL)

    empresa = models.CharField(
        max_length=50,
        default='',
        null=True
    )

    carro = models.BooleanField(default=False)

    motivo = models.CharField(
        max_length=50,
        default=''
    )

    Estatus = models.CharField(
        max_length=50,
        default='Pendiente'
    )

    placa = models.CharField(
        max_length= 50,
        default=''
    )
    persona_visita = models.CharField(
        max_length= 50,
        default=''
    )
    fecha = models.DateField()
    

    empresa = models.CharField(max_length=50, default='', null=True)
    foto_1 = models.ImageField(upload_to='uploads/', null=True)
    foto_2 = models.ImageField(upload_to='uploads/', null=True)


    def __str__(self):
        return self.persona.nombre