# Harinas Del Norte - Sistema de Gestión Web

Este proyecto es una aplicación web desarrollada como entrega final para el curso de Python en Coderhouse. Consiste en un prototipo funcional de un sistema de gestión y portal web diseñado para una empresa de distribución mayorista de harinas. 

El sistema permite exhibir el catálogo de productos al público y ofrece un panel de administración completo para gestionar las operaciones diarias del negocio.

## 🚀 Características Principales

El proyecto cuenta con un sistema de control de acceso que divide las funcionalidades según el estado del usuario:

### 🔒 Acceso Público (Usuarios no registrados)
* **Landing Page:** Interfaz principal que invita a los usuarios a registrarse.
* **Información Institucional:** Sección "Acerca de" con información de la empresa y datos de contacto para consultas comerciales o servicios de entrega.

### 🔓 Panel de Administración (Usuarios Autenticados)
Al iniciar sesión, se desbloquean las funcionalidades del sistema de gestión:

* **Gestión de Base de Datos (CRUD):** Interfaces completas para Crear, Leer, Actualizar y Eliminar registros de 4 entidades principales:
  * Clientes
  * Proveedores
  * Empleados
  * Productos
* **Motor de Búsqueda:** Funcionalidad para filtrar productos de manera dinámica dentro de la base de datos, facilitando la localización de artículos específicos.
* **Gestión de Perfil de Usuario:** 
  * Edición de datos personales (Nombre, Apellido, Email).
  * Sistema de cambio de contraseña seguro.
  * Personalización de la cuenta mediante la carga de un Avatar (foto de perfil).

## 💻 Tecnologías Utilizadas
* **Backend:** Python (Django)
* **Frontend:** HTML, CSS

## 🧪 Testing y Casos de Uso

El proyecto incluye un excel con la planificación y ejecución de pruebas para asegurar el correcto funcionamiento de los módulos. 
Puedes revisar el documento en la rama principal o mediante el siguiente enlace:
