print("1) Crear una lista con las notas de 10 estudiantes.")
print("• Mostrar la lista completa.")
print("• Calcular y mostrar el promedio.")
print("• Indicar la nota más alta y la más baja.")

notas = [7,2,9,5,3,8,10,8,6,4]
suma = 0
nota_mas_alta = notas[0]
nota_mas_baja = notas[0]

#listar nomas + promedio
for i in notas:
    suma = suma + i

longitud_lista = len(notas)

promedio = suma / longitud_lista

#nota mas alta
for j in notas:
    if j > nota_mas_alta:
        nota_mas_alta = j

    if j < nota_mas_baja:
        nota_mas_baja = j


print(f"Listado de Notas Alumnos {notas}")
print(f"suma total = {suma}, promedio = {promedio}")
print(f"Nota mas alta {nota_mas_alta}")
print(f"Nota mas baja {nota_mas_baja}")

print("2) Pedir al usuario que cargue 5 productos en una lista.")
print("• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().")
print("• Preguntar al usuario qué producto desea eliminar y actualizar la lista.")

productos = []

while len(productos) < 5:
    producto_a_ingresar = str(input("Ingrese el nombre del producto... "))
    productos.append(producto_a_ingresar)

productos_ordenados = sorted(productos)

print("Productos ", productos_ordenados)

import random
print("3) Generar una lista con 15 números enteros al azar entre 1 y 100.")
print("• Crear una lista con los pares y otra con los impares.")
print("• Mostrar cuántos números tiene cada lista.")

lista = []
lista_pares = []
lista_impares = []

while len(lista) < 15:
    numero_azar = random.randint(1,100)
    lista.append(numero_azar)

print(lista)

for num in lista:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

elementos_pares = len(lista_pares)
elementos_impares = len(lista_impares)        

print(f"Lista números pares , {lista_pares}, esta lista tiene {elementos_pares} números impares")
print(f"Lista números impares , {lista_impares}, esta lista tiene {elementos_impares} números impares")

print("4) Dada una lista con valores repetidos:")
print("• Crear una nueva lista sin elementos repetidos.")
print("• Mostrar el resultado.")

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista_sin_repetidos = []

for i in datos:
    if i not in lista_sin_repetidos:
        lista_sin_repetidos.append(i)

print(f"Lista sin repetidos {lista_sin_repetidos}")


print("5) Crear una lista con los nombres de 8 estudiantes presentes en clase.")
print("• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.")
print("• Mostrar la lista final actualizada.")

lista_estudiantes = []
cuenta = 0

while len(lista_estudiantes) < 8:
    nombre_estudiante = str(input("Ingrese el nombre de un estudiante "))
    lista_estudiantes.append(nombre_estudiante)

print(lista_estudiantes)

opcion1 = 1
opcion2 = 2

ingrese_opcion = int(input("ingrese 1 para agregar un alumno a la lista, 2 para quitar un alumno de la lista o cualquier otro número para dejar la lista como está "))

if ingrese_opcion == 1:
    agregar_estudiante = lista_estudiantes.append(str(input(lista_estudiantes)))
elif ingrese_opcion == 2:
    quitar_estudiante = str(input("Escriba el nombre del alumno a quitar de la lista "))
    lista_estudiantes.remove(quitar_estudiante)

print(lista_estudiantes)

print("6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el")
print("último pasa a ser el primero).")

lista_original = [45, 98, 55, 77, 66, 21, 18]

ultimo_numero = lista_original[-1]
resto = lista_original[:-1]

lista_rotada = [ultimo_numero] + resto

print(f"Lista Original {lista_original}")
print(f"Lista con rotacion {lista_rotada}")

print("7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.")
print("• Calcular el promedio de las mínimas y el de las máximas.")
print("• Mostrar en qué día se registró la mayor amplitud térmica.")

temperaturas = [
    [10, 16],
    [8, 13],
    [12, 25],
    [7, 22],
    [19, 31],
    [18, 32],
    [19, 26]
]

suma_minimas = 0
suma_maximas = 0
#bucle for realiza sumatoria de las minimas y las maximas por separado
for h in range(len(temperaturas)):
    minimas = temperaturas[h][0]
    suma_minimas += minimas
    maximas = temperaturas[h][1]
    suma_maximas += maximas

#realiza el promedio dividiendo por la cantidad de elementos las sumatoria de minima y maxima
promedio_minimas = suma_minimas / len(temperaturas)
promedio_maximas = suma_maximas / len(temperaturas)

print(f"El promedio de temperaturas minimas es {promedio_minimas:.2f}")
print(f"El promedio de temperaturas maximas es {promedio_maximas:.2f}")

amplitud_termica = 0
for g in range(len(temperaturas)):
    diferencia_temperatura = (temperaturas[g][1])-(temperaturas[g][0])
    if diferencia_temperatura > amplitud_termica:
        amplitud_termica = diferencia_temperatura
        dia_mayor_amplitud = g+1
        dia_amplitud = temperaturas[g]
        
print(f"Mayor amplitud termica... {amplitud_termica}° el dia N° {dia_mayor_amplitud} cuyas temp max y min fueron {dia_amplitud}")

print("8) Crear una matriz con las notas de 5 estudiantes en 3 materias.")
print("• Mostrar el promedio de cada estudiante.")
print("• Mostrar el promedio de cada materia.")

notas_alumnos = [
    [5, 8, 6],#19 => /3= 6.33
    [9, 4, 10],#23 => /3= 7.66
    [6, 3, 8],#17 => /3= 5.66
    [7, 7, 8],#22 => /3= 7.33
    [4, 10, 8]#22 => /3= 7.33
]
#Bucle promedio por alumno
for i, p in enumerate(notas_alumnos, 1):
    suma_notas_alumno = 0
    conteo_notas = 0
    for q in p:
        suma_notas_alumno += q
        conteo_notas += 1
    promedio_alumnos = suma_notas_alumno / conteo_notas
    
    print(f"promedio alumno {i}: {promedio_alumnos:.2f}")

#bucle promedio por materia
num_materias = len(notas_alumnos[0])  
num_estudiantes = len(notas_alumnos)  

print("\nPromedios de las materias:")

for j in range(num_materias):
    suma_materia = 0
    for i in range(num_estudiantes):
        suma_materia += notas_alumnos[i][j]  
    promedio_materia = suma_materia / num_estudiantes
    print(f"Promedio de la materia {j + 1}: {promedio_materia:.2f}")


print("9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).")
print("• Inicializarlo con guiones "-" representando casillas vacías.")
print("• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar 'X' o 'O'.")
print("• Mostrar el tablero después de cada jugada.")

tablero = []

for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

for fila in tablero:
    for celda in fila:
        print(celda, end= " ")
    print()

jugador = "X"
jugadas = 0        

while jugadas < 9:
    print(f"\n Turno del jugador {jugador}")

    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))

    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Posición fuera de rango. Intenta de nuevo")
        continue

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        jugadas +=1
    else:
        print("Casilla ocupada. Intenta de nuevo")
        continue

    for fila in tablero:
        for celda in fila:
            print(celda, end= " ")
        print()

    if jugador =="X":
        jugador = "O"
    else:
        jugador = "X"


print("10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.")
print("• Mostrar el total vendido por cada producto.")
print("• Mostrar el día con mayores ventas totales.")
print("• Indicar cuál fue el producto más vendido en la semana.")

ventas = [
    [5,3,2,7,4,6,3],
    [2,8,1,3,5,7,4],
    [6,4,7,2,8,8,5],
    [3,6,4,5,2,9,7]
]

totales_productos = []

for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto += ventas[i][j]
    totales_productos.append(total_producto)
    print(f"Producto {i+1}: {total_producto}")
    
mayor_ventas = 0
dia_mayor = 0

for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    print(f"Total del día {j+1}: {total_dia}")
    if total_dia > mayor_ventas:
        mayor_ventas = total_dia
        dia_mayor = j
        

print(f"\nEl día con mayores ventas fue el {dia_mayor+1}, con {mayor_ventas} ventas.")    

mayor_producto = 0
indice_mayor = 0

for i in range(4):
    if totales_productos[i] > mayor_producto:
        mayor_producto = totales_productos[i]
        indice_mayor = i
        
print(f"\nEl producto mas vendido fue el {indice_mayor+1}, con {mayor_producto} ventas.")


