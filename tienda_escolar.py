# TIENDA ESCOLAR - SIMULADOR
# __________________________
 
# Lista de productos y sus precios (listas paralelas: misma posición = mismo producto)
productos = ["Cuaderno", "Lápiz", "Tijera", "Regla"]
precios = [300, 50, 150, 100]
 
# Muestra todos los productos disponibles con su precio
def mostrar_productos():
    print("\nProductos disponibles:")
    for i in range(len(productos)):
        print(f"{i + 1}. {productos[i]} - ${precios[i]}")
 
# Permite elegir un producto y agregarlo al carrito
# El carrito es un diccionario: clave = nombre del producto, valor = cantidad comprada
# Esto permite mostrar "Cuaderno x2" en vez de repetir el producto dos veces
def comprar_producto(carrito, total, presupuesto):
    mostrar_productos()
    try:
        opcion = int(input("\nSeleccione un producto: ")) - 1
        if 0 <= opcion < len(productos):
            nombre = productos[opcion]
            precio = precios[opcion]
            if total + precio <= presupuesto:
                # Si el producto ya está en el carrito, suma 1 a la cantidad
                # Si es nuevo, lo agrega con cantidad 1
                if nombre in carrito:
                    carrito[nombre] += 1
                else:
                    carrito[nombre] = 1
                total += precio
                print(f"Producto agregado: {nombre}")
                # Se guarda automáticamente despues de cada compra para no perder datos
                guardar_compra(carrito, total)
            else:
                print("No cuenta con presupuesto suficiente.")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")
    return carrito, total
 
# Muestra el estado actual: productos en el carrito, total gastado y saldo
def ver_estado(carrito, total, presupuesto):
    print("\nEstado de la compra:")
    if carrito:
        for nombre, cantidad in carrito.items():
            print(f"   - {nombre} x{cantidad}")
    else:
        print("  Sin productos")
    print("Total gastado $", total)
    print("Saldo restante $", presupuesto - total)
 
# Guarda el registro actualizado de la compra en un archivo de texto
# Usa modo "w" (sobreescritura) para que siempre refleje el estado actual de la sesión
# El historial de sesiones anteriores se mantiene con un separador
def guardar_compra(carrito, total):
    with open("compras.txt", "a") as archivo:
        archivo.write("Registro de compra.\n")
        if carrito:
            for nombre, cantidad in carrito.items():
                archivo.write(f"  - {nombre} x{cantidad}\n")
        else:
            archivo.write("  Ninguno\n")
        archivo.write(f"Total $ {total}\n")
        archivo.write("__________________\n")
 
# Muestra el ticket de la sesión actual en pantalla al finalizar la compra
# Se llama automáticamente al salir si el usuario lo solicita, no desde el menú
def ver_ticket(carrito, total):
    print("\n..............................")
    print("    🧾 TICKET DE COMPRA 🧾 ")
    print("..............................\n")
    for nombre, cantidad in carrito.items():
        # Busca el precio del producto en las listas paralelas por nombre
        indice = productos.index(nombre)
        subtotal = precios[indice] * cantidad
        # Formatea la línea alineando el precio a la derecha
        linea = f"  {nombre} x{cantidad}"
        print(f"{linea:<22} $ {subtotal}")
    print("------------------------------")
    print(f"  {'TOTAL':<20} $ {total}")
    print("\n..............................")
 
# Función principal del juego
# Está pensada para ser llamada desde el menú principal del grupo sin modificaciones
def juego_tienda():
    presupuesto = 1000
    carrito = {}   # Diccionario vacío: se irá llenando con {nombre: cantidad}
    total = 0
 
    print("\n ༘˚⋆ 🛒 TIENDA ESCOLAR 🛒  ༘˚⋆ ")
    print("Bienvenido/a al simulador de compras escolares.")
    print("Presupuesto inicial $", presupuesto)
 
    while True:
        print("\n─────────  MENÚ  ─────────")
        print("\n1. VER PRODUCTOS")
        print("2. COMPRAR PRODUCTO")
        print("3. VER ESTADO DEL CARRITO")
        print("0. VOLVER AL MENÚ PRINCIPAL") 
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                mostrar_productos()
            elif opcion == 2:
                carrito, total = comprar_producto(carrito, total, presupuesto)
            elif opcion == 3:
                ver_estado(carrito, total, presupuesto)
            elif opcion == 0:
                # Si compró algo, ofrece el ticket antes de salir
                if carrito:
                    ver = input("\n¿Desea ver su ticket de compra? (Si/No): ").strip().lower()
                    if ver == "si":
                        ver_ticket(carrito, total)
                print("\nCompra finalizada.")
                print("\n¡Gracias por jugar a la tienda escolar!")
                return
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada inválida.")
 
# Permite probar el juego de forma independiente antes de integrarlo al menú grupal
if __name__ == "__main__":
    juego_tienda()