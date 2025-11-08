#1) Dado el diccionario precios_frutas 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las siguientes frutas con sus respectivos precios:
#Naranja = 1200
#Manzana = 1500
#Pera = 2300

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
# actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
#crear una lista que contenga únicamente las frutas sin los precios.

listado_de_keys = precios_frutas.keys()

print(listado_de_keys)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

diccionario_telefonico = {}
contador = 0

while contador < 5:
    contacto_telefonico = str(input('Ingrese el nombe del contacto...'))
    numero_telefonico = int(input('Ingrese el número telefonico del contacto...'))
    diccionario_telefonico[contacto_telefonico]=numero_telefonico
    contador +=1

opcion = 0

while  opcion != 3:
    print("-----MENU-----")
    print("opcion 1: listar contactos almacenados")
    print("opción 2: ver el número telefonico ingresando el nombre del contacto")
    print("Opcion 3: Ingrese 3 para salir")

    opcion = int(input("Ingrese una opción..."))

    if opcion == 1:
        print(diccionario_telefonico)
    if opcion == 2:
        nombre = str(input("Ingresar nombre de persona para ver su número telefonico..."))
        telefono = diccionario_telefonico.get(nombre)
        print(telefono)

#5) Solicita al usuario una frase e imprime:
#* Las palabras únicas (usando un set).
#* Un diccionario con la cantidad de veces que aparece cada palabra.

import string

frase = input("Por favor, introduce una frase: ")
    
frase_limpia = frase.lower().translate(str.maketrans('', '', string.punctuation))
    
palabras = frase_limpia.split()
    
palabras = [palabra for palabra in palabras if palabra]

print("--- Resultados del Análisis ---")
    
palabras_unicas = set(palabras)
    
print("Palabras Únicas (Set):")
print(palabras_unicas)
    
frecuencia_palabras = {}
for palabra in palabras:
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
        
print("Frecuencia de Palabras (Diccionario):")
print(frecuencia_palabras)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

def calcular_promedios_alumnos_simple(cantidad_alumnos=3):
    
    alumnos = {}
        
    print(f"**Ingrese los datos para {cantidad_alumnos} alumnos.**")
    
    for i in range(cantidad_alumnos):
        print(f"\n--- Alumno {i + 1} de {cantidad_alumnos} ---")
        
        nombre = input("➡️ Ingrese el nombre del alumno: ").strip().capitalize()
        
        notas_lista = []
        for j in range(3):
            nota = float(input(f"   Ingrese la nota {j + 1}: "))
            notas_lista.append(nota)
        
        alumnos[nombre] = tuple(notas_lista)
    
    print("\n" + "="*40)
    print("       PROMEDIOS DE ALUMNOS ")
    print("="*40)
        
    for nombre, notas in alumnos.items():
        
        promedio = sum(notas) / len(notas)
                
        print(f"**{nombre}**: Notas {notas} -> Promedio: **{promedio:.2f}**")
    
    print("\n--- Fin del Proceso ---")

if __name__ == "__main__":
    calcular_promedios_alumnos_simple(3)
    

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

aprobados_parcial1 = {"juan", "ana", "jorge", "luisa", "gregorio", "elena", "juana"}
aprobados_parcial2 = {"gladys", "julio", "juan", "luisa", "victor", "elena", "martin"}

print("--- Listas de Aprobados ---")
print(f"Parcial 1 (Set 1): {aprobados_parcial1}")
print(f"Parcial 2 (Set 2): {aprobados_parcial2}")

ambos_parciales = aprobados_parcial1.intersection(aprobados_parcial2)

print("\n--- Resultados ---")
print("Aprobados AMBOS parciales (Intersección):")
print(ambos_parciales)

solo_uno = aprobados_parcial1.symmetric_difference(aprobados_parcial2)

print("\nAprobados SOLO UNO de los parciales (Diferencia Simétrica):")
print(solo_uno)

al_menos_uno = aprobados_parcial1.union(aprobados_parcial2)

print("\nLista TOTAL de aprobados (al menos uno) (Unión):")
print(al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.


inventario = {
    "Manzana": 50,
    "Banana": 120,
    "Leche": 30
}

def consultar_stock_sin_excepciones(producto):
    """Consulta e imprime el stock de un producto sin usar try/except."""
    
    print("\n--- Consulta de Stock ---")
    if producto in inventario:
        stock = inventario[producto]
        print(f"El stock actual de **{producto}** es de **{stock}** unidades.")
    else:
        print(f"El producto **{producto}** no se encuentra en el inventario.")
    print("-------------------------")

def actualizar_stock_sin_excepciones(producto, unidades):
    """Agrega unidades si el producto existe o lo crea si no existe."""
    
    if producto in inventario:        
        inventario[producto] += unidades
        print(f"\nStock actualizado para **{producto}**.")
        print(f"   Unidades añadidas: **{unidades}**. Nuevo stock: **{inventario[producto]}**.")
    else:        
        inventario[producto] = unidades
        print(f"\nNuevo producto agregado: **{producto}**.")
        print(f"   Stock inicial: **{unidades}**.")

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n" + "="*40)
    print("      SISTEMA DE GESTIÓN DE INVENTARIO")
    print("="*40)
    print("1. Consultar stock de un producto.")
    print("2. Agregar unidades / Agregar nuevo producto.")
    print("3. Mostrar inventario completo.")
    print("4. Salir.")
    print("="*40)

def ejecutar_inventario_sin_excepciones():
    """Función principal para interactuar con el usuario."""
    while True:
        mostrar_menu()
                
        opcion = input("➡️ Elige una opción (1-4): ")
        
        if opcion == '1':            
            producto = input("Ingrese el nombre del producto a consultar: ").strip().capitalize()
            consultar_stock_sin_excepciones(producto)            
        elif opcion == '2':            
            producto = input("Ingrese el nombre del producto: ").strip().capitalize()                        
            unidades_str = input(f"Ingrese la cantidad de unidades a agregar para '{producto}' (entero): ")
            unidades = int(unidades_str) 

            actualizar_stock_sin_excepciones(producto, unidades)
            
        elif opcion == '3':            
            print("\n" + "="*40)
            print("         INVENTARIO COMPLETO")
            print("="*40)
            if inventario:
                for producto, stock in inventario.items():
                    print(f"  {producto}: {stock} unidades")
            else:
                print("El inventario está vacío.")
            print("="*40)

        elif opcion == '4':            
            print("\n¡Gracias por usar el sistema de inventario! ")
            break            
        else:
            print("\n Opción no válida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    ejecutar_inventario_sin_excepciones()
    
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

def gestionar_agenda():
        
    agenda = {
        ("lunes", "10:00"): "Reunión de planificación",
        ("martes", "15:00"): "Clase de inglés",
        ("miércoles", "09:30"): "Entrenamiento en gimnasio",
        ("jueves", "18:00"): "Proyecto Python",
        ("viernes", "11:00"): "Almuerzo con equipo"
    }

    print("---Agenda de Eventos---")
    print("La agenda está inicializada con los siguientes eventos:")
        
    for (dia, hora), evento in agenda.items():
        print(f"[{dia.capitalize()} a las {hora}] -> {evento}")

    print("\n" + "="*40)
    print("CONSULTA DE EVENTO")
    print("="*40)
    
    dia_consulta = input("Ingrese el día (ej: lunes): ").strip().lower()
        
    hora_consulta = input("Ingrese la hora (ej: 10:00): ").strip()
    
    clave_consulta = (dia_consulta, hora_consulta)

    print("\n--- Resultado de la Consulta ---")
        
    evento_encontrado = agenda.get(clave_consulta)

    if evento_encontrado:
        print(f"Hay un evento programado para el **{dia_consulta.capitalize()} a las {hora_consulta}**:")
        print(f"   **{evento_encontrado}**")
    else:
        print(f"No hay eventos programados para el {dia_consulta.capitalize()} a las {hora_consulta}.")

if __name__ == "__main__":
    gestionar_agenda()
    
    
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

def invertir_diccionario_paises():
    
    original = {
        "Argentina": "Buenos Aires", 
        "Chile": "Santiago", 
        "Perú": "Lima",
        "Colombia": "Bogotá",
        "Uruguay": "Montevideo"
    }

    print("--- Diccionario Original (País: Capital) ---")
    print(original)
     
    invertido = {capital: pais for pais, capital in original.items()}

    print("\n--- Diccionario Invertido (Capital: País) ---")
    print(invertido)

if __name__ == "__main__":
    invertir_diccionario_paises()