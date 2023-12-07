from django.db import models

class escuela (models.Models):
    numero_escuela = models.Charfield(max_length=100, unique=True)

class alumno (models.Models):
    nombre = models.Charfield(max_length=100, unique=True)
    apellido = models.Charfield(max_length=100, unique=True)
    mail = models.EmailField(max_length=254)

class materia (models.Models):
    materia = models.Charfield(max_length=100, unique=True)
    nota = models.DecimalField(max_digits=5, decimal_places=2)