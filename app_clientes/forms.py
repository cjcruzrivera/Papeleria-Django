from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields=[
            'identificacion',
            'nombre',
            'apellidos',
            'sexo',
            'telefono',
            'fecha_nacimiento',
        ]

        labels={
            'identificacion':'ID',
            'nombre':'Nombre',
            'apellidos':'Apellidos',
            'sexo':'Sexo',
            'telefono':'Telefono',
            'fecha_nacimiento':'Fecha de Nacimiento',
        }


        widgets={
            'identificacion': forms.TextInput(attrs={'class':'form-control','id':'id', 'placeholder': 'Ingrese la identificacion del cliente'}),
            'nombre':forms.TextInput(attrs={'class':'form-control','id':'nombre', 'placeholder': 'Ingrese el nombre del cliente'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control','id':'apellidos', 'placeholder': 'Ingrese los apellidos del cliente'}),
            'sexo':forms.Select(attrs={'class':'form-control','id':'sexo'}),
            'telefono':forms.TextInput(attrs={'class':'form-control','id':'telefono', 'placeholder': 'Ingrese el telefono del cliente'}),
            'fecha_nacimiento':forms.DateInput(attrs={'class':'form-control','id':'fecha',}),
        }


