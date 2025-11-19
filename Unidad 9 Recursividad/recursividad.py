# 1) Crea una función recursiva que calcule el factorial de un número.
# Luego, utiliza esa función para calcular y mostrar en pantalla el 
# factorial de todos los números enteros entre 1 y el número que indique el usuario.

def factorial_recursivo(n):
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursivo(n - 1)

num_usuario = int(input("Ingrese un número entero positivo para calcular factoriales hasta él: "))

print(f"\nFactoriales desde 1 hasta {num_usuario}:")

for i in range(1, num_usuario + 1):
    resultado = factorial_recursivo(i)
    print(f"El factorial de {i} ({i}!) es: {resultado}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la
# posición indicada. Posteriormente, muestra la serie completa hasta la posición 
# que el usuario especifique.

def fibonacci_recursivo(n):
        
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

posicion_usuario = int(input("Ingrese la posición máxima (N) para la serie de Fibonacci (N >= 0): "))

print(f"\nSerie de Fibonacci hasta la posición {posicion_usuario}:")

serie_completa = []

for i in range(posicion_usuario + 1):
    valor_fib = fibonacci_recursivo(i)
    serie_completa.append(str(valor_fib))

print("Serie:", ", ".join(serie_completa))
print(f"El valor de Fibonacci en la posición {posicion_usuario} es: {valor_fib}")

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia_recursiva(base, exponente):
    
    if exponente == 0:
        return 1
        
    elif exponente == 1:
        return base
        
    elif exponente > 1:
        
        return base * potencia_recursiva(base, exponente - 1)
        
    elif exponente < 0:
        
        return 1 / potencia_recursiva(base, abs(exponente))
    
print("--- Prueba de Potencia Recursiva ---")

base = float(input("Ingrese la base (n): "))
exponente = int(input("Ingrese el exponente (m): "))


resultado = potencia_recursiva(base, exponente)

print(f"\nCálculo: {base} elevado a la {exponente} ({base}^{exponente})")
print(f"El resultado recursivo es: {resultado}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal
# y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario_recursivo(n):
    if n == 0:
        return "0"
        
    if n == 1:
        return "1"
        
    return decimal_a_binario_recursivo(n // 2) + str(n % 2)

numero_decimal = int(input("Ingrese un numero entero en base 10   "))
binario_resultante = decimal_a_binario_recursivo(numero_decimal)

print(f"El número decimal {numero_decimal} en binario es: {binario_resultante}")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena
# de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
        
    return es_palindromo(palabra[1:-1])

# --- Ejemplos --- #
print(f"¿'radar' es palíndromo? {es_palindromo('radar')}")          # True
print(f"¿'oso' es palíndromo? {es_palindromo('oso')}")              # True
print(f"¿'anilina' es palíndromo? {es_palindromo('anilina')}")      # True
print(f"¿'reconocer' es palíndromo? {es_palindromo('reconocer')}")  # True
print(f"¿'python' es palíndromo? {es_palindromo('python')}")        # False
print(f"¿'ala' es palíndromo? {es_palindromo('ala')}")              # True
print(f"¿'' es palíndromo? {es_palindromo('')}")                    # True
print(f"¿'a' es palíndromo? {es_palindromo('a')}")                  # True

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):    
    if n < 10:
        return n        
    ultimo_digito = n % 10        
    resto_numero = n // 10        
    return ultimo_digito + suma_digitos(resto_numero)

print("--- Prueba de la función suma_digitos ---")

print(f"Suma de dígitos de 1234: {suma_digitos(1234)} (Esperado: 10)")

print(f"Suma de dígitos de 9: {suma_digitos(9)} (Esperado: 9)")

print(f"Suma de dígitos de 305: {suma_digitos(305)} (Esperado: 8)")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    
    if n == 1:
        return 1
        
    return n + contar_bloques(n - 1)

print("--- Prueba de la función contar_bloques ---")

# Ejemplo 1: contar_bloques(1) -> 1
print(f"Bloques para base 1: {contar_bloques(1)} (Esperado: 1)")

# Ejemplo 2: contar_bloques(2) -> 2 + 1 = 3
print(f"Bloques para base 2: {contar_bloques(2)} (Esperado: 3)")

# Ejemplo 3: contar_bloques(4) -> 4 + 3 + 2 + 1 = 10
print(f"Bloques para base 4: {contar_bloques(4)} (Esperado: 10)")

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número
# entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    
    if numero == 0:
        return 0
        
    ultimo_digito = numero % 10
        
    conteo_actual = 1 if ultimo_digito == digito else 0
        
    resto_numero = numero // 10
        
    return conteo_actual + contar_digito(resto_numero, digito)

print("--- Prueba de la función contar_digito ---")

# Ejemplo 1: contar_digito(12233421, 2) → 3
print(f"Veces que aparece 2 en 12233421: {contar_digito(12233421, 2)} (Esperado: 3)")

# Ejemplo 2: contar_digito(5555, 5) → 4
print(f"Veces que aparece 5 en 5555: {contar_digito(5555, 5)} (Esperado: 4)")

# Ejemplo 3: contar_digito(123456, 7) → 0
print(f"Veces que aparece 7 en 123456: {contar_digito(123456, 7)} (Esperado: 0)")