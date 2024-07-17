from django import forms
from .models import Outflow


class OutflowForm(forms.ModelForm):
    class Meta:
        model = Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'product': 'Produto',
            'description': 'Descrição',
            'quantity': 'Quantidade',

        }
