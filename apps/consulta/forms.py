from django import forms
from .models import ConsultaNutricionista

class ConsultaNutricionistaForm(forms.ModelForm):
    class Meta:
        model = ConsultaNutricionista
        fields = '__all__'
