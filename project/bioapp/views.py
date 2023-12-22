from django.shortcuts import redirect, render
from .forms import AlumnoFormulario, AlumnoBuscarFormulario, MateriaFormulario
from .models import Alumno, Materia


def inicio_view (request):
    return render(request, "bioapp/inicio.html")


def profesor_view(request):
     if request.method == "GET":
         print("+" * 90) #  Imprimimos esto para ver por consola
         print("+" * 90) #  Imprimimos esto para ver por consola
         return render(
             request,
             "bioapp/profesor_formulario_basico.html",
         )
     else:
         print("*" * 90)     #  Imprimimos esto para ver por consola
         print(request.POST) #  Imprimimos esto para ver por consola
         print("*" * 90)     #  Imprimimos esto para ver por consola
         return render(
             request,
             "bioapp/profesor_formulario_basico.html",
         )   
     
       

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
            modelo = Alumno(nombre=informacion["nombre"], apellido=informacion["apellido"], mail=informacion["mail"] )
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
            for alumno in Alumno.objects.filter(apellido=informacion["apellido"]):
                alumno_lista.append(alumno)

            contexto = {"alumno": alumno_lista}
            return render(request, "bioapp/alumno_lista.html", contexto)


def materias_view(request):
    if request.method == "GET":
        print("+" * 90) #  Imprimimos esto para ver por consola
        print("+" * 90) #  Imprimimos esto para ver por consola
        form = MateriaFormulario()
        return render(
            request,
            "bioapp/materia_formulario.html",
            context={"form": form}
        )
    else:
        formulario = MateriaFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Materia (materia=informacion["materia"], codigo=informacion["codigo"])
            modelo.save()

        return redirect("bioapp:inicio")




  
            