from django import forms
from .models import Persona, Visita, VisitasProgramadas



class PersonaPost(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido']

#####################
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'empresa', 'Estatus']

class PersonaFormTwo(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['Estatus','Solicitante']


class VisitaFormCarro(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['persona', 'motivo', 'placa', 'carro']

class VisitaFormPeaton(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['persona', 'motivo']

class VisitaFormExit(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['Estatus']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['persona', 'placa', 'carro', 'motivo', 'persona_visita', 'foto_1']
        # motivo = forms.IntegerField(widget=forms.HiddenInput())
        widgets = {
            'placa':forms.TextInput(attrs={'required': False})
        }

class scheduled_visits(forms.ModelForm):
    class Meta:
        model = VisitasProgramadas
        fields = ['persona', 'fecha', 'empresa', 'motivo','persona_visita']
        # motivo = forms.IntegerField(widget=forms.HiddenInput())
        widgets = {
            'fecha':forms.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
        
        }


class CreatePersonFoto(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'empresa', 'foto_1']
        # motivo = forms.IntegerField(widget=forms.HiddenInput())
        widgets = {
            'placa':forms.TextInput(attrs={'required': False})
        }