print("EJERCICIO 1: Crear una función llamada imprimir_hola_mundo que imprima por")
print("pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el")
print("programa principal.")

def imprimir_hola_mundo ():
    print("HOLA MUNDO!")

imprimir_hola_mundo()

print("EJERCICIO 2: Crear una función llamada saludar_usuario(nombre) que reciba")
print("como parámetro un nombre y devuelva un saludo personalizado.")
print("Por ejemplo, si se llama con saludar_usuario(Marcos), deberá devolver:")
print("“Hola Marcos!”. Llamar a esta función desde el programa")
print("principal solicitando el nombre al usuario.")

def saludar_usuario(nombre):
    nombre = input("Ingrese su nombre...")
    print(f"Hola {nombre}!")
    
saludar_usuario("julio")

print(" EJERCICIO 3: printCrear una función llamada informacion_personal(nombre, apellido,")
print("edad, residencia) que reciba cuatro parámetros e imprima: “Soy")
print("[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir")
print("los datos al usuario y llamar a esta función con los valores ingresados.")

def informacion_personal(nombre, apellido, edad, residencia):
    nombre = str(input("Ingrese su nombre..."))
    apellido = str(input("Ingrese su apellido..."))
    edad = int(input("ingrese su edad..."))
    residencia = str(input("Ingrese su ciudad de residencia..."))
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    
informacion_personal("nombre", "apellido", "edad", "residencia")

print("EJERCICIO 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio")
print("como parámetro y devuelva el área del círculo. calcular_perimetro_")
print("circulo(radio) que reciba el radio como parámetro y devuelva")
print("el perímetro del círculo. Solicitar el radio al usuario y llamar ambas")
print("funciones para mostrar los resultados.")
import math

radio = float(input("Ingrese el radio del circulo"))

def calcular_area_circulo(radio):
    pi = math.pi
    area_circulo = pi * radio ** 2
    return area_circulo
    

def calcular_perimetro_circulo(radio):
    pi = math.pi
    perimetro_circulo = 2 * pi * radio
    return perimetro_circulo

print(f"El Area del círculo es...{calcular_area_circulo(radio):.2f}")
print(f"El Perimetro del círculo es...{calcular_perimetro_circulo(radio):.2f}")

print("EJERCICIO 5: Crear una función llamada segundos_a_horas(segundos) que reciba")
print("una cantidad de segundos como parámetro y devuelva la cantidad")
print("de horas correspondientes. Solicitar al usuario los segundos y mostrar")
print("el resultado usando esta función.")

segundos = int(input("Ingrese los segundos que desea convertir a horas")) 

def segundos_a_horas(segundos):
    horas = segundos / 60
    return horas

print(f"Las horas equivalentes a {segundos} segundos es {segundos_a_horas(segundos):.2f} horas")

print("EJERCICIO 6: Crear una función llamada tabla_multiplicar(numero) que reciba un")
print("número como parámetro y imprima la tabla de multiplicar de ese")
print("número del 1 al 10. Pedir al usuario el número y llamar a la función.")


def tabla_multiplicar(num):
    for i in range(1,11):
        multiplicacion = num * i
        print(f"{num} x {i} = {multiplicacion}")
    
num = int(input("Ingrese un número para crear su tabla de multiplicación"))

tabla_multiplicar(num)

print("EJERCICIO 7: Crear una función llamada operaciones_basicas(a, b) que reciba")
print("dos números como parámetros y devuelva una tupla con el resultado")
print("de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados")
print("de forma clara.")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    print(f"el resultado de la suma {a} + {b} = {suma}")
    print(f"el resultado de la resta {a} - {b} = {resta}")
    print(f"el resultado de la multiplicacion {a} x {b} = {multiplicacion}")
    print(f"el resultado de la division {a} / {b} = {division}")
    return (suma, resta, multiplicacion, division)
    
a = int(input("Ingrese el primer número para realizar las operaciones básicas"))
b = int(input("Ingrese el segundo número para realizar las operaciones básicas"))
    
operaciones_basicas(a, b)

print("EJERCICIO 8: Crear una función llamada calcular_imc(peso, altura) que reciba el")
print("peso en kilogramos y la altura en metros, y devuelva el índice de")
print("masa corporal (IMC). Solicitar al usuario los datos y llamar a la función")
print("para mostrar el resultado con dos decimales.")

def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

peso = float(input("Ingrese su peso expresado en kilogramos..."))
altura = float(input("Ingrese su altura expresada en metros..."))

print(f"El ratio de IMC es ={calcular_imc(peso, altura)}")

imc = calcular_imc(peso, altura)

if imc < 18.5:
    print("Peso inferior al normal")
elif imc >= 18.5 and imc <= 24.90:
    print("Peso Normal")
elif imc > 24.9 and imc < 29.90:
    print("Peso superior al normal")
else:
    print("Obesidad")
    
print("EJERCICIO 9: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba")
print("una temperatura en grados Celsius y devuelva su equivalente en")
print("Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el")
print("resultado usando la función.")

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit
    
celsius = float(input("Ingrese los grados en CELSIUS para recibir su equivalente en FAHRENHEIT..."))

print(f"Los grados equivalentes a {celsius} grados celsius en fahrenheit son {celsius_a_fahrenheit(celsius)} grados fahrenheit...")


print("EJERCICIO 10: Crear una función llamada calcular_promedio(a, b, c) que reciba")
print("tres números como parámetros y devuelva el promedio de ellos.")
print("Solicitar los números al usuario y mostrar el resultado usando esta")
print("función.")

def calcular_promedio(num_a, num_b, num_c):
    sumatoria = num_a + num_b + num_c
    promedio = sumatoria / 3
    return promedio

num_a = float(input("Ingrese el 1° número para el calculo del promedio..."))
num_b = float(input("Ingrese el 2° número para el calculo del promedio..."))
num_c = float(input("Ingrese el 3° número para el calculo del promedio..."))

print(f"El promedio de los números ingresados {num_a}, {num_b}, {num_c} es {calcular_promedio(num_a, num_b, num_c):.2f} ")
