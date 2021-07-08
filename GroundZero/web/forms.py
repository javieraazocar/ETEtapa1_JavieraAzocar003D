from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Proovedor

class ProovedorForm(forms.ModelForm):

    class Meta:
        model = Proovedor
        fields = ['id','nomCompleto','telefono','direccion','email','pais','contra','img']

        labels ={
            'id': 'Identificador',
            'nomCompleto': 'Nombre Completo',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'email': 'Email',
            'pais': 'pais',
            'contra': 'Contrasenna',
            'moneda': 'Moneda',
        }

        widgets = {
            'id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número identificador',
                    'id':'id'
                }
            ),
            'nomCompleto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre completo',
                    'id':'nomCompleto'
                }
            ),
            'email': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'usuario@dominio.com',
               'id':'email'
            }
         ),
         'telefono': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': '+56 9 xxxx xxxx',
               'id':'telefono'
            }
         ),
         'direccion': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'Dirección',
               'id':'direccion'
            }
         ),
         'pais': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'País',
               'id':'pais'
            }
         ),
         'moneda': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'Ingrese tipo de moneda',
               'id':'moneda'
            }
         ),
         'contrasenna': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'Ingrese Contraseña',
               'id':'password'
            }
         ),
        }
    
        img = forms.ImageField(label='Imagen',widget=forms.ClearableFileInput(
            attrs={
                'class':'form_control'
            }
        ))
