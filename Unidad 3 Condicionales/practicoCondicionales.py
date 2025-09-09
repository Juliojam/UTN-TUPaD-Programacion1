
print('TRABAJO PRACTICO N° 3 - CONDICIONALES')

print(' 1)Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad".')
#solicita al usuario que ingrese sus edad por teclado, int hacer referencia a que la variable ingresada es un número entero
edad = int(input('Ingrese su edad por favor...'))
#if evalua la condición, en caso de que la edad ingresada sea mayor o igual a 18 imprime la frase "Es Mayor de edad"
if edad >= 18:
    print('Es Mayor de edad') 
    

print('2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6,'
      'deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”')
#solicita al usuario que ingrese una nota para ser evaluada, la variable ingresada será de tipo decimal por eso usamos float 
nota = float(input('Ingrese la calificación recibida'))
#Evalua si la nota ingresada es por lo menos 6 para considerarla aprobado o no
if nota >= 6:
    print('Aprobado')
else:
    print('Desaprobado')
    
    
print('3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par,')
print('imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".')   
#Solicita al usuario que ingrese por teclado un número par
numeroPar = int(input('Ingrese un número Par'))
#El if evalua si el número ingresado es par o no a traves de la operacion modulo (%) la cual arroja el resto de la división,
# que al dividirse por 2 y resultar 0 es par indudablemente. Caso contrario aclara, y solicita ingresar un número par. Luego imprime
if numeroPar % 2 == 0:
    print('Ha ingresado un número Par')
else:
    print('Por favor, ingrese un número Par')
    

print('4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:')
print('* Niño/a: menor de 12 años.')
print('* Adolescente: mayor o igual que 12 años y menor que 18 años.')
print('* Adulto/a joven: mayor o igual que 18 años y menor que 30 años.')
print('* Adulto/a: mayor o igual que 30 años.')
#Solicita al usuario ingresar su edad
edad = int(input('Ingrese su edad por favor'))
#el if analiza la categoría a la que corresponde la edad del usuario según los ragos de edades dados en el ejercicio e imprime la misma
if edad < 12:
    print('Niño/a')
elif edad >= 12 and edad < 18:
    print('Adolescente')
elif edad >= 18 and edad < 30:
    print('Adulto/a joven')
else:
    print('Adulto/a')
    
    
print('5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres')
print('(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en')
print('pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por')
print('pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".')
#Solicita al usuario que ingrese una contraseña con un rango de caracteres especificos
contraseña = str(input("Ingrese por favor una contraseña de entre 8 y 14 caracteres por favor"))
#if corrobora que la contraseña ingresada siga los parametros solicitados, la funcion len() sirve como si fuera un número, 
#el número de len() es el número de la cantidad de caracteres que ingreso el usuario. si esta dentro de los parametros es correcta, 
#sino pide un reingreso de contraseña con los caracteres solicitados
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor ingrese una contraseña de entre 8 y 14 caracteres')
    

print('6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda,')
print('la mediana y la media de dichos números.')
print('escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y')
print('las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.')
#importa una funcion o paquete externo que permite usar funciones de calculos estadisticos    
from statistics import mode, median, mean
import random
#se genera una lista de 50 números aleatorios de entre el 1 y el 100.
numero_aleatorios = [random.randint(1, 100) for i in range(50)]
#imprime la lista aleatoria generada
print(numero_aleatorios)
#se asignan a las variables media, mediana y moda los calculos estadisticos correspondientes a sus nombres tomando el listado generado precedentemente
media = mean(numero_aleatorios)
moda = mode(numero_aleatorios)
mediana = median(numero_aleatorios)
#se imprimen los calculos de la media, mediana y moda precedidos por un string que los nombra para no perder referencia de cual es cual
print('Media ', media)
print('Mediana ', mediana)
print('Moda ', moda)
#if evalua las condiciones aclaradas en el ejercicio para determinar en base a los calculos anteriores el sesgo estadistico o su ausencia.
if media > mediana and mediana > moda:
    print('Sesgo Positivo o a la Derecha')
elif media < mediana and mediana < moda:
    print('Sesgo Negativo o a la izquierda') 
elif media == mediana == moda:
    print('Sin sesgo')
else:
    print("No se cumple ninguna de las condiciones de sesgos definidas")

print('7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,')
print('añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar') 
print('el string tal cual lo ingresó el usuario e imprimirlo por pantalla.')
#solicita el ingreso por teclado del usuario de una palabra o frase
frase = input('Ingrese una palabra o frase')
#la condición del if evalua que la ultima letra de la frase o palabra ingresas sea igual a una vocal en minúsculas con la funcion lower,
#para evitar que el usuario ingrese mayúsculas y no sea tenida en cuenta. luego imprime la misma frase ingresada con un ! al final si termina en vocal
#caso contrario imprime la frase tal cual se ingreso
if frase[-1].lower() in 'aeiou':
    print(frase + '!')
else:
    print(frase)


print('8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:')
print('1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.')
print('2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.')
print('3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.')
print('El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e') 
print('imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir')
print('entre mayúsculas y minúsculas.')
#Solicita al usuario que ingrese su nombre
name = input("Escriba su nombre")
#Solicita al usuario que ingrese un número del 1 al 3 de acuerdo a la descripción señalada en el input
opcionesNombres = input("Escriba 1 si quiere su nombre en mayúsculas, escriba 2 si quiere su nombre en minúsculas o 3 solo con la 1ra letra en mayúsculas")
#if evalua las opciones ofrecidas e ingresada por el usuario
#la función upper() toma el nombre ingresado y lo lleva en su totalidad a mayúsculas 
if opcionesNombres == "1":
     print(name.upper())
#la función lower() toma el nombre ingresado y lo lleva en su totalidad a minusculas 
elif opcionesNombres == "2":
    print(name.lower())
#la función title() toma el nombre ingresado y lo transforma a mayúsculas las primeras letras y el resto las mantiene como minúsculas
elif opcionesNombres == "3":
    print(name.title())


ejercicio9 = """
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
"""
print(ejercicio9)
#Solicita al usuario que ingrese un número por teclado que puede ser decimal (float)
magnitudTerremoto = float(input('Ingrese la magnitud del terremoto según escala Richter'))
#analiza los rangos de la escala richter, e imprime la leyenda correspondiente, acorde a la clasificación otorgada en el ejercicio
if magnitudTerremoto < 3:
    print('"Muy leve" (imperceptible)')
elif magnitudTerremoto >= 3 and magnitudTerremoto < 4:
    print('"Leve" (ligeramente perceptible)')
elif magnitudTerremoto >= 4 and magnitudTerremoto < 5:
    print('"Moderado" (sentido por personas, pero generalmente no causa daños)')
elif magnitudTerremoto >= 5 and magnitudTerremoto < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles)')
elif magnitudTerremoto >= 6 and magnitudTerremoto < 7:
    print('"Muy Fuerte" (puede causar daños significativos)')
    
    
ejercicio10 = """10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano."""

print(ejercicio10)
print('INGRESE LOS DATOS QUE SE SOLICITAN A CONTINUACION PARA DETERMINAR A QUE ESTACION DEL AÑO CORRESPONDE')
#Solicita que el usuario ingrese por teclado un día
dia = int(input("Ingrese el día del mes "))
#Solicita que el usuario ingrese por teclado un mes expresado en números (donde 1 sería enero y 12 diciembre) 
mes = str(input('Ingrese un mes del año ingresando un número (1-12) dependiendo del mes que corresponda '))
#solicita que se ingrese por teclado el hemisferio del cual se quiere conocer la estación del año. "N" si es norte, y cualquier otra letra si es Sur.
variableHemisferio = str(input('Ingrese "n" para Hemisferio Norte u otra letra para Hemisferio Sur'))  
hemisferio = "N" if variableHemisferio.upper() == "N" else "S"  
#evalua las 3 variables ingresadas por teclado: día, mes y hemisferio para determinar la estación del año e imprimir la correspondiente 
if dia >= 21 and dia <= 31 and mes == "12":
    if hemisferio == "N":
        print("Invierno")
    else:
        print("Verano") 
elif dia >= 1 and dia <= 31 and mes == "1":
    if hemisferio == "N":
        print("Invierno") 
    else:
        print("Verano")
elif dia >= 1 and dia <= 29 and mes == "2":
    if hemisferio == "N":
        print("Invierno") 
    else:
        print("Verano")
elif dia >= 1 and dia <= 20 and mes == "3":
    if hemisferio == "N":
        print("Invierno") 
    else:
        print("Verano")
elif dia >= 21 and dia <= 31 and mes == "3":
    if hemisferio == "N":
        print("Primavera") 
    else:
        print("Otoño")
elif dia >= 1 and dia <= 30 and mes == "4":
    if hemisferio == "N":
        print("Primavera") 
    else:
        print("Otoño")
elif dia >= 1 and dia <= 31 and mes == "5":
    if hemisferio == "N":
        print("Primavera") 
    else:
        print("Otoño")
elif dia >= 1 and dia <= 20 and mes == "6":
    if hemisferio == "N":
        print("Primavera") 
    else:
        print("Otoño")
elif dia >= 21 and dia <= 30 and mes == "6":
    if hemisferio == "N":
        print("Verano") 
    else:
        print("Invierno")
elif dia >= 1 and dia <= 31 and mes == "7" or dia <= 31 and mes == "8":
    if hemisferio == "N":
        print("Verano") 
    else:
        print("Invierno")
elif dia >= 1 and dia <= 20 and mes == "9": 
    if hemisferio == "N":
        print("Verano") 
    else:
        print("Invierno")
elif dia >= 21 and dia <= 30 and mes == "9": 
    if hemisferio == "N":
        print("Otoño") 
    else:
        print("Primavera")
elif dia >= 1 and dia <= 31 and mes == "10": 
    if hemisferio == "N":
        print("Otoño") 
    else:
        print("Primavera")
elif dia >= 1 and dia <= 30 and mes == "11": 
    if hemisferio == "N":
        print("Otoño") 
    else:
        print("Primavera")
elif dia >= 1 and dia <= 20 and mes == "12": 
    if hemisferio == "N":
        print("Otoño") 
    else:
        print("Primavera")



