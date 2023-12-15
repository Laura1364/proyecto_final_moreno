from django import forms


class AlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    mail = forms.EmailField(max_length=200)
class AlumnoBuscarFormulario(forms.Form):
    apellido = forms.CharField(max_length=50)
    



