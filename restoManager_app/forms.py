from django import forms
from restoManager_app.models import Categoria

class NewPlato(forms.Form):
    plato = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Plato',
        'style': 'width: 300px;',
        'class': 'form-control'
        }))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.TextInput(attrs={
        'style': 'width: 300px;',
        'class': 'form-select',
        'aria-label': "Test",
        }))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Descripcion',
        'class': 'form-control'
        }))