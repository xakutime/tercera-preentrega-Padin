from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    comision = models.IntegerField() 

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    comision = models.IntegerField()  

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    nombre_receta = models.CharField(max_length=100)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    ingredientes = models.TextField()

    def __str__(self):
        return self.nombre_receta