# TIENDA ESCOLAR - SIMULADOR
# __________________________
 
# Lista de productos y sus precios (listas paralelas: misma posición = mismo producto)
productos = ["Cuaderno", "Lápiz", "Goma", "Regla"]
precios = [300, 100, 50, 150]
 
# Muestra todos los productos disponibles con su precio
def mostrar_productos():
    print("\nProductos disponibles:")
    for i in range(len(productos)):
        print(f"{i + 1}. {productos[i]} - ${precios[i]}")
 
# Permite elegir un producto y agregarlo al carrito
# Se fija que la opción sea válida y que haya presupuesto suficiente
def comprar_producto(carrito, total, presupuesto):
    mostrar_productos()
    try:
        opcion = int(input("\nSeleccione un producto: ")) - 1
        if 0 <= opcion < len(productos):
            precio = precios[opcion]
            if total + precio <= presupuesto:
                carrito.append(productos[opcion])
                total += precio
                print(f"Producto agregado: {productos[opcion]}")
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
    print("Productos:", carrito if carrito else "Sin productos")
    print("Total gastado $", total)
    print("Saldo restante $", presupuesto - total)
 
# Guarda el registro de la compra en un archivo de texto (modo append para no borrar compras anteriores)
# Se llama tanto al salir con 0 como al volver al menú principal, para no perder datos
def guardar_compra(carrito, total):
    with open("compras.txt", "a") as archivo:
        archivo.write("Registro de compra.\n")
        archivo.write(f"Productos: {', '.join(carrito) if carrito else 'Ninguno'}\n")
        archivo.write(f"Total $ {total}\n")
        archivo.write("__________________\n")
 
# Muestra el ticket de la sesión actual en pantalla (no se guarda en archivo)
def ver_ticket(carrito, total):
    print("\n..............................")
    print("    🧾 TICKET DE COMPRA 🧾 ")
    print("..............................\n")
    print("Productos:", carrito if carrito else "Ninguno")
    print("Total gastado $", total)
    print("\n..............................")
 
# Función principal del juego
# Está pensada para ser llamada desde el menú principal del grupo sin modificaciones
def juego_tienda():
    presupuesto = 1000
    carrito = []
    total = 0
 
    print("\n ༘˚⋆ 🛒 TIENDA ESCOLAR 🛒  ༘˚⋆ " )
    print("Bienvenido/a al simulador de compras escolares.")
    print("Presupuesto inicial $", presupuesto)
 
    while True:
        print("\nMENÚ")
        print("1. VER PRODUCTOS")
        print("2. COMPRAR PRODUCTO")
        print("3. VER ESTADO DEL CARRITO")
        print("4. VER TICKET DE COMPRA")
        print("0. SALIR")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                mostrar_productos()
            elif opcion == 2:
                carrito, total = comprar_producto(carrito, total, presupuesto)
            elif opcion == 3:
                ver_estado(carrito, total, presupuesto)
            elif opcion == 4:
                ver_ticket(carrito, total)
            elif opcion == 0:
                # Se guarda al salir para no perder los datos de la sesión
                guardar_compra(carrito, total)
                print("\nCompra finalizada y registrada.")
                print("\n¡Gracias por comprar en la tienda escolar!")
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada inválida.")
 
# Permite probar el juego de forma independiente antes de integrarlo al menú grupal
if __name__ == "__main__":
    juego_tienda()