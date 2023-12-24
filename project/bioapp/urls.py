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

from django.urls import path
from django.contrib.auth.views import LogoutView
from bioapp.views import (
    inicio_view,
    profesor_view,
    alumno_crear_view,
    alumno_buscar_view,
    materias_view,
    login_view,
    registro_view,
    about_view,
    contenido_view,
    editar_perfil_view,
    crear_avatar_view,
    profesores_crud_delete_view,
    profesores_crud_read_view,
    profesores_crud_update_view,
    profesor_view
)

app_name= "bioapp"


urlpatterns = [
    path("alumno/crear/", alumno_crear_view, name="alumno_crear"),
    path("alumno/buscar/",alumno_buscar_view, name="alumno_buscar"),
    path("materias/", materias_view, name="materias"),
    path("inicio/", inicio_view, name="inicio"),
    path("registro", registro_view, name="registro"),
    path("login", login_view, name="login"),
    path("logout", LogoutView.as_view(template_name="bioapp/logout.html"), name="logout"),
    path("editar-perfil/", editar_perfil_view, name="editar-perfil"),
    path("crear-avatar/", crear_avatar_view, name="crear-avatar"),
    path("about/", about_view, name= "about"),
    path("contenido/", contenido_view, name= "contenido"),
    path("profesor/", profesor_view),
    path("profesor-lista/", profesores_crud_read_view),
    path("profesor-eliminar/<profesor_materia>/", profesores_crud_delete_view),
    path("profesor-editar/<profesor_materia>/", profesores_crud_update_view),
]
