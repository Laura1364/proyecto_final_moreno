from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.escuela)
admin.site.register(models.alumno)
admin.site.register(models.materia)
