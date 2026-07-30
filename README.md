# Harinas del Norte — Web Management System

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0.6-092E20?logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Academic%20Project-success)

A web-based management system developed with Django for a wholesale flour distribution business.

The application provides a public company website and an authenticated management area where users can manage customers, employees, suppliers, products, and their own account information.

This project was developed by **Martino De Ninis** as the final assignment for a Python and Django course.

<p align="center">
  <a href="https://www.youtube.com/watch?v=80gE1eTMtEs">
    <img
      src="https://img.youtube.com/vi/80gE1eTMtEs/maxresdefault.jpg"
      alt="Harinas del Norte application demo"
      width="720"
    >
  </a>
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=80gE1eTMtEs">
    Watch the application demo
  </a>
</p>

## Features

### Public area

Visitors can access:

- Company landing page
- General company information
- Contact information
- User registration
- User login

### Authenticated management area

Registered users can access:

- Customer management
- Employee management
- Supplier management
- Product and stock management
- Product search
- User profile editing
- Password changes
- Profile avatar uploads
- User logout

### CRUD operations

The application provides interfaces to create, read, update, and delete records for:

- Customers
- Employees
- Suppliers
- Products

### User account management

Users can:

- Register a new account
- Log in and log out
- Update their first name, last name, and email
- Change their password
- Upload or replace their profile avatar

## Tech Stack

### Backend

- Python
- Django 5.0.6
- Django ORM
- Django Authentication
- SQLite

### Frontend

- HTML
- CSS
- Bootstrap
- Django Templates
- Font Awesome

### Development tools

- Git
- GitHub
- Python virtual environments
- Django development server

## Architecture

The application follows Django's Model-View-Template architecture.

### Models

The domain model includes:

- `Cliente`: customer information
- `Empleado`: employee information
- `Producto`: product, brand, and stock information
- `Proveedor`: supplier information
- `Avatar`: user profile image

### Views

The application contains views for:

- Listing records
- Creating records
- Editing records
- Deleting records
- Searching products
- Authentication
- Registration
- Profile management
- Avatar uploads

### Templates

Django templates are used to render:

- The landing page
- Authentication forms
- Management tables
- CRUD forms
- User profile pages
- Institutional and contact pages

### Persistence

Data is stored locally using SQLite and accessed through the Django ORM.

## Requirements

Before running the application, install:

- Python 3.10 or newer
- Git

You can verify the installation with:

```bash
python --version
git --version
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Dnmartinoo/Sistema_de_Gestion_Web.git
cd Sistema_de_Gestion_Web
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Apply the database migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Creating an Account

You can create a regular account from the registration page:

```text
http://127.0.0.1:8000/registro/
```

After logging in, the management features become available.

## Django Administration

To access Django's built-in administration interface, create a superuser:

```bash
python manage.py createsuperuser
```

Then visit:

```text
http://127.0.0.1:8000/admin/
```

## Main Routes

| Route | Description | Authentication |
|---|---|---|
| `/` | Home page | Public |
| `/acerca` | Company information | Public |
| `/contacto` | Contact information | Public |
| `/registro/` | User registration | Public |
| `/login/` | User login | Public |
| `/clientes` | Customer management | Required |
| `/empleados` | Employee management | Required |
| `/productos` | Product management | Required |
| `/proovedores` | Supplier management | Required |
| `/buscarproductos` | Product search | Required |
| `/perfil/` | Profile management | Required |
| `/agregar_avatar/` | Avatar upload | Required |
| `/admin/` | Django administration | Staff only |

## Manual Testing

The original project includes a manual test plan covering the primary application flows:

- User registration
- Login and logout
- CRUD operations
- Product search
- Profile editing
- Password changes
- Avatar uploads

The test document can be found here:

[View manual test cases](./Casos%20de%20Test.xls)

Automated tests are planned as a future improvement.

## Demo

A complete walkthrough of the application is available on YouTube:

## Project Status

The academic version is complete and functional.

The current repository represents a learning project and is not intended for production deployment.

## Known Limitations

- SQLite is used as a local development database
- Access control only distinguishes between authenticated and unauthenticated users
- Management operations do not currently use separate employee or administrator roles
- Automated tests have not yet been implemented
- The application has not been deployed to a production environment
- The frontend was designed primarily for desktop use

## Possible Future Improvements

- Add automated tests with Django TestCase and pytest
- Add role-based permissions
- Replace SQLite with PostgreSQL
- Add pagination to management tables
- Add confirmation pages for destructive operations
- Move sensitive configuration to environment variables
- Add Docker support
- Add GitHub Actions for continuous integration
- Deploy a public demonstration environment
- Improve responsive design and accessibility
- Add product categories and supplier relationships
- Add inventory movement and stock history

## Academic Context

This project was originally developed as the final assignment for a Python and Django course.

The repository is publicly available for educational and professional portfolio purposes.

## Author

### Martino De Ninis

Computer Engineering student at the University of Buenos Aires.

- GitHub: [Dnmartinoo](https://github.com/Dnmartinoo)

## Disclaimer

The application was developed as an educational prototype.

The names, data, users, and records included in public demonstrations should be considered fictional or illustrative.
