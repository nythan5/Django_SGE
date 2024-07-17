from django import forms
from .models import Inflow


class InflowForm(forms.ModelForm):
    class Meta:
        model = Inflow
        fields = ['product', 'supplier', 'quantity', 'description']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'product': 'Produto',
            'description': 'Descrição',
            'quantity': 'Quantidade',
            'supplier': 'Fornecedor'
        }
