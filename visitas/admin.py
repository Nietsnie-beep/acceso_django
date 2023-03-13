from django.contrib import admin

# Register your models here.
from .models import Visita, Persona, VisitasProgramadas

admin.site.register(Visita)
admin.site.register(Persona)
admin.site.register(VisitasProgramadas)
