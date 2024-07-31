from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alumno/add/', views.alumno_create, name='alumno_create'),
    path('profesor/add/', views.profesor_create, name='profesor_create'),
    path('receta/add/', views.receta_create, name='receta_create'),
    path('buscar/', views.buscar, name='buscar'),
]