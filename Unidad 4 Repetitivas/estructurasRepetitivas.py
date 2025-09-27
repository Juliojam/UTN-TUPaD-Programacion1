print("EJERCICIO ESTRUCTURAS REPETITIVAS")

print("1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100")
print("(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.")

contador = 0
#Bucle while, imprimirá el contador iniciando desde cero, 
#e ira incrementandose de uno en un hasta llegar a 100
while contador <= 100:
    print(contador)
    contador = contador + 1
    
    
print("2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de")
print("dígitos que contiene.")
#solicita al usuario ingresar un numero, inicializa por defecto un contador,
#y una variable inicializada como falsa, previendo usarla para el caso de que ingresen un negativo
numeroAIngresar = int(input("Ingrese un número"))
counter = 0
esNegativo = False
#evalua la condición del número, si el número menor a 0, es negativo lo convierte a positivo con un signo menos
if numeroAIngresar < 0:
    esNegativo = True
    numeroAIngresar = -numeroAIngresar
#en caso de que el número ingresado sea cero el contador quedara en 1    
if numeroAIngresar == 0:
    contador == 1   
#este bucle divide por diez (considerando enteros nada más) el número ingresado por teclado hasta que ya no pueda,
#asi mismo en cada vuelta del bucle el contador ira sumando 1 en cada vuelta. el número de vueltas del contador
#indicara la cantidad de digitos del número ingresado
while  numeroAIngresar > 0:
    numeroAIngresar = int(numeroAIngresar / 10)
    counter += 1
    
print("El número ingresado tiene", counter, " digitos")


print("3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores")
print("dados por el usuario, excluyendo esos dos valores.")
    
minimo = int(input("Ingrese el número inferior del rango de números a sumar"))
maximo = int(input("Ingrese el número superior del rango de números a sumar"))

acumulador = 0

for num in range(minimo + 1, maximo):
    acumulador = acumulador + num
    
    
print(acumulador)


print("4) Elabora un programa que permita al usuario ingresar números enteros y los sume en")
print("secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese")
print("un 0.")

number = int(input("Ingrese un número para agregar a la suma, y para concluir ingrese 0..."))
sumatoria = 0

while number != 0:
    sumatoria = sumatoria + number
    number = int(input("Ingrese un número para agregar a la suma , y para concluir ingrese 0..."))
    
print("Total Acumulado ", sumatoria)
    

print("5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el")
print("programa debe mostrar cuántos intentos fueron necesarios para acertar el número.")
import random
#se inicializa la variable num1 para que pueda iniciar el bucle
num1 = 0
#se inicializa el contador de intentos para adivinar el número
cuenta = 0
#bucle en el cual se genera un número aleatorio que luego se coteja con un número ingresado por el usuario
#si ambos coinciden se imprime la lineas de acierto, y con break sale del programa
#A su vez el contador va realizando la cuenta de intentos de 1 en 1 por cada vuelta
while num1 >= 0 and num1 <= 9:
    numAleatorio = int(random.randint(0, 9))
    num1 = int(input("Ingrese un número entre 0 y 9, si ingresa uno distinto sale del juego"))
    cuenta += 1
    if numAleatorio == num1:
        print("Ud. ha acertado, FELICIDADES!!!")
        break
    else:
        print("Lo sentimos, Ud. ha perdido")
#imprime la cantidad de intentos necesitadas para ganar    
print(f"Ud. ha realizado {cuenta} intetentos para poder ganar")


print("6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos")
print("entre 0 y 100, en orden decreciente.")
#incializa el número en 100
numeroInicial = 100

print(numeroInicial)
#bucle en el cual la suma inicial va decreciendo de 2 en 2, lo que permite imprimir todos
#los números pares como solicita la consigna
while numeroInicial <= 100 and numeroInicial >= 2:
    numeroInicial -= 2
    print(numeroInicial)
    

print("7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un")
print("número entero positivo indicado por el usuario.")

numerolimiteSuperior = int(input("Ingrese el número superior del rango de números a sumar"))

count = 0

for numx in range(0, numerolimiteSuperior + 1):
    count = count + numx
    
    
print(count)


print("8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el")
print("programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son")
print("negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad")
print("menor, pero debe estar preparado para procesar 100 números con un solo cambio.")
#se inicializa el contador de vueltas del bucle while
paraContar = 0
#se inicializa el contador de números pares
paresContador = 0
#Se inicializa el contador de números impares
imparesContador = 0
#Se inicializa el contador de números negativos
negativosContador = 0
#Se inicializa el contador de números positivos
positivosContador = 0


while paraContar < 100:
    numA = int(input("ingrese números para evaluar pares e impares"))
#if evalua si el número ingresado es mayor o igual a cero lo sumara como positivo, sino lo sumara como negativo
    if numA >= 0:
        positivosContador +=1
    else:
        negativosContador +=1
#if evalua mediante el modulo de 2, si es igual a cero es número par, sino es impar (else)   
    if numA % 2 == 0:
#Si la condición da que numA es PAR suma 1 punto el contador de pares
        paresContador +=1
#Si la condición da que numA es IMPAR suma 1 punto el contador de impares
    else:
        imparesContador +=1
#aumenta de 1 en 1 el contador para llegar a las vueltas deseadas en la condición o que no sea un bucle infinito        
    paraContar +=1
        
#se imprimen las cantidades de números pares, impares, negativos y positivos que se hallaron al finalizar el bucle        
print(f"Cantidad de números Pares {paresContador}")
print(f"Cantidad de números Impares {imparesContador}")
print(f"Cantidad de números positivos {positivosContador}")
print(f"Cantidad de números Negativos {negativosContador}")


print("9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la")
print("media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe")
print("poder procesar 100 números cambiando solo un valor.")
#se inicializa un acumulador para la sumatoria de números 
sumatoriaNumeros = 0
#esta variable define la cantidad de elementos que se ingresarán por teclado
ultimaVuelta = 6

for i in range(0, ultimaVuelta, 1):
    numTeclado = int(input("Ingrese un número entero"))
#esta variable es la que acumula la sumatoria de números que se van ingresando por teclado
    sumatoriaNumeros = sumatoriaNumeros + numTeclado
    
#esta variable toma la sumatoria total de números al finalizar el bucle y los divide por la cantidad
#de elementos tenidos en cuenta (vueltas del bucle), es decir la media
mediaCalculo = sumatoriaNumeros / ultimaVuelta

#Imprime el calculo de la media
print(f"La media de los números ingresados es {mediaCalculo}")


print("10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el")
print("usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.")

#Solicita al usuario que ingrese el número a invertir
numeroAInvertir = input("Ingresa un número: ")

#Se inicializa la variable del número invertido como un string vacio
numeroInvertido = ""

#Recorre los dígitos del número ingresado, iniciando desde la posición [0] usando un bucle
#lo orderana en la primera posición que luego se correra al ingresar el siguiente elemento
#del array de ("strings") concatenandolos
for digito in numeroAInvertir:
#Aqui se concatena el digito que se va recorriendo y lo suma (string)
    numeroInvertido = digito + numeroInvertido

#Se imprime la leyenda y el número ingresado invertido
print("El número invertido es:", numeroInvertido)
