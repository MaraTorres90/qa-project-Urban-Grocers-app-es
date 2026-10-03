Urban Grocers — Pruebas de API con Python

Descripción
Urban Grocers es una aplicación de entrega de comestibles. En este proyecto escribí pruebas para revisar el campo name al crear un kit de productos mediante su API.

Objetivo
Comprobar cómo responde la API al recibir distintos nombres de kits, incluyendo datos válidos, campos vacíos y tipos de datos incorrectos.

Qué hice
- Creé un usuario para obtener un token de autorización.
- Utilicé el token para enviar solicitudes de creación de kits.
- Preparé casos positivos y negativos para el campo name.
- Comprobé los códigos de respuesta.
- En los casos positivos, comprobé que el nombre recibido coincidiera con el enviado.

Escenarios de prueba
- Nombre de un carácter.
- Nombres largos para revisar la longitud permitida.
- Nombre vacío.
- Caracteres especiales.
- Espacios en el nombre.
- Números escritos como texto.
- Solicitud sin el campo name.
- Un número entero en lugar de texto.

Para los casos positivos definí como respuesta esperada el código 201. Para los negativos, el código 400.

## Herramientas
Python, pytest y Requests.

Cómo organicé el proyecto
- configuration.py: contiene la dirección del servidor y las rutas de la API.
- data.py: contiene los datos y encabezados utilizados.
- sender_stand_request.py: contiene las funciones para enviar solicitudes.
- create_kit_name_kit_test.py: contiene los casos de prueba y sus comprobaciones.

Cómo ejecutar las pruebas
1. Tener Python instalado.
2. Iniciar el servidor de Urban Grocers.
3. Actualizar URL_SERVICE en configuration.py con la dirección del servidor. El valor api.example.com es solo un ejemplo y debe reemplazarse.
4. Instalar las dependencias con:
   python -m pip install pytest requests
5. Ejecutar:
   python -m pytest create_kit_name_kit_test.py -v

Resultados y evidencias
Implementé nueve casos de prueba para revisar la creación de kits con distintas entradas.

Las comprobaciones y los datos utilizados pueden consultarse en create_kit_name_kit_test.py.

No incluyo un porcentaje de pruebas aprobadas porque no tengo adjunto un reporte actualizado de ejecución.

Detalle pendiente de corregir
Durante la revisión del código identifiqué que los casos llamados 511 y 512 caracteres contienen realmente 255 y 256 caracteres.

Debo ajustar esos datos y volver a ejecutar las pruebas para comprobar los límites previstos. Esta diferencia está en los datos de prueba y no demuestra un error de la API.

Mi aportación
Organicé las solicitudes y las comprobaciones para facilitar la revisión de distintos nombres de kits. Separé los casos positivos y negativos para identificar cuándo la API acepta o rechaza los datos enviados.

Autora
Maarabid Torres — QA Engineer Jr.

Portafolio:
https://maratorres90.github.io/