#TODO EL TRABAJO REALIZADO

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Ejercicio N° 1")

print("Hola Mundo!")

'''
2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.
'''
print("Ejercicio N° 2")

nombre = input("por favor ingrese su nombre ")
print(f"Hola ",nombre,"!")

"""
3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
"""
print("Ejercicio N° 3")

name = input("por favor ingrese su nombre ")
last_Name = input("por favor ingrese su apellido ")
age = input("por favor ingrese su edad ")
residence = input("por favor ingrese su residencia ")

print (f"Soy ", name, " ",last_Name,","," tengo ", age, " años y vivo en ", residence)

"""
4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.
"""
print("Ejercicio N° 4")

radio = input("ingrese el radio del circulo")
num_Pi = float(3.141592)
area_Del_Circulo = num_Pi * float(radio) ** 2
perimetro_Del_Circulo = float(radio) * float(num_Pi) * 2

print("El Área del Circulo es",float(area_Del_Circulo))
print("El perimetro o circunferencia del Circulo es",float(perimetro_Del_Circulo))

"""
5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.
"""
print("Ejercicio N° 5")

segundos = input("ingrese la cantidad de segundos deseada")

horas_equivalentes = float(segundos) / 3600

print(segundos, " segundos equivalen a ", horas_equivalentes, " horas")

"""
6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.
"""

print("Ejercicio N° 6")

num1 = int(input("Ingrese el número del cual desee la tabla de multiplicar"))

multiplicacion_Por_0 = num1 * 0
multiplicacion_Por_1 = num1 * 1
multiplicacion_Por_2 = num1 * 2
multiplicacion_Por_3 = num1 * 3
multiplicacion_Por_4 = num1 * 4
multiplicacion_Por_5 = num1 * 5
multiplicacion_Por_6 = num1 * 6
multiplicacion_Por_7 = num1 * 7
multiplicacion_Por_8 = num1 * 8
multiplicacion_Por_9 = num1 * 9
multiplicacion_Por_10 = num1 * 10

print(num1, "x 0 = ",multiplicacion_Por_0)
print(num1, "x 1 = ",multiplicacion_Por_1)
print(num1, "x 2 = ",multiplicacion_Por_2)
print(num1, "x 3 = ",multiplicacion_Por_3)
print(num1, "x 4 = ",multiplicacion_Por_4)
print(num1, "x 5 = ",multiplicacion_Por_5)
print(num1, "x 6 = ",multiplicacion_Por_6)
print(num1, "x 7 = ",multiplicacion_Por_7)
print(num1, "x 8 = ",multiplicacion_Por_8)
print(num1, "x 9 = ",multiplicacion_Por_9)
print(num1, "x 10 = ",multiplicacion_Por_10)

"""
7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos,
dividirlos, multiplicarlos y restarlos.
"""
print("Ejercicio N° 7")

num_Uno = float(input("Ingrese un número distinto de 0 para realizar las operaciones"))
num_Dos = float(input("Ingrese otro número distinto de 0 para realizar las operaciones"))

suma = num_Uno + num_Dos
resta = num_Uno - num_Dos
multip = num_Uno * num_Dos
division = num_Uno / num_Dos

print("El resultado de la SUMA ambos números es = ", float(suma))
print("El resultado de la RESTA de ambos números es = ", float(resta))
print("El resultado de la MULTIPLICACION de ambos números es = ", float(multip))
print("El resultado de la DIVISION ambos números es = ", float(division))

"""
8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
"""
print("Ejercicio N° 8")

print("Para calcular su indice de masa corporal ingrese los siguientes datos")

peso_En_Kilos = float(input("Ingrese su peso en Kilos"))
altura = float(input("Ingrese su altura expresado en metros"))

IMC = peso_En_Kilos / (altura**2)

print("Tu Indice de Masa Corporal (IMC) es =", IMC)

"""
9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla
su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
"""

print("Ejercicio N° 9")

celusius = float(input("Ingrese una temperatura en grados Celsius"))

fahrenheit = 9/5 * celusius + 32

print("La temperatura expresado en fahrenheit equivalente es =", fahrenheit)

"""
10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
"""

print("Ejercicio N° 10")

numero1 = float(input("Ingrese un número"))
numero2 = float(input("Ingrese otro número"))
numero3 = float(input("Ingrese otro número"))

sumatoria = numero1 + numero2 + numero3
promedio = sumatoria / 3

print("El promedio de los 3 números ingresados es =", promedio)