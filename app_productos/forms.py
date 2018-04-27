
from django import forms

from .models import Producto


class ProductoCreateForm(forms.ModelForm):
    
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
            'precio_unitario': 'PRECIO',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class':'form-control',
                'id':'nombre',
                'placeholder':'Ingrese el nombre del producto',
            })
        }
        