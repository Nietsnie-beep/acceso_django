import django_filters
from .models import Visita, Persona

class SnippetFilter(django_filters.FilterSet):
    class Meta:
        model = Visita
        fields = ('persona', 'empresa','Estatus' )

class SnippetFilterPersona(django_filters.FilterSet):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido','empresa' )