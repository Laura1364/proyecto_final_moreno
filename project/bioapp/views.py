from django.shortcuts import render
from .forms import AlumnoFormulario, AlumnoBuscarFormulario
from .models import Escuela
from .models import Alumno


def inicio_view(request):
    return render(request, "bioapp/inicio2.html")


def numero_escuela_view(xx):
    numero = "123"
    nombre = "Malvinas"
    diccionario = {
        'numero': numero,
        'nombre': nombre,
         } 
    return render(xx, "bioapp/padre.html", diccionario)     


def alumno_crear_view(request):
    if request.method == "GET":
        contexto ={"form":AlumnoFormulario()}
        return render(request,"bioapp/formulario_avanzado.html, context = contexto")
    else:
        print(request.POST)
        formulario = AlumnoFormulario(request.POST)
        if formulario.is_valid():
            informacion_nueva = formulario.cleaned_data
            modelo = Alumno (alumno = informacion_nueva["alumno"])
            modelo.save()
            return render(request, "bioapp/index.html")
        


def alumno_buscar_view(request):
    if request.method == "GET":
        form = AlumnoBuscarFormulario()
        return render(
            request,
            "bioapp/alumno_formulario_busqueda.html",
            context={"form": form}
        )
    else:
        formulario = AlumnoBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            alumnos_lista = []
            for alumno in Alumno.objects.filter(curso=informacion["curso"]):
                alumnos_lista.append(Alumno)

            contexto = {"cursos": alumnos_lista}
            return render(request, "bioapp/cursos_list.html", contexto)


def materias_view(request):
    materias = []
    for materias in materias.objects.all():
        materias.append(materias)

    contexto = {"materias": materias}
    return render(request, "bioapp/alumnos_list.html", contexto)






  
            