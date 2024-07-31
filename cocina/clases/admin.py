from django.contrib import admin
from .models import Alumno, Profesor, Receta

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'comision')
    search_fields = ('nombre',)

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'comision')
    search_fields = ('nombre',)

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'alumno', 'ingredientes')
    search_fields = ('nombre', 'alumno__nombre')