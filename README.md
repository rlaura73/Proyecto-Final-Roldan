# Proyecto Final - Python
#### Comisión: 47770
#### Alumno: Laura Roldán

## Nombre del Proyecto
Bookrealm: compra de libros

## Versión
1.0

## Descripción del Proyecto
Sitio Web destinado a compras de libros.

A fin de navegar por las secciones de la página web, el usuario será requerido iniciar sesión o registrarse (en caso de no contar con usuario o contraseña) al querer realizar una compra o agregar reseña. En ambas opciones, una vez la página valide la autenticación del usuario, este será redirigido al inicio del sitio web.



Los usuarios pueden realizar las siguientes accciones:
- Iniciar / cerrar sesión
- Editar perfil
- Ver libros o ver detalle del libro
- Comprar libros
- Ver ofertas
- Buscar ofertas
- Ver las compras que realizaron
- Agregar comentarios
- Ver todos los comentarios que realizaron
- Editar sus comentarios
- Eliminar sus comentarios



El administrador puede:
- Agregar libro
- Ver libro
- Editar libro
- Eliminar libro
- Eliminar reseñas de otros usuarios
- Iniciar / cerrar sesión



## Funcionalidad
Se dispone de un menú de navegación en el que se visualizan:
- LOGO DE LA EMPRESA: nos manda al tope de la página, no al inicio.
- INICIO: página principal del sitio.
    - "Botón" de acceso rápido a la sección (botón -Ver más-), de lo cual, nos muestra novedades, libros principales con información breve.
- LIBROS: página de libros registrados en la base de datos. Cuenta con:
    - Un botón de acceso rápido a la sección (botón -Ver más-)
    - Un botón para realizar una búsqueda de libros por título, lo cual redirige hacia otra página.
        - La página búsqueda por título, nos muestra una barra de búsqueda, de lo cual, al usarla (clic en botón -Buscar-) sea si encuentra o no resultados, nos lleva hacia otra página.
        - La página resultado de la búsqueda, nos muestra si encontró o no registros de los libros.
            - De haber encontrado, los despliega.
            - De no haber encontrado, despliega un mensaje de aviso en un párrafo.
    - Los más nuevos a la izquierda o tope de la sección, los más viejos al fondo o derecha.
        - Si iniciaste sesión o no, solo muestra el precio, si iniciaste como administrador o staff muestra stock y oferta. Si querés explorar un libro con más detalle, se aprieta botón -Ver-
            - Nos lleva a otra página: detalle del libro.
            - En esta otra página, observamos un carrusel del cual podemos hacer una lectura previa del libro.
            - En caso de querer comprar ese libro sin tener que regresar a la página de Libros, ya cuenta con un botón -Comprar-.
        - Para el botón -Comprar-:
            - En caso de no haber iniciado sesión, te exige que te loguees, ya que es necesario para el sistema registrar quién está haciendo la compra.
            - Si lograste loguearte exitosamente, te redirige a la página Inicio y se visualizará tu nombre de usuario en la barra de navegación (reemplazando al botón -Login-)
        - Las funciones de editar y eliminar Libro son exclusivamente del Aministrador o staff. Es un botón que se visualiza al lado del botón -Buscar libros por título-, únicamente para el super usuario o staff.
            - Unicamente, en el botón -Editar-, podrá incluir imágenes como la portada, la imagen previa 1 y la imagen previa 2. Estos 3 campos son obligatorios ya que el sistema no cuenta con un autocompletado para buscar las imágenes.
- OFERTAS: página para visualizar las ofertas disponibles.
    - Un botón de acceso rápido a la sección (botón -Ver más-)
    - Un botón para realizar una búsqueda de ofertas específicas (15%, 20%, etc), lo cual redirige hacia otra página.
        - La página búsqueda de ofertas, nos muestra una barra de búsqueda, de lo cual, al usarla (clic en botón -Buscar-) sea si encuentra o no resultados, nos lleva hacia otra página.
        - La página resultado de la búsqueda, nos muestra si encontró o no registros de los libros con ofertas.
            - De haber encontrado, los despliega.
            - De no haber encontrado, despliega un mensaje de aviso en un párrafo.
    - Como son registros de libros, se visualizan los botones de -Ver- y -Comprar-.
- COMENTARIOS: página de reseñas de los usuarios, comentando sobre la experiencia de usuario en el sitio.
    - Botón de acceso rápido a la sección (-Ver más-)
    - Botón nueva reseña
        - Si no estás logueado, te exige que inicies sesión, ya que de no hacerlo el sistema no sabe quién agrega un comentario. Al loguearte, te redirige a la página Inicio.
        - Si has rellenado los campos, al agregar el comentario, el sitio te redirige a la página Comentarios.
    - Se listan los más nuevos al tope de la sección, los más viejos al fondo. Se incluye avatar (si tiene o no) del usuario, fecha de subida, valoración, título y comentario.
- SOBRE MÍ: página de información personal de la empresa y mía como desarrolladora del sitio.
- LOGIN: página para iniciar sesión en el sistema, actualmente en desarrollo. Cuenta con un enlace para registrarse como usuario en la base de datos.
    - Dispone de un enlace de registro, en caso de no tener usuario.
        - Es otra página distinta: registro. Todos los campos a rellenar son obligatorios, si se registró exitosamente, te redirije a la página Inicio.
    - En caso de introducir bien los datos, te redirige al Inicio, de no ser así se despliega un mensaje de aviso y un botón para regresar al formulario.
        - Una vez iniciada la sesión, al hacer clic en el nombre de usuario, nos lleva a la página Perfil:
            - Botón -Editar perfil-: redirige a otra página, del cual podemos rellenar algunos datos, cambiar la contraseña y si queremos un avatar, lo podemos desplegar. En estos campos, no son obligatorios.
            - Botón -Ver tus compras-: redirige a otra página, del cual podemos observar la cronología de compras realizadas. Cada una dispone de un botón -Ver-, en caso de querer consultar más información.
            - Botón -Ver tus reseñas-: redirige a otra página, del cual podemos observar la cronología de los comentarios realizados. Cada uno dispone de un obtón -Editar reseña- y -Eliminar reseña-. NOTA: no se puede editar o eliminar comentarios de otros, a no ser que seas el administrador.
            - Botón -Cerrar sesión-: nos desloguea y nos redirige a la página Inicio.
        
NOTAS:
- El administrador no necesita comprar o agregar reseña por lo que algunos botones (como -Comprar-, -Nueva reseña-, -Ver tus compras-, -Ver tus reseñas-) no se visualizarán al iniciar como administrador o staff. Además, podrá agregar, ver, editar o borrar libros únicamente en la página Libros.
- La mayoría de las páginas, cuenta con un botón de acceso rápido a la sección, -Ver más-.

## Tecnología Utilizada

##### Front-End
- HTML 5
- CSS 3
- Javascript ES6
- Bootstrap 5.2

##### Back-End
- Python 3.9.5
- Django 4.2.5
- Pillow 10.0.1

## Video Demostración

https://www.youtube.com/watch?v=hKDEFuiTgGk


## URLS

##### /admin/
##### /libros/
##### /libros/nuevo-libro/
##### /libros/detalle-libro/int/
##### /libros/modificar-libro/int/
##### /libros/eliminar-libro/int/
##### /libros/busqueda-libro/
##### /ofertas/
##### /ofertas/busqueda-oferta/
##### /comentarios/
##### /comentarios/agregar-comentario/
##### /comentarios/editar-comentario/int/
##### /comentarios/eliminar-comentario/int/
##### /comentarios/mis-comentarios/
##### /compras/
##### /compras/mis-compras/
##### /compras/comprar-libro/int/
##### /compras/detalle-compra/int/
##### /usuarios/
##### /usuarios/inicio-sesion/
##### /usuarios/registro/
##### /usuarios/perfil/
##### /usuarios/editar/
##### /usuarios/logout/



## Pasos entorno virtual

```
pip install pipenv
pipenv shell
pipenv install -r requirements.txt
```






