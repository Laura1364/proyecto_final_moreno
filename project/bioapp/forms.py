from django import forms
from .models import Avatar

class AlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    mail = forms.EmailField(max_length=200)
class AlumnoBuscarFormulario(forms.Form):
    apellido = forms.CharField(max_length=50)
    
class MateriaFormulario(forms.Form):
    materia = forms.CharField(max_length=100)
    codigo = forms.CharField(max_length=100)

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido =forms.CharField(max_length=100)
    materia= forms.CharField(max_length=100)
    

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel


class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["password1", "password2", "username", "email"]
        help_texts = {k: "" for k in fields}


class UserEditionFormulario(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Apellido", widget=forms.PasswordInput)
    password = None

    class Meta:
        model = UserModel
        fields = ["email", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}
        
class UserAvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ["imagen"]