from django.shortcuts import redirect, render
from .forms import AlumnoFormulario, AlumnoBuscarFormulario, MateriaFormulario, ProfesorFormulario, UserAvatarFormulario
from .models import Alumno, Materia, Profesor, Avatar
from django.contrib.auth.decorators import login_required

def inicio_view (request):
    return render(request, "bioapp/inicio.html")


   
       

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



from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def login_view(request):

    if request.user.is_authenticated:
        return render(
            request,
            "bioapp/inicio.html",
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )

    if request.method == "GET":
        return render(
            request,
            "bioapp/login.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(
                request,
                "bioapp/inicio.html",
                {"mensaje": f"Bienvenido {modelo.username}"}
            )
        else:
            return render(
                request,
                "bioapp/login.html",
                {"form": formulario}
            )



def logout_view(request):
    pass


from .forms import UserCreationFormulario, UserEditionFormulario
from django.contrib.auth.views import PasswordChangeView


def registro_view(request):

    if request.method == "GET":
        return render(
            request,
            "bioapp/registro.html",
            {"form": UserCreationFormulario()}
        )
    else:
        formulario = UserCreationFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(
                request,
                "bioapp/inicio.html",
                {"mensaje": f"Usuario creado: {usuario}"}
            )
        else:
            return render(
                request,
                "bioapp/registro.html",
                {"form": formulario}
            )
            
def editar_perfil_view(request):

    usuario = request.user
    avatar = Avatar.objects.filter(user=usuario).first()
    avatar_url = avatar.imagen.url if avatar is not None else ""


    if request.method == "GET":


        valores_iniciales = {
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        }


        formulario = UserEditionFormulario(initial=valores_iniciales)
        return render(
            request,
            "bioapp/editar-perfil.html",
            context={"form": formulario, "usuario": usuario, "avatar_url": avatar_url}
            )
    else:
        formulario = UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.email = informacion["email"]

            usuario.set_password(informacion["password1"])

            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
        return redirect("bioapp:inicio")


def crear_avatar_view(request):

    usuario = request.user

    if request.method == "GET":
        formulario = UserAvatarFormulario()
        return render(
            request,
            "bioapp/crear-avatar.html",
            context={"form": formulario, "usuario": usuario}
        )
    else:
        formulario = UserAvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Avatar(user=usuario, imagen=informacion["imagen"])
            modelo.save()
            breakpoint()
        return redirect("bioapp:inicio")            
  
  
def about_view (request):
      return render (request, "bioapp/about.html")         
  
  
  
@login_required
def profesor_view(request):
    if request.method == "GET":
        return render(
            request,
            "bioapp/profesor_formulario_avanzado.html",
            {"form": ProfesorFormulario()}
        )
    else:
        formulario = ProfesorFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Profesor(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                materia=informacion["materia"]
            )
            modelo.save()
        return render(
            request,
            "bioapp/inicio.html",
        )

@login_required
def profesores_crud_read_view(request):
    profesor = Profesor.objects.all()
    return render(request, "bioapp/profesor_lista.html", {"profesor": profesor})

@login_required
def profesores_crud_delete_view(request, profesor_materia):
    profesor_a_eliminar = Profesor.objects.filter(materia=profesor_materia).first()
    profesor_a_eliminar.delete()
    return profesores_crud_read_view(request)


@login_required
def profesores_crud_update_view(request, profesor_materia):
    profesor = Profesor.objects.filter(materia=profesor_materia).first()
    if request.method == "GET":
        formulario = ProfesorFormulario(
            initial={
                "nombre": profesor.nombre,
                "apellido": profesor.apellido,
                "materia": profesor.materia
            }
        )
        return render(request, "bioapp/profesor_formulario_edicion.html", {"form": formulario, "profesor": profesor})
    else:
        formulario = ProfesorFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            profesor.nombre=informacion["nombre"]
            profesor.apellido=informacion["apellido"]
            profesor.materia=informacion["materia"]
            profesor.save()
        return profesores_crud_read_view(request) 