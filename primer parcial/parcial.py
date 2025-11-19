
titulos = ["la odisea", "troya", "matar a un ruiseñor"]

ejemplares = [3, 4, 0]

opcion = 0

while opcion != 8: 
    print("MENU")
    print("1 Ingresar títulos")
    print("2 Ingresar ejemplares")
    print("3 Mostrar catálogo")
    print("4 Consultar disponibilidad")
    print("5 Listar agotados")
    print("6 Agregar título")
    print("7 Préstamo/Devolución actualizar ejemplares")
    print("8 Salir")
    
    entrada = (input("Ingrese una opcion  "))
    
    if entrada.isdigit():
        opcion = int(entrada)
        if opcion < 1 or opcion > 8:
            print("Ingresó una opción distinta de los números 1 a 8")
    else:
        print("Ingresó una opción no válida, use los números del 1 al 8")
    
    if opcion == 1:
        ingreso_titulo = str(input("Ingrese el nombre del título... ")).strip().lower()
        if not ingreso_titulo:
            print("Error: No se puede agregar un título vacio.")        
        elif ingreso_titulo in titulos: # Controla que el título no se cargue duplicado
            print(f"El título {ingreso_titulo} ya existe en el catálogo.")
        else:
            titulos.append(ingreso_titulo)
            print(f"Título {ingreso_titulo} agregado exitosamente.")
            ejemplares.append(0) #agrega 0 ejemplares para mantener el orden en la lista
               
    if opcion == 2:        
        ingreso_titulo = str(input("Ingrese el nombre del título del cual desea ingresar ejemplares... ")).strip().lower()
        if ingreso_titulo not in titulos: 
            print("ERROR, no existe ese titulo en el catálogo")
        elif ingreso_titulo in titulos:     
            ingreso_ejemplares = int(input("Ingrese la cantidad de ejemplares que desea agregar... "))
            indice = titulos.index(ingreso_titulo)
            ejemplares[indice] += ingreso_ejemplares
            print(f"Se han agregado {ingreso_ejemplares} Ejemplares de {ingreso_titulo} al Catálogo")           
                
    if opcion == 3:
        for i in range(len(titulos)):            
            print(f"Título: {titulos[i]} ejemplares disponibles: {ejemplares[i]}")
    
    if opcion == 4:
        ingreso_titulo = str(input("Ingrese el nombre del título, para ver su disponibilidad... ")).strip().lower()
        if ingreso_titulo not in titulos: 
            print("ERROR, no existe ese titulo en el catálogo")
        elif ejemplares[titulos.index(ingreso_titulo)] > 0:
            print(f"El título {ingreso_titulo} esta disponible, y hay {ejemplares[titulos.index(ingreso_titulo)]} copias")
        else:
            print("No hay disponibles copias del título ingresado")
            
    if opcion == 5:
        agotados = False
        for i in range(len(titulos)):
            if ejemplares[i] == 0:
                print(f"Títulos sin ejemplares disponibles {titulos[i]}")
                agotados = True
        if not agotados:
            print("Todos los títulos del Catálogo tienen al menos 1 ejemplar")
            
    if opcion == 6:
        ingreso_titulo = str(input("Ingrese el nombre del título... ")).strip().lower()
        if not ingreso_titulo:
            print("Error: No se puede agregar un título vacio.")        
        elif ingreso_titulo in titulos: # Controla que el título no se cargue duplicado
            print(f"El título {ingreso_titulo} ya existe en el catálogo.")
        else:     
            ingreso_ejemplares = int(input("Ingrese la cantidad de ejemplares que desea agregar... "))
            titulos.append(ingreso_titulo)
            ejemplares.append(ingreso_ejemplares)
            print(f"Se han agregado {ingreso_ejemplares} Ejemplares de {ingreso_titulo} al Catálogo")
            
    if opcion == 7:# PRESTAMO/DEVOLUCION
        prestamo_devolucion = str(input("Ingrese 'p' si es un PRESTAMO o 'd' si es una DEVOLUCION... ")).strip().lower()
        ingreso_titulo = str(input("Ingrese el nombre del título... ")).strip().lower()
        if ingreso_titulo not in titulos:
            print("El título ingresado no existe en el Catálogo")
        else:
            indice_prestamo = titulos.index(ingreso_titulo)
            if prestamo_devolucion == "p":
                if ejemplares[indice_prestamo] > 0:
                    ejemplares[indice_prestamo] -= 1    
                    print(f"Prestamo realizado. Quedan {ejemplares[indice_prestamo]} ejemplares de {ingreso_titulo}")
                else:
                    print("No hay ejemplares disponibles para prestar")
            elif prestamo_devolucion == "d":
                ejemplares[indice_prestamo] += 1
                print(f"Devolución realizada, Ahora hay {ejemplares[indice_prestamo]} ejemplares de {ingreso_titulo}")
            else:
                print("Opción invalida. Use 'p' para PRESTAMO o 'd' para DEVOLUCION")