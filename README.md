# 🚀 Proyecto Guía de Django

Este es un proyecto web de ejemplo desarrollado con Python y Django, creado como parte de la guía del curso. El proyecto sigue el patrón de arquitectura MVT (Modelo-Vista-Template).

---

## 📋 Funcionalidades Principales

Este proyecto cumple con los siguientes requisitos clave de la consigna:

* **Patrón MVT:** La estructura del proyecto separa la lógica de negocio (Vistas), la estructura de datos (Modelos) y la presentación (Templates).
* **Modelos:** Incluye modelos (en `models.py`) que definen las tablas de la base de datos (Paso 20).
* **Vistas:** Contiene vistas (en `views.py`) que procesan las solicitudes de los usuarios y devuelven respuestas (Paso 19).
* **Templates:** Utiliza plantillas HTML (en la carpeta `templates/`) para renderizar la información (Paso 17).
* **Formularios:** Implementa formularios de Django (en `forms.py`) para permitir la entrada de datos por parte del usuario (Paso 21).
* **Panel de Administración:** Los modelos están registrados en el `admin.py` para poder gestionarlos desde el panel de administrador (Paso 20.5).

---

## ⚙️ Instalación y Puesta en Marcha

Sigue estos pasos para correr el proyecto en tu máquina local.

### Prerrequisitos

* [Python 3.x](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)

### Pasos

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/frespinosa/guia-django.git](https://github.com/frespinosa/guia-django.git)
    cd guia-django
    ```

2.  **Crear y Activar el Entorno Virtual:**
    *Este proyecto usa un entorno virtual (`venv`) para manejar las dependencias. Es crucial crearlo y activarlo.*
    ```bash
    # Paso 1: Crear el entorno (ej: .venv)
    python -m venv .venv

    # Paso 2: Activarlo
    # En Windows (PowerShell):
    .\.venv\Scripts\Activate.ps1
    
    # En Mac/Linux:
    source .venv/bin/activate
    ```
    *(Recuerda que la carpeta `.venv` ya está incluida en el `.gitignore`)*.

3.  **Instalar las Dependencias:**
    *Todas las librerías necesarias (como Django) están listadas en `requirements.txt`.*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar las Migraciones:**
    *Esto creará la base de datos `db.sqlite3` y las tablas de tus modelos.*
    ```bash
    python manage.py migrate
    ```

5.  **Crear un Superusuario (Opcional pero recomendado):**
    *Para acceder al panel de admin (`/admin`), necesitas un usuario.*
    ```bash
    python manage.py createsuperuser
    ```

6.  **Correr el Servidor:**
    ```bash
    python manage.py runserver
    ```
    ¡Listo! Abre tu navegador y visita [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 📍 Guía de Funcionalidades (URLs)

Una vez que el servidor esté corriendo, puedes acceder a las siguientes secciones:

* **/ (Página de Inicio):** `inicio/views.py` -> `inicio()`
* **/listado-autos/**: Muestra la lista de todos los autos en la base de datos.
* **/crear-auto/<marca>/<modelo>/**: Crea un nuevo auto pasándole los datos por la URL. (Ej: `/crear-auto/Ford/Fiesta`)
* **/admin/**: Panel de administración de Django (requiere superusuario)
