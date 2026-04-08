# Formularios de Django para gestionar Socios

from django import forms
from practico_05.ejercicio_01 import Socio


class SocioForm(forms.Form):
    """Formulario para crear/modificar un Socio"""
    
    dni = forms.IntegerField(
        label='DNI',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese DNI'
        })
    )
    
    nombre = forms.CharField(
        label='Nombre',
        max_length=250,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nombre'
        })
    )
    
    apellido = forms.CharField(
        label='Apellido',
        max_length=250,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese apellido'
        })
    )
    
    def clean_nombre(self):
        """Validación personalizada del nombre"""
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3 or len(nombre) > 15:
            raise forms.ValidationError('El nombre debe tener entre 3 y 15 caracteres.')
        return nombre
    
    def clean_apellido(self):
        """Validación personalizada del apellido"""
        apellido = self.cleaned_data['apellido']
        if len(apellido) < 3 or len(apellido) > 15:
            raise forms.ValidationError('El apellido debe tener entre 3 y 15 caracteres.')
        return apellido
