from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#Forms de las distintas clases
class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    telefono = forms.IntegerField(required=True)
    

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    oficio = forms.CharField(max_length=50, required=True)
    

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    marca = forms.CharField(max_length=50, required=True)
    stock = forms.IntegerField(required=True)

class ProovedorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    producto = forms.CharField(max_length=50, required=True)
    
    
    
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email","password1", "password2"]



class EditarusuarioForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
    


