from django.db import models

class Escuela (models.Model):
    escuela = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.escuela}"
 

class Alumno (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    
class Materia (models.Model):
    materia = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.materia} ({self.nota})"
