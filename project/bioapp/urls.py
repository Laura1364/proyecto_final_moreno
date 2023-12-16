"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bioapp.views import (
    inicio_view,
    numero_escuela_view,
    alumno_crear_view,
    alumno_buscar_view,
    materias_view
)

app_name = "bioapp"


urlpatterns = [
    path("inicio/", inicio_view, name="inicio"),
    path("numero_escuela/",numero_escuela_view, name="numero_escuela"),
    path("alumno/crear", alumno_crear_view, name="alumno_crear"),
    path("alumno/buscar",alumno_buscar_view, name="alumno_buscar"),
    path("materias/", materias_view)
    
]
