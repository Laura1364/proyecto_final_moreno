from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=100)
    materia= models.CharField(max_length=100)
      
 

class Alumno (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)


    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.mail}"
    
    
class Materia (models.Model):
    materia = models.CharField(max_length=100)
    codigo = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.materia} ({self.codigo})"

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="media/avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

