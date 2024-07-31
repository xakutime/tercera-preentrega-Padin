from django import forms
from .models import Alumno, Profesor, Receta

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'comision']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'comision']

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre_receta', 'alumno', 'ingredientes']