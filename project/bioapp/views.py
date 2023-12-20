from django.shortcuts import redirect, render
from .forms import AlumnoFormulario, AlumnoBuscarFormulario, MateriaFormulario
from .models import Alumno


def inicio_view (request):
    return render(request, "bioapp/inicio.html")


def numero_escuela_view(request):
    numero = "123"
    nombre = "Malvinas"
    diccionario = {
        'numero': numero,
        'nombre': nombre,
         } 
    return render(request, "bioapp/padre.html", diccionario)     


def alumno_crear_view(request):
    if request.method == "GET":
        print("+" * 90) #  Imprimimos esto para ver por consola
        print("+" * 90) #  Imprimimos esto para ver por consola
        form = AlumnoFormulario()
        return render(
            request,
            "bioapp/formulario_avanzado.html",
            context={"form": form}
        )
    else:
        formulario = AlumnoFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Alumno(alumno=informacion["alumno"], camada=informacion["camada"])
            modelo.save()

        return redirect("bioapp:inicio")


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
            alumno_lista = []
            for alumno in Alumno.objects.filter(nota=informacion["nota"]):
                alumno_lista.append(alumno)

            contexto = {"not": alumno_lista}
            return render(request, "bioapp/alumno_lista.html", contexto)


def materias_view(request):
    if request.method == "GET":
        print("+" * 90) #  Imprimimos esto para ver por consola
        print("+" * 90) #  Imprimimos esto para ver por consola
        form = MateriaFormulario()
        return render(
            request,
            "bioapp/formulario_avanzado.html",
            context={"form": form}
        )
    else:
        formulario = MateriaFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Alumno(alumno=informacion["alumno"], camada=informacion["camada"])
            modelo.save()

        return redirect("bioapp:inicio")




  
            