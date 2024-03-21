# Proyecto de Pruebas E2E con Selenium y Python

## README

Este proyecto implementa pruebas End-to-End (E2E) para el flujo de compra en el sitio web 'Sauce Demo', utilizando Selenium con Python y siguiendo el patrón de diseño Page Object Model (POM).

### Pre-requisitos

- Python 3.6 o superior.
- pip (gestor de paquetes de Python).
- WebDriver para Google Chrome o Firefox.
- selenium 4.11.2   
- webdriver-manager 4.0.0
- pytest 7.4.0   
- pytest-html 3.2.0

### Configuración del Entorno

1. Clonar el repositorio o descargar los archivos.
2. Crear y activar un entorno virtual en Python.
3. Instalar las dependencias con `pip install -r requirements.txt`.
4. Descargar el WebDriver correspondiente y colocarlo en la carpeta `/drivers` o en el PATH del sistema.

### Ejecución de las Pruebas

Ejecutar las pruebas con el comando `python -m pytest -v --html=reports/report.html`.

### Estructura del Proyecto

- `/drivers`: WebDriver para el navegador.
- `/pages`: Clases para cada página web según el modelo POM.
- `/tests`: Scripts de prueba.
- `requirements.txt`: Dependencias del proyecto.

Instrucciones de Ejecución de Pruebas en Cypress para PetStore API
=================================================================

Pre-requisitos:
---------------
1. Asegúrate de tener Node.js y npm instalados en tu máquina.
2. Instala Cypress si aún no lo has hecho. Puedes instalarlo ejecutando el siguiente comando en tu terminal:
   npm install cypress --save-dev

Configuración del Proyecto:
---------------------------
1. Crea un nuevo directorio para tu proyecto de pruebas si aún no tienes uno.
2. Dentro de este directorio, inicializa un nuevo proyecto de Node.js ejecutando:
   npm init -y
3. Instala Cypress como se mencionó anteriormente.
4. Abre Cypress por primera vez ejecutando:
   npx cypress open
   Esto configurará la estructura de directorios estándar de Cypress en tu proyecto.

Añadir las Pruebas:
-------------------
1. Localiza el directorio "e2e/APITesting" en tu proyecto.
2. Crea un nuevo archivo de especificación para tus pruebas, por ejemplo, "httprequests.cy.js".
3. Copia y pega el código de las pruebas proporcionado en este archivo.

Ejecutar las Pruebas:
---------------------
1. Abre Cypress utilizando el comando `npx cypress open` si aún no está abierto.
2. En la interfaz de usuario de Cypress, encontrarás el archivo de especificación que creaste. Haz clic en él para ejecutar las pruebas.
3. Lo puedes ejecutar por consola npx cypress run --spec + La ruta del test. 
3. Observa la ejecución de las pruebas en tiempo real en el navegador de Cypress o en la terminal.

Reporte de Pruebas Cypress para PetStore API
------------------
Fecha de Ejecución: 20 de Marzo de 2024
Entorno de Prueba: Desarrollo
Ejecutor de Prueba: Equipo de QA

Resumen General
---------------
Total de Pruebas Ejecutadas: 4
Total de Éxitos: 3
Total de Fallas: 1
Total de Pruebas Saltadas: 0

Detalles de la Ejecución
------------------------
1. Añadir una Mascota a la Tienda
   - Estado: Éxito
   - ID de Mascota Creada: 123456789
   - Detalles: La mascota con ID 123456789 fue creada exitosamente con el nombre "doggie" y estado "available".

2. Consultar la Mascota Ingresada Previamente (Búsqueda por ID)
   - Estado: Éxito
   - ID de Mascota Consultada: 123456789
   - Detalles: La consulta de la mascota con ID 123456789 fue exitosa, validando su existencia y datos.

3. Actualizar el Nombre de la Mascota y el Estado a "Sold"
   - Estado: Fallo
   - ID de Mascota Actualizada: 123456789
   - Detalles: La actualización del nombre y estado de la mascota con ID 123456789 falló debido a un error de timeout de la petición. Es posible que la API esté experimentando problemas de rendimiento.

4. Consultar la Mascota Modificada por Estado (Búsqueda por Estado)
   - Estado: Éxito
   - Estado de Búsqueda: Sold
   - Detalles: La búsqueda de mascotas con estado "sold" no retornó la mascota con ID 123456789 debido al fallo en la actualización previa, pero la ejecución de la petición fue exitosa.



