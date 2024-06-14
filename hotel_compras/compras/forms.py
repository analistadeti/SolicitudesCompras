from django import forms
from .models import SolicitudCompra, EstadoCompra

class SolicitudCompraForm(forms.ModelForm):
    class Meta:
        model = SolicitudCompra
        fields = ['descripcion']

class EstadoCompraForm(forms.ModelForm):
    class Meta:
        model = EstadoCompra
        fields = ['estado']
