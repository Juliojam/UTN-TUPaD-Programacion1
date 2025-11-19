# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. 
# Cada línea debe tener: nombre,precio,cantidad.

with open("productos.txt", "w") as archivo:
    archivo.write("cuaderno,7000,20\n")
    archivo.write("borrador,1500,30\n")
    
# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip()
# y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        partes = linea_limpia.split(",")        
        
        nombre = partes[0].capitalize() 
        precio = partes[1]
        cantidad = partes[2]
        
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        
# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, 
# le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.

nombre_nuevo = input("Ingrese el NOMBRE del nuevo producto: ").strip()
precio_nuevo = input("Ingrese el PRECIO del nuevo producto: ").strip()
cantidad_nuevo = input("Ingrese la CANTIDAD del nuevo producto: ").strip()

nueva_linea = f"{nombre_nuevo},{precio_nuevo},{cantidad_nuevo}\n"

with open("productos.txt", "a") as archivo:
    archivo.write(nueva_linea)
    
print(f"\n Producto agregado: {nombre_nuevo.capitalize()}, Precio: ${precio_nuevo}, Cantidad: {cantidad_nuevo}")
print("-" * 30)

print("Contenido FINAL del archivo después de la adición:")
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
        
# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos,
# donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

productos = []

print("Cargando productos del archivo 'productos.txt'...")

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        
        linea_limpia = linea.strip()
        partes = linea_limpia.split(",")
               
        nombre_str, precio_str, cantidad_str = partes
                
        producto_diccionario = {
            "nombre": nombre_str.capitalize(),
            "precio": float(precio_str),
            "cantidad": int(cantidad_str.strip()),
        }
                
        productos.append(producto_diccionario)

print("\n Lista de productos cargada:")

for item in productos:
    print(item)
    
    
# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

print("-" * 30)
print("BUSCADOR DE PRODUCTOS")
print("-" * 30)

nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip().capitalize()

producto_encontrado = None


for producto in productos:
    
    if producto["nombre"] == nombre_buscado:
        producto_encontrado = producto
        break 


print("-" * 30)
if producto_encontrado:
    print("¡Producto encontrado!")
    print(f"Nombre: {producto_encontrado['nombre']}")
    
    print(f"Precio: ${producto_encontrado['precio']:.2f}")
    print(f"Cantidad en stock: {producto_encontrado['cantidad']}")
else:
    print(f"Error: El producto '{nombre_buscado}' no existe en la lista.")

print("-" * 30)

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

print("GUARDANDO DATOS EN productos.txt")
print("-" * 30)

with open("productos.txt", "w") as archivo:
    for producto in productos:        
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)

print("¡Productos actualizados y guardados correctamente en 'productos.txt'!")
print("-" * 30)