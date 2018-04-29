
from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    
    class Meta():
        model = Producto

        fields = [
            'nombre',
            'descripcion',
            'precio_unitario',
        ]

        labels = {
            'nombre': 'PRODUCTO',
            'descripcion': 'DESCRIPCION',
            'precio_unitario': 'PRECIO (Por unidad en COP)',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class':'form-control',
                'id':'nombre',
                'placeholder':'Ingrese el nombre del producto',
            }),
            'descripcion': forms.TextInput(attrs={
                'class':'form-control',
                'id':'descripcion',
                'placeholder':'Ingrese la descripcion del producto',
            }),
            'precio_unitario': forms.NumberInput(attrs={
                'class':'form-control',
                'id':'precio_unitario',
                'placeholder':'Ingrese el precio del producto',
            }),
        }
        