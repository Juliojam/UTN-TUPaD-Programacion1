import csv
import os

PAISES = []
NOMBRE_ARCHIVO_CSV = 'paises.csv'

def cargar_datos_desde_csv(nombre_archivo):
    global PAISES
    paises_cargados = []
    
    if not os.path.exists(nombre_archivo):
        print(f" El archivo '{nombre_archivo}' no fue encontrado, Iniciando con lista vacia.")
        PAISES = []
        return
    
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        
        nombres_columnas = lector_csv.fieldnames or []
        
        if not nombres_columnas:
            print("El archivo CSV esta vacio.")
            PAISES = []
            return
        
        encabezado = []
        
        for nombre_campo in nombres_columnas:
            encabezado.append(nombre_campo.strip().lower())
        
        columnas_esperadas = ['nombre', 'poblacion', 'superficie', 'continente']
        
        if not all(columna in encabezado for columna in columnas_esperadas):
            print("Error de formato en CSV.")
            return
        
        archivo.seek(0)
        lector_csv = csv.DictReader(archivo)
                
        for fila in lector_csv:
            fila_normalizada = obtener_fila_normalizada(fila)
            if not all(fila_normalizada.get(columna) for columna in columnas_esperadas):
                continue
            poblacion = parsear_campo_entero(fila_normalizada.get('poblacion'))
            superficie = parsear_campo_entero(fila_normalizada.get('superficie'))
            
            if poblacion is None or superficie is None:
                continue
            
            paises_cargados.append({
                'Nombre': fila_normalizada.get('nombre', 'N/A'),
                'Población': poblacion,
                'Superficie': superficie,
                'Continente': fila_normalizada.get('continente', 'N/A')
            })
                
    PAISES = paises_cargados
    
    print(f"Carga exitosa. {len(PAISES)} paises cargados.")
    return

def obtener_fila_normalizada(fila):
    return { (clave or '').strip().lower(): (valor or '').strip() for clave, valor in fila.items() if clave }

def parsear_campo_entero(valor):
    valor_cadena = (valor or '').replace(',', '').replace('.', '').strip()
    if valor_cadena == '':
        return None
    if valor_cadena.isdigit():
        return int(valor_cadena)
    else:
        return None

def guardar_datos_a_csv(nombre_archivo):
    encabezados = ['nombre', 'poblacion', 'superficie', 'continente']
    
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezados)
        
        for pais in PAISES:
            fila = [
                pais.get('Nombre', ''),
                pais.get('Población', ''),
                pais.get('Superficie', ''),
                pais.get('Continente', '')
            ]
            
            escritor.writerow(fila)
    print(f"cambios guardados en '{nombre_archivo}'.")
    return

def validar_entero_positivo(prompt):
    while True:
        valor = input(prompt).strip()
        valor_normalizado = valor.replace(',', '').replace('.', '').strip()

        if valor_normalizado and valor_normalizado.isdigit():
            numero = int(valor_normalizado)
            if numero >= 0:
                return numero

        print("Entrada invalida. Debe ser un numero entero positivo.")

def validar_cadena_no_vacia(prompt):
    while True:
        valor_cadena = input(prompt).strip()
        if valor_cadena:
            return valor_cadena
        print("El campo no puede estar vacio.")

def agregar_pais():
    nombre = validar_cadena_no_vacia("Ingrese Nombre del Pais: ")
    
    if buscar_pais_por_nombre(nombre):
        print(f"El pais '{nombre}' ya existe en la lista.")
        return
    poblacion = validar_entero_positivo("Ingrese Población (entero): ")
    superficie = validar_entero_positivo("Ingrese Superficie en km2 (entero): ")
    continente = validar_cadena_no_vacia("Ingrese Continente: ")
    
    nuevo_pais = {
        'Nombre': nombre,
        'Población': poblacion,
        'Superficie': superficie,
        'Continente': continente
    }
    
    PAISES.append(nuevo_pais)
    
    print(f"Pais '{nombre}' agregado exitosamente.")

def buscar_pais_por_nombre(nombre):
    if not isinstance(nombre, str):
        return []
    
    nombre_a_buscar = nombre.strip().casefold()
    
    if not nombre_a_buscar:
        return []
    
    coincidencias_exactas = []
    
    for pais in PAISES:
        nombre = pais.get('Nombre', '')
        if nombre and nombre.strip().casefold() == nombre_a_buscar:
            coincidencias_exactas.append(pais)
            
    if coincidencias_exactas:
        return coincidencias_exactas
    
    coincidencias_parciales = []
    
    for pais in PAISES:
        nombre = pais.get('Nombre', '')
        if nombre and nombre_a_buscar in nombre.strip().casefold():
            coincidencias_parciales.append(pais)
            
    return coincidencias_parciales

def mostrar_resultados_busqueda(resultados):
    if not resultados:
        print("No se encontraron paises con ese criterio de busqueda/filtro.")
        return
    
    if isinstance(resultados, dict):
        resultados = [resultados]
    print("\n--- Resultados de la Busqueda/Filtro ---")
    print(f"| {'Nombre':<20} | {'Población':>15} | {'Superficie (km2)*':>18} | {'Continente':<15} |")
    print("-" * 75)
    
    for pais in resultados:
        nombre = pais.get('Nombre', '')
        poblacion = pais.get('Población', 0)
        superficie = pais.get('Superficie', 0)
        continente = pais.get('Continente', '')
        print(f"| {nombre:<20} | {poblacion:>15,} | {superficie:>18,} | {continente:<15} |")
    print("-" * 75)

def buscar_pais_menu():
    if not PAISES:
        print("La lista de paises esta vacia. Cargue datos primero.")
        return

    nombre = validar_cadena_no_vacia("Ingrese el Nombre (o parte del Nombre) del pais a buscar: ")
    resultados = buscar_pais_por_nombre(nombre)

    mostrar_resultados_busqueda(resultados)

def actualizar_pais():
    if not PAISES:
        print("La lista de paises esta vacia.")
        return
    
    nombre = validar_cadena_no_vacia("Ingrese el Nombre del pais a actualizar: ")
    pais_encontrado = buscar_pais_por_nombre(nombre)
    
    if not pais_encontrado:
        print(f"El pais '{nombre}' no fue encontrado para actualizar.")
        return
    
    pais = pais_encontrado[0]
    
    print(f"\nDatos actuales de {pais['Nombre']}:")
    print(f"  Población: {pais['Población']:,}")
    print(f"  Superficie: {pais['Superficie']:,} km2")
    
    nueva_poblacion = validar_entero_positivo("Ingrese la NUEVA Población (entero): ")
    nueva_superficie = validar_entero_positivo("Ingrese la NUEVA Superficie en km2 (entero): ")
    
    pais['Población'] = nueva_poblacion
    pais['Superficie'] = nueva_superficie
    
    print(f"Pais '{pais['Nombre']}' actualizado exitosamente.")

def filtrar_por_continente():
    if not PAISES:
        print("La lista de paises esta vacia.")
        return
    
    continente = validar_cadena_no_vacia("Ingrese el Continente a filtrar: ").strip().lower()
    
    resultados = []
    
    for pais in PAISES:
        continente_pais = pais.get('Continente', '').strip().lower()
        if continente_pais == continente:
            resultados.append(pais)
    
    mostrar_resultados_busqueda(resultados)

def filtrar_por_rango(campo):
    if not PAISES:
        print("La lista de paises esta vacia.")
        return
    
    valor_minimo = validar_entero_positivo(f"Ingrese el valor MINIMO de {campo}: ")
    valor_maximo = validar_entero_positivo(f"Ingrese el valor MAXIMO de {campo}: ")
    
    if valor_minimo > valor_maximo:
        print("El valor minimo no puede ser mayor que el valor maximo.")
        return
    
    resultados = []
    
    for pais in PAISES:
        valor = pais.get(campo, 0)
        if valor_minimo <= valor <= valor_maximo:
            resultados.append(pais)
            
    mostrar_resultados_busqueda(resultados)

def ordenamiento_paises(clave_ordenamiento, descendente):
    total_paises = len(PAISES)
    
    if total_paises < 2:
        return
    
    for i in range(total_paises - 1):
        for j in range(total_paises - 1 - i):
            
            pais_izquierda = PAISES[j]
            pais_derecha = PAISES[j + 1]
            
            valor_izquierda = pais_izquierda.get(clave_ordenamiento, '')
            valor_derecha = pais_derecha.get(clave_ordenamiento, '')
            
            if isinstance(valor_izquierda, str):
                valor_izquierda = valor_izquierda.lower()
                
            if isinstance(valor_derecha, str):
                valor_derecha = valor_derecha.lower()
                
            if descendente:
                requiere_intercambio = valor_izquierda < valor_derecha
            else:
                requiere_intercambio = valor_izquierda > valor_derecha
            
            if requiere_intercambio:
                PAISES[j], PAISES[j + 1] = pais_derecha, pais_izquierda
                
def ordenar_paises():
    if not PAISES:
        print("La lista de paises esta vacia.")
        return
    
    print("\n--- Opciones de Ordenamiento ---")
    print("1. Por Nombre")
    print("2. Por Población")
    print("3. Por Superficie")
    
    opcion = input("Ingrese la opcion de ordenamiento (1-3): ").strip()
    
    mapeo = {'1': 'Nombre', '2': 'Población', '3': 'Superficie'}
    
    if opcion not in mapeo:
        print("Opcion de ordenamiento invalida.")
        return
    
    clave = mapeo[opcion]
    reversa = False
    
    if clave == 'Superficie':
        orden = input("¿Desea ordenar de forma (A)scendente o (D)escendente? (A/D): ").strip().lower()
        if orden == 'd':
            reversa = True
        elif orden != 'a':
            print("⚠️ Opción de orden inválida. Usando Ascendente por defecto.")
    
    ordenamiento_paises(clave, reversa)
    
    print(f"Lista ordenada por {clave} ({'Descendente' if reversa else 'Ascendente'}).")
    
    mostrar_resultados_busqueda(PAISES)

def mostrar_estadisticas():
    if not PAISES:
        print("La lista de paises esta vacia.")
        return

    print("\n--- Estadisticas de Paises ---")

    pais_mayor = PAISES[0]
    pais_menor = PAISES[0]
    
    for pais in PAISES[1:]:
        poblacion = pais.get('Población', 0)
        if poblacion > pais_mayor.get('Población', 0):
            pais_mayor = pais
        if poblacion < pais_menor.get('Población', 0):
            pais_menor = pais

    print(f"Pais con Mayor Población: {pais_mayor['Nombre']} ({pais_mayor['Población']:,})")
    print(f"Pais con Menor Población: {pais_menor['Nombre']} ({pais_menor['Población']:,})")

    total_poblacion = 0
    total_superficie = 0
    
    for pais in PAISES:
        total_poblacion += pais.get('Población', 0)
        total_superficie += pais.get('Superficie', 0)

    cantidad = len(PAISES)
    
    promedio_poblacion = total_poblacion / cantidad if cantidad else 0
    promedio_superficie = total_superficie / cantidad if cantidad else 0

    print(f"Promedio de Población: {promedio_poblacion:,.2f}")
    print(f"Promedio de Superficie: {promedio_superficie:,.2f} km2")

    conteo_continentes = {}
    
    for pais in PAISES:
        continente = pais.get('Continente', '')
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1

    print("\nCantidad de Paises por Continente:")
    
    for continente, cantidad in conteo_continentes.items():
        print(f"  - {continente}: {cantidad}")

def mostrar_menu():
    print("\n===========================================")
    print("      GESTION DE DATOS DE PAISES")
    print("===========================================")
    print("1. Agregar un pais")
    print("2. Actualizar Población y Superficie de un Pais")
    print("3. Buscar un pais por Nombre (parcial/exacto)")
    print("4. Filtrar paises por Continente")
    print("5. Filtrar paises por Rango de Población")
    print("6. Filtrar paises por Rango de Superficie")
    print("7. Ordenar paises")
    print("8. Mostrar Estadisticas")
    print("0. Salir (Guardar y cerrar)")
    print("-------------------------------------------")

def main():
    cargar_datos_desde_csv(NOMBRE_ARCHIVO_CSV)
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opcion: ").strip()
        if opcion.isdigit():
            i = int(opcion)
            if 0 <= i <= 8:
                if i == 1:
                    agregar_pais()
                elif i == 2:
                    actualizar_pais()
                elif i == 3:
                    buscar_pais_menu()
                elif i == 4:
                    filtrar_por_continente()
                elif i == 5:
                    filtrar_por_rango('Población')
                elif i == 6:
                    filtrar_por_rango('Superficie')
                elif i == 7:
                    ordenar_paises()
                elif i == 8:
                    mostrar_estadisticas()
                elif i == 0:
                    guardar_datos_a_csv(NOMBRE_ARCHIVO_CSV)
                    print("Saliendo del programa.")
                    break
            else:
                print("Opcion invalida. Ingrese un numero del 0 al 8.")
        else:
            print("Opcion invalida. Ingrese un numero.")

if __name__ == "__main__":
    main()
