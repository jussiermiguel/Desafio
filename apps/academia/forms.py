from django import forms
from .models import AlunoAcademia

class AlunoAcademiaForm(forms.ModelForm):
    class Meta:
        model = AlunoAcademia
        fields = '__all__'
