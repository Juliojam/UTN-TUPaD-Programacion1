import csv
import os

# Lista principal que almacena los países (lista de diccionarios)
PAISES = [] 
NOMBRE_ARCHIVO = 'paises.csv'

# --- 1. Carga y Guardado Base de Datos ---

def cargar_datos_desde_csv(nombre_archivo):
    """
    Lee los datos desde un archivo CSV. Si no existe, inicializa la lista vacía.
    """
    paises_cargados = []
    global PAISES
    
    print(f"⌛ Intentando cargar datos desde {nombre_archivo}...")
    
    # Comprobación de existencia del archivo
    if not os.path.exists(nombre_archivo):
        print(f"⚠️ Advertencia: El archivo '{nombre_archivo}' no fue encontrado.")
        print("ℹ️ Iniciando con lista vacía. El archivo será creado al guardar.")
        PAISES = []
        return True
        
    # Si el archivo existe, procedemos a leer
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        lector_simple = csv.reader(archivo)
        filas = list(lector_simple)
        
        if not filas:
            print("Advertencia: El archivo CSV está vacío (sin datos).")
            PAISES = []
            return True
            
        cabecera = [h.strip().lower() for h in filas[0]]
        columnas_esperadas = ['nombre', 'poblacion', 'superficie', 'continente']
        
        if not all(col in cabecera for col in columnas_esperadas):
            print("❌ Error de formato en CSV: Faltan encabezados esperados.")
            return False
        
        # Volvemos al inicio para usar DictReader
        archivo.seek(0)
        lector_csv = csv.DictReader(archivo)
        
        for fila in lector_csv:
            fila_normalizada = {k.strip().lower(): v.strip() for k, v in fila.items() if k}
            
            # Validar campos vacíos y formatos numéricos
            if not all(fila_normalizada.get(col) for col in columnas_esperadas):
                continue

            poblacion_str = fila_normalizada.get('poblacion', '')
            superficie_str = fila_normalizada.get('superficie', '')
            
            if poblacion_str.isdigit() and superficie_str.isdigit():
                pais = {
                    'Nombre': fila_normalizada.get('nombre', 'N/A'),
                    'Población': int(poblacion_str),
                    'Superficie': int(superficie_str),
                    'Continente': fila_normalizada.get('continente', 'N/A')
                }
                paises_cargados.append(pais)
            
    PAISES = paises_cargados
    print(f"✅ Carga exitosa. {len(PAISES)} países cargados.")
    return True

def guardar_datos_a_csv(nombre_archivo):
    """
    Guarda los datos de la lista PAISES en el archivo CSV.
    Crea el archivo si no existe o lo sobrescribe si existe.
    """
    if not PAISES:
        print("ℹ️ Lista de países vacía. No hay nada que guardar.")
        return
        
    # Nombres de encabezados para el archivo CSV (en minúsculas)
    encabezados_csv = ['nombre', 'poblacion', 'superficie', 'continente']
    
    # Abrimos el archivo en modo 'w'. ESTA LÍNEA CREA EL ARCHIVO SI NO EXISTE.
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        
        # 1. Escribir la cabecera
        escritor.writerow(encabezados_csv)
        
        # 2. Escribir los datos, mapeando los diccionarios a listas de valores
        for pais in PAISES:
            fila_valores = [
                pais['Nombre'], 
                pais['Población'], 
                pais['Superficie'], 
                pais['Continente']
            ]
            escritor.writerow(fila_valores)
            
    print(f"✅ Los cambios se han guardado exitosamente en '{nombre_archivo}'.")


# --- 2. Funciones Auxiliares para Validación de Entrada ---

def _validar_entero_positivo(prompt):
    """Auxiliar para pedir y validar un entero positivo sin try-except."""
    while True:
        valor_str = input(prompt).strip()
        if valor_str.isdigit():
            return int(valor_str)
        else:
            print("❌ Entrada inválida. Debe ser un número entero positivo.")

def _validar_cadena_no_vacia(prompt):
    """Auxiliar para pedir y validar una cadena no vacía."""
    while True:
        cadena = input(prompt).strip()
        if cadena:
            return cadena
        else:
            print("❌ El campo no puede estar vacío.")

# --- 3. Gestión de Países (CRUD Básico) ---

def agregar_pais():
    """Permite añadir un nuevo país a la lista global PAISES."""
    print("\n--- ➕ Agregar Nuevo País ---")
    
    nombre = _validar_cadena_no_vacia("Ingrese Nombre del País: ")
    if buscar_pais_por_nombre(nombre, coincidencia_exacta=True):
        print(f"❌ Error: El país '{nombre}' ya existe en la lista.")
        return

    poblacion = _validar_entero_positivo("Ingrese Población (entero): ")
    superficie = _validar_entero_positivo("Ingrese Superficie en km² (entero): ")
    continente = _validar_cadena_no_vacia("Ingrese Continente: ")
    
    nuevo_pais = {
        'Nombre': nombre,
        'Población': poblacion,
        'Superficie': superficie,
        'Continente': continente
    }
    PAISES.append(nuevo_pais)
    print(f"✅ País '{nombre}' agregado exitosamente.")

def buscar_pais_por_nombre(nombre_buscado, coincidencia_exacta=False):
    """Busca países por nombre."""
    nombre_buscado = nombre_buscado.strip().lower()
    resultados = []

    for pais in PAISES:
        nombre_pais = pais['Nombre'].lower()
        if coincidencia_exacta:
            if nombre_pais == nombre_buscado:
                return pais 
        else:
            if nombre_buscado in nombre_pais:
                resultados.append(pais)

    return None if coincidencia_exacta else resultados

def mostrar_resultados_busqueda(resultados):
    """Formatea y muestra una lista de países."""
    if not resultados:
        print("ℹ️ No se encontraron países con ese criterio de búsqueda/filtro.")
        return
    
    print("\n--- 🔎 Resultados de la Búsqueda/Filtro ---")
    print(f"| {'Nombre':<20} | {'Población':>15} | {'Superficie (km²)*':>18} | {'Continente':<15} |")
    print("-" * 75)
    for pais in resultados:
        print(f"| {pais['Nombre']:<20} | {pais['Población']:>15,} | {pais['Superficie']:>18,} | {pais['Continente']:<15} |")
    print("-" * 75)


def buscar_pais_menu():
    """Función para la opción de menú de búsqueda."""
    if not PAISES:
        print("⚠️ La lista de países está vacía. Cargue datos primero.")
        return
        
    nombre = _validar_cadena_no_vacia("Ingrese el nombre (o parte del nombre) del país a buscar: ")
    resultados = buscar_pais_por_nombre(nombre, coincidencia_exacta=False)
    mostrar_resultados_busqueda(resultados)


def actualizar_pais():
    """Actualiza Población y Superficie de un país existente."""
    if not PAISES:
        print("⚠️ La lista de países está vacía.")
        return

    nombre_b = _validar_cadena_no_vacia("Ingrese el nombre del país a actualizar: ")
    pais_a_actualizar = buscar_pais_por_nombre(nombre_b, coincidencia_exacta=True)
    
    if pais_a_actualizar is None:
        print(f"❌ Error: El país '{nombre_b}' no fue encontrado para actualizar.")
        return
    
    print(f"\nDatos actuales de {pais_a_actualizar['Nombre']}:")
    print(f"  Población: {pais_a_actualizar['Población']:,}")
    print(f"  Superficie: {pais_a_actualizar['Superficie']:,} km²")
    
    nueva_poblacion = _validar_entero_positivo("Ingrese la NUEVA Población (entero): ")
    nueva_superficie = _validar_entero_positivo("Ingrese la NUEVA Superficie en km² (entero): ")
    
    pais_a_actualizar['Población'] = nueva_poblacion
    pais_a_actualizar['Superficie'] = nueva_superficie
    
    print(f"✅ País '{pais_a_actualizar['Nombre']}' actualizado exitosamente.")


# --- 4. Filtros ---

def filtrar_por_continente():
    """Filtra países por continente."""
    if not PAISES:
        print("⚠️ La lista de países está vacía.")
        return

    continente_f = _validar_cadena_no_vacia("Ingrese el Continente a filtrar: ")
    continente_f = continente_f.strip().lower()
    
    resultados = [pais for pais in PAISES if pais['Continente'].lower() == continente_f]
    mostrar_resultados_busqueda(resultados)

def filtrar_por_rango(campo):
    """Filtra países por rango de población o superficie."""
    if not PAISES:
        print("⚠️ La lista de países está vacía.")
        return

    print(f"\n--- Filtrar por Rango de {campo} ---")
    
    min_valor = _validar_entero_positivo(f"Ingrese el valor MÍNIMO de {campo}: ")
    max_valor = _validar_entero_positivo(f"Ingrese el valor MÁXIMO de {campo}: ")

    if min_valor > max_valor:
        print("❌ Error: El valor mínimo no puede ser mayor que el valor máximo.")
        return

    resultados = [pais for pais in PAISES if min_valor <= pais[campo] <= max_valor]
    mostrar_resultados_busqueda(resultados)

# --- 5. Ordenamiento ---

def ordenar_paises():
    """Permite ordenar la lista de países por Nombre, Población o Superficie."""
    if not PAISES:
        print("⚠️ La lista de países está vacía.")
        return

    print("\n--- ⇅ Opciones de Ordenamiento ---")
    print("1. Por Nombre")
    print("2. Por Población")
    print("3. Por Superficie")
    
    opcion = input("Ingrese la opción de ordenamiento (1-3): ").strip()
    
    criterio_map = {'1': 'Nombre', '2': 'Población', '3': 'Superficie'}
    
    if opcion not in criterio_map:
        print("❌ Opción de ordenamiento inválida.")
        return

    criterio = criterio_map[opcion]
    
    reversa = False
    if criterio != 'Nombre':
        orden = input("¿Desea ordenar de forma (A)scendente o (D)escendente? (A/D): ").strip().lower()
        if orden == 'd':
            reversa = True
        elif orden != 'a':
             print("⚠️ Opción de orden inválida. Usando Ascendente por defecto.")

    PAISES.sort(key=lambda pais: pais[criterio], reverse=reversa)
    
    print(f"✅ Lista ordenada por {criterio} ({'Descendente' if reversa else 'Ascendente'}).")
    mostrar_resultados_busqueda(PAISES)


# --- 6. Estadísticas ---

def mostrar_estadisticas():
    """Calcula y muestra estadísticas básicas."""
    if not PAISES:
        print("⚠️ La lista de países está vacía.")
        return
        
    print("\n--- 📊 Estadísticas de Países ---")
    
    # País con mayor y menor población
    pais_mayor_poblacion = max(PAISES, key=lambda pais: pais['Población'])
    pais_menor_poblacion = min(PAISES, key=lambda pais: pais['Población'])
    
    print(f"🥇 País con Mayor Población: {pais_mayor_poblacion['Nombre']} ({pais_mayor_poblacion['Población']:,})")
    print(f"🥉 País con Menor Población: {pais_menor_poblacion['Nombre']} ({pais_menor_poblacion['Población']:,})")
    
    # Promedio de población y superficie
    total_poblacion = sum(pais['Población'] for pais in PAISES)
    total_superficie = sum(pais['Superficie'] for pais in PAISES)
    num_paises = len(PAISES)

    promedio_poblacion = total_poblacion / num_paises
    promedio_superficie = total_superficie / num_paises
    
    print(f"👤 Promedio de Población: {promedio_poblacion:,.2f}")
    print(f"🗺️ Promedio de Superficie: {promedio_superficie:,.2f} km²")
    
    # Cantidad de países por continente
    conteo_continentes = {}
    for pais in PAISES:
        continente = pais['Continente']
        if continente in conteo_continentes:
            conteo_continentes[continente] += 1
        else:
            conteo_continentes[continente] = 1
            
    print("\n🌍 Cantidad de Países por Continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"  - {continente}: {cantidad}")

# --- 7. Menú Principal ---

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n===========================================")
    print("      🌎 GESTIÓN DE DATOS DE PAÍSES 🌎")
    print("===========================================")
    print("1. Agregar un país")
    print("2. Actualizar Población y Superficie de un País")
    print("3. Buscar un país por nombre (parcial/exacto)")
    print("4. Filtrar países por Continente")
    print("5. Filtrar países por Rango de Población")
    print("6. Filtrar países por Rango de Superficie")
    print("7. Ordenar países")
    print("8. Mostrar Estadísticas")
    print("0. Salir (Guardar y cerrar)")
    print("-------------------------------------------")

def main():
    """Función principal del programa."""
    
    # 1. Carga inicial de datos
    cargar_datos_desde_csv(NOMBRE_ARCHIVO)
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ").strip()
        
        # Validación de entrada del menú
        if opcion.isdigit():
            opcion_int = int(opcion)
            if 0 <= opcion_int <= 8:
                if opcion_int == 1:
                    agregar_pais()
                elif opcion_int == 2:
                    actualizar_pais()
                elif opcion_int == 3:
                    buscar_pais_menu()
                elif opcion_int == 4:
                    filtrar_por_continente()
                elif opcion_int == 5:
                    filtrar_por_rango('Población')
                elif opcion_int == 6:
                    filtrar_por_rango('Superficie')
                elif opcion_int == 7:
                    ordenar_paises()
                elif opcion_int == 8:
                    mostrar_estadisticas()
                elif opcion_int == 0:
                    # Persistencia al salir
                    guardar_datos_a_csv(NOMBRE_ARCHIVO)
                    print("\n👋 ¡Gracias por usar el sistema! Saliendo del programa.")
                    break
            else:
                print("❌ Opción inválida. Ingrese un número del 0 al 8.")
        else:
            print("❌ Opción inválida. Ingrese un número.")
        
# --- Ejecución ---

if __name__ == "__main__":
    main()