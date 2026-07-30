from django.urls import path, include
from administracion.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #Home
    path('', home, name="home"), 
    
    #Clientes 
    path('clientes', clientes, name="clientes"),
    path('clienteform', clienteForm, name="clienteform"),
    path('Updatecliente/<id_cliente>/', Updatecliente, name="Updatecliente"),
    path('eliminarcliente/<id_cliente>/', eliminarcliente, name="eliminarcliente"),
    
    
    #Empleados
    path('empleados', empleados, name="empleados"),
    path('empeladoform', empleadoForm, name="empleadoform"),
    path('Updateempleado/<id_empleado>/', Updateempleado, name="Updateempleado"),
    path('eliminarempleado/<id_empleado>/', eliminarempleado, name="eliminarempleado"),
        
        
    #Productos
    path('productos', productos, name="productos"),
    path('productoform', productoForm, name="productoform"),
    path('Updateproducto/<id_producto>/', Updateproducto, name="Updateproducto"),
    path('eliminarproducto/<id_producto>/', eliminarproducto, name="eliminarproducto"),
    
    
    #Proovedores
    path('proovedores', proovedores, name="proovedores"),
    path('proovedorform', proovedorForm, name="proovedorform"),
    path('Updateproovedor/<id_proovedor>/', Updateproovedor, name="Updateproovedor"),
    path('eliminarproovedores/<id_proovedor>/', eliminarproovedores, name="eliminarproovedores"),
    
    #Otros
    path('acerca', acerca, name="acerca"),
    path('contacto', contacto, name="contacto"), 
    
    #Busquedas
    path('buscarproductos', BuscarProductos, name="buscarproductos"),
    path('encontrarproductos', EncontrarProductos, name="encontrarproductos"),  
    
    #Login
    path('login/',loginRequest, name="login"),
    
    
    #logout
    path('logout/', LogoutView.as_view(template_name="administracion/logout.html"), name="logout"),


    #Registracion
    path('registro/',Registrarse, name="registro"),
    
    
    #Editar Perfil
    path('perfil/',editarPerfil, name="perfil"),
    path('<int:pk>/password/',Cambiarcontraseña.as_view(), name="cambiarContraseña"),
    
    #Avatar
    path('agregar_avatar/',agregarAvatar, name="agregar_avatar"),

]

