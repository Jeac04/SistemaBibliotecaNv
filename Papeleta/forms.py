from django import forms
from .models import PapeletaPrestamo

class PapeletaPrestamoForm(forms.ModelForm):
    class Meta:
        model = PapeletaPrestamo
        fields = []
