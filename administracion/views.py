from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView



# Funciones botones principales

def home(request):
    return render(request, "administracion/index.html")

#Clientes
@login_required
def clientes(request):
    contexto = {"clientes": Cliente.objects.all()}
    return render(request, "administracion/clientes.html",contexto)

@login_required
def clienteForm(request):
    if request.method == "POST":
        formcliente = ClienteForm(request.POST)
        if formcliente.is_valid():
            cliente_nombre = formcliente.cleaned_data.get("nombre")
            cliente_apellido = formcliente.cleaned_data.get("apellido")
            cliente_email = formcliente.cleaned_data.get("email")
            cliente_telefono = formcliente.cleaned_data.get("telefono")
            cliente = Cliente(nombre=cliente_nombre, apellido=cliente_apellido, email=cliente_email,telefono=cliente_telefono)
            cliente.save()
            contexto = {"clientes": Cliente.objects.all()}
            return render(request, "administracion/clientes.html",contexto)
    else:
         formcliente= ClienteForm()
        
    return render(request, "administracion/clienteform.html", {"form":formcliente})


@login_required
def Updatecliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        formcliente = ClienteForm(request.POST)
        if formcliente.is_valid():
                cliente.nombre = formcliente.cleaned_data.get("nombre")
                cliente.apellido = formcliente.cleaned_data.get("apellido")
                cliente.email = formcliente.cleaned_data.get("email")
                cliente.telefono = formcliente.cleaned_data.get("telefono")
                cliente.save()
                contexto = {"clientes": Cliente.objects.all()}
                return render(request, "administracion/clientes.html",contexto)
    else:
        formcliente = ClienteForm(initial={"nombre": cliente.nombre, "apellido": cliente.apellido,"email": cliente.email, "telefono": cliente.telefono})
    
    return render(request, "administracion/clienteform.html", {"form":formcliente} )
        
@login_required
def eliminarcliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    contexto = {"clientes": Cliente.objects.all()}
    return render(request,"administracion/clientes.html", contexto)

    
#Empleados

@login_required
def empleados(request):
    contexto = {"empleados": Empleado.objects.all()}
    return render(request, "administracion/empleados.html", contexto)



@login_required
def empleadoForm(request):
    if request.method == "POST":
        formempleado = EmpleadoForm(request.POST)
        if formempleado.is_valid():
            empleado_nombre = formempleado.cleaned_data.get("nombre")
            empleado_apellido = formempleado.cleaned_data.get("apellido")
            empleado_oficio = formempleado.cleaned_data.get("oficio")
            empleado = Empleado(nombre=empleado_nombre, apellido=empleado_apellido, oficio=empleado_oficio)
            empleado.save()
            contexto = {"empleados": Empleado.objects.all()}
            return render(request, "administracion/empleados.html",contexto)
    else:
         formempleado= EmpleadoForm()
        
    return render(request, "administracion/empleadoform.html",{"form":formempleado})


@login_required
def Updateempleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    if request.method == "POST":
        formempleado = EmpleadoForm(request.POST)
        if formempleado.is_valid():
                empleado.nombre = formempleado.cleaned_data.get("nombre")
                empleado.apellido = formempleado.cleaned_data.get("apellido")
                empleado.oficio = formempleado.cleaned_data.get("oficio")
                empleado.save()
                contexto = {"empleados": Empleado.objects.all()}
                return render(request, "administracion/empleados.html",contexto)
    else:
        formempleado = EmpleadoForm(initial={"nombre": empleado.nombre, "apellido": empleado.apellido,"oficio": empleado.oficio})
    
    return render(request, "administracion/empleadoform.html", {"form":formempleado} )


@login_required
def eliminarempleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    empleado.delete()
    contexto = {"empleados": Empleado.objects.all()}
    return render(request,"administracion/empleados.html", contexto)

#Productos

@login_required
def productos(request):
    contexto = {"productos": Productos.objects.all()}
    return render(request, "administracion/productos.html", contexto)



@login_required
def productoForm(request):
    if request.method == "POST":
        formproducto = ProductoForm(request.POST)
        if formproducto.is_valid():
            producto_nombre = formproducto.cleaned_data.get("nombre")
            producto_marca = formproducto.cleaned_data.get("marca")
            producto_stock = formproducto.cleaned_data.get("stock")
            producto = Productos(nombre=producto_nombre, marca=producto_marca, stock=producto_stock)
            producto.save()
            contexto = {"productos": Productos.objects.all()}
            return render(request, "administracion/productos.html",contexto)
    else:
         formproducto= ProductoForm()
        
    return render(request, "administracion/productoform.html",{"form":formproducto})


@login_required
def Updateproducto(request, id_producto):
    producto = Productos.objects.get(id=id_producto)
    if request.method == "POST":
        formproducto = ProductoForm(request.POST)
        if formproducto.is_valid():
                producto.nombre = formproducto.cleaned_data.get("nombre")
                producto.marca = formproducto.cleaned_data.get("marca")
                producto.stock = formproducto.cleaned_data.get("stock")
                producto.save()
                contexto = {"productos": Productos.objects.all()}
                return render(request, "administracion/productos.html",contexto)
    else:
        formproducto = ProductoForm(initial={"nombre": producto.nombre, "marca": producto.marca,"stock": producto.stock})
    
    return render(request, "administracion/productoform.html", {"form":formproducto} )


@login_required
def eliminarproducto(request, id_producto):
    producto = Productos.objects.get(id=id_producto)
    producto.delete()
    contexto = {"productos": Productos.objects.all()}
    return render(request,"administracion/productos.html", contexto)

#Proovedores

@login_required
def proovedores(request):
    contexto = {"proovedores": Proovedor.objects.all()}
    return render(request, "administracion/proovedores.html", contexto)


@login_required
def proovedorForm(request):
    if request.method == "POST":
        formproovedor = ProovedorForm(request.POST)
        if formproovedor.is_valid():
            proovedor_nombre = formproovedor.cleaned_data.get("nombre")
            proovedor_producto = formproovedor.cleaned_data.get("producto")
            proovedor = Proovedor(nombre=proovedor_nombre,producto=proovedor_producto)
            proovedor.save()
            contexto = {"proovedores": Proovedor.objects.all()}
            return render(request, "administracion/proovedores.html",contexto)
    else:
         formproovedor= ProovedorForm()
        
    return render(request, "administracion/proovedorform.html",{"form":formproovedor})


@login_required
def Updateproovedor(request, id_proovedor):
    proovedor = Proovedor.objects.get(id=id_proovedor)
    if request.method == "POST":
        formproovedor = ProovedorForm(request.POST)
        if formproovedor.is_valid():
            proovedor.nombre = formproovedor.cleaned_data.get("nombre")
            proovedor.producto = formproovedor.cleaned_data.get("producto")
            proovedor.save()
            contexto = {"proovedores": Proovedor.objects.all()}
            return render(request, "administracion/proovedores.html",contexto)
    else:
        formproovedor = ProovedorForm(initial={"nombre": proovedor.nombre, "producto": proovedor.producto})
    
    return render(request, "administracion/proovedorform.html", {"form":formproovedor} )


@login_required
def eliminarproovedores(request, id_proovedor):
    proovedores = Proovedor.objects.get(id=id_proovedor)
    proovedores.delete()
    contexto = {"proovedores": Proovedor.objects.all()}
    return render(request,"administracion/proovedores.html", contexto)


#Otros
def acerca(request):
    return render(request,"administracion/acerca.html")

def contacto(request):
    return render(request,"administracion/contacto.html")



#Buscar
@login_required
def BuscarProductos(request):
    return render(request,"administracion/buscarproductos.html")


@login_required
def EncontrarProductos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Productos.objects.filter(nombre__icontains=patron)
        contexto = {'productos': productos}    
    else:
        contexto = {'productos': Productos.objects.all()}
        
    return render(request, "administracion/productos.html", contexto)


#Login

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario,password=clave)
        if user is not None:
            login(request,user)
            
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            return render(request, "administracion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        LoginForm = AuthenticationForm()
        
    return render(request, "administracion/login.html", {"form":LoginForm})


#Registracion

def Registrarse(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "administracion/registro.html", {"form": miForm}) 


#Editar Perfil

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        editForm = EditarusuarioForm(request.POST)
        if editForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = editForm.cleaned_data.get("email")
            user.first_name = editForm.cleaned_data.get("first_name")
            user.last_name = editForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        editForm = EditarusuarioForm(instance=usuario)
    return render(request, "administracion/editarperfil.html",{"form":editForm})   
            

class Cambiarcontraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = "administracion/cambiarcontraseña.html"
    success_url = reverse_lazy("home")
    

#Avatar

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        formavatar = AvatarForm(request.POST, request.FILES)
        if formavatar.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = formavatar.cleaned_data["imagen"]
            avatarviejo = Avatar.objects.filter(user=usuario)
            if len(avatarviejo) > 0:
                for i in range(len(avatarviejo)):
                    avatarviejo[i].delete()
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            return redirect(reverse_lazy("home"))
    else:
        formavatar = AvatarForm()
    return render(request, "administracion/agregaravatar.html", {"form": formavatar})    
    
    
       
        
    