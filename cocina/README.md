Proyecto de Clases de Cocina
Este proyecto es una aplicación web desarrollada con Django para gestionar alumnos, profesores y recetas en una clase de cocina.

Estructura del Proyecto
cocina/: Carpeta del proyecto principal de Django.
clases/: Aplicación Django para gestionar alumnos, profesores y recetas.
media/: Carpeta para almacenar archivos multimedia subidos por el usuario.
static/: Carpeta para archivos estáticos como CSS y JS.
templates/: Carpeta para las plantillas HTML.
Instalación
Clonar el repositorio:

bash
Copiar código
git clone <URL-del-repositorio>
cd cocina
Crear un entorno virtual y activarlo:

bash
Copiar código
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
Instalar las dependencias:

bash
Copiar código
pip install -r requirements.txt
Aplicar las migraciones:

bash
Copiar código
python manage.py migrate
Crear un superusuario para el panel de administración:

bash
Copiar código
python manage.py createsuperuser
Iniciar el servidor de desarrollo:

bash
Copiar código
python manage.py runserver
Uso
Acceder al panel de administración:

URL: http://127.0.0.1:8000/admin/
Ingresar con las credenciales del superusuario creado.
Agregar y gestionar registros:

Alumnos: Nombre del alumno y comisión.
Profesores: Nombre del profesor y comisión.
Recetas: Nombre de la receta, nombre del alumno que la creó y sus ingredientes.
Buscar información:

Buscar: Puedes buscar por nombre de alumno o profesor para ver todos los registros asociados a ellos.
Funcionalidades
Página Principal (index.html): Muestra enlaces para agregar alumnos, profesores y recetas, y para buscar registros.
Agregar Alumno (alumno_form.html): Formulario para agregar un nuevo alumno.
Agregar Profesor (profesor_form.html): Formulario para agregar un nuevo profesor.
Agregar Receta (receta_form.html): Formulario para agregar una nueva receta.
Buscar (buscar.html): Permite buscar alumnos, profesores y recetas. Muestra toda la información asociada al alumno o profesor buscado, incluyendo recetas y profesores de la comisión.
Archivos Importantes
clases/models.py: Define los modelos Alumno, Profesor y Receta.
clases/forms.py: Define los formularios para Alumno, Profesor y Receta.
clases/views.py: Contiene las funciones para manejar las vistas de la aplicación.
clases/urls.py: Define las rutas para las vistas de la aplicación.
clases/admin.py: Registra los modelos en el panel de administración de Django.
templates/clases/base.html: Plantilla base para la aplicación.
templates/clases/index.html: Página principal con enlaces a formularios y búsqueda.
templates/clases/alumno_form.html: Formulario para agregar un alumno.
templates/clases/profesor_form.html: Formulario para agregar un profesor.
templates/clases/receta_form.html: Formulario para agregar una receta.
templates/clases/buscar.html: Página de búsqueda que muestra resultados basados en la consulta realizada.