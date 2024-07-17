from django import forms
from .models import Outflow
from django.core.exceptions import ValidationError


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

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade disponivel em estoque para o produto {product.title} é de {product.quantity} unidades.')

        return quantity
