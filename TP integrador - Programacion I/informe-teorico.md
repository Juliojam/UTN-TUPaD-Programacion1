# Informe Teorico - Uso de Conceptos en el Programa

## Listas

Las listas se utilizan en el programa para almacenar y gestionar la coleccion de paises. La lista principal `PAISES` contiene todos los paises cargados en memoria, donde cada elemento es un diccionario que representa un pais. Ademas, se emplean listas temporales para almacenar resultados de busquedas y filtrados, como cuando se buscan coincidencias exactas o parciales de nombres de paises, o cuando se filtran paises por continente o por rangos de poblacion y superficie. Las listas tambien se utilizan para almacenar los encabezados de las columnas del archivo CSV y para construir las filas que se escribiran en el archivo.

## Diccionarios

Los diccionarios son la estructura de datos fundamental para representar cada pais en el programa. Cada pais se almacena como un diccionario con las claves 'Nombre', 'Poblacion', 'Superficie' y 'Continente', lo que permite acceder facilmente a cada atributo del pais. Tambien se utilizan diccionarios para normalizar las filas leidas del archivo CSV, convirtiendo las claves a minusculas y eliminando espacios. Adicionalmente, se emplea un diccionario para realizar el conteo de paises por continente al calcular las estadisticas, donde cada clave representa un continente y su valor es la cantidad de paises que pertenecen a ese continente.

## Funciones

El programa esta organizado mediante funciones que encapsulan diferentes funcionalidades. Se definen funciones para cargar y guardar datos desde y hacia archivos CSV, funciones de validacion para asegurar que los datos ingresados por el usuario sean correctos, funciones para realizar busquedas y filtrados, funciones para ordenar la lista de paises, y funciones para calcular y mostrar estadisticas. Esta organizacion modular permite reutilizar codigo, facilitar el mantenimiento y hacer el programa mas legible. La funcion principal `main()` coordina todas estas operaciones mediante un menu interactivo.

## Condicionales

Las estructuras condicionales se utilizan extensivamente en todo el programa para controlar el flujo de ejecucion. Se emplean para validar si un archivo existe antes de intentar leerlo, para verificar si los datos ingresados son validos, para determinar si un pais ya existe antes de agregarlo, para comprobar si se encontraron resultados en las busquedas, y para validar que los rangos minimo y maximo sean correctos en los filtros. Las condicionales tambien se usan en el menu principal para determinar que operacion ejecutar segun la opcion seleccionada por el usuario, y en las funciones de validacion para repetir la solicitud de datos hasta que se ingresen valores correctos.

## Ordenamientos

El programa implementa un algoritmo de ordenamiento para organizar la lista de paises segun diferentes criterios. Se utiliza el algoritmo de ordenamiento burbuja (bubble sort) que permite ordenar los paises por nombre, poblacion o superficie. El algoritmo recorre la lista comparando elementos adyacentes y los intercambia si es necesario segun el criterio seleccionado y la direccion del ordenamiento (ascendente o descendente). Esta funcionalidad permite al usuario visualizar los datos de manera organizada, facilitando la comparacion y analisis de la informacion.

## Estadisticas Basicas

Se implementan calculos estadisticos basicos para proporcionar informacion agregada sobre los paises almacenados. El programa calcula el pais con mayor y menor poblacion mediante la comparacion de valores en la lista. Tambien se calculan promedios de poblacion y superficie sumando todos los valores y dividiendo por la cantidad de paises. Adicionalmente, se realiza un conteo de paises agrupados por continente, lo que permite conocer la distribucion geografica de los datos. Estas estadisticas ofrecen una vision general y resumida de la informacion almacenada.

## Archivos CSV

El programa utiliza archivos CSV para la persistencia de datos, permitiendo que la informacion se mantenga entre diferentes ejecuciones del programa. Se implementa la lectura de archivos CSV para cargar los paises al inicio del programa, validando que el archivo exista, que tenga el formato correcto con las columnas requeridas, y procesando cada fila para convertir los datos al formato interno del programa. De manera similar, se implementa la escritura de archivos CSV para guardar todos los cambios realizados durante la ejecucion, escribiendo primero los encabezados y luego cada pais como una fila en el archivo. Esta persistencia permite que el usuario pueda trabajar con los mismos datos en sesiones diferentes del programa.

