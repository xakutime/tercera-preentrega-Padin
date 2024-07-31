from django.shortcuts import render, redirect
from .forms import AlumnoForm, ProfesorForm, RecetaForm
from .models import Alumno, Profesor, Receta

def index(request):
    return render(request, 'clases/index.html')

def alumno_create(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlumnoForm()
    return render(request, 'clases/alumno_form.html', {'form': form})

def profesor_create(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfesorForm()
    return render(request, 'clases/profesor_form.html', {'form': form})

def receta_create(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecetaForm()
    return render(request, 'clases/receta_form.html', {'form': form})

def buscar(request):
    query = request.GET.get('q')
    if query:
        alumnos = Alumno.objects.filter(nombre__icontains=query)
        recetas = Receta.objects.filter(alumno__nombre__icontains=query)
        resultados = []
        for alumno in alumnos:
            profesor = Profesor.objects.filter(comision=alumno.comision).first()
            recetas_alumno = recetas.filter(alumno=alumno)
            resultados.append({
                'alumno': alumno,
                'recetas': recetas_alumno,
                'profesor': profesor
            })
    else:
        resultados = []

    return render(request, 'clases/buscar.html', {'resultados': resultados})
