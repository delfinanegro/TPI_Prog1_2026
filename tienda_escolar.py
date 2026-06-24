# =========================
# TIENDA ESCOLAR - ETAPA 1
# Estructura base del simulador
# =========================

# Listas paralelas (producto - precio)
productos = ["Cuaderno", "Lápiz", "Goma", "Regla"]
precios = [300, 100, 50, 150]


# Muestra productos disponibles
def mostrar_productos():
    print("\nProductos disponibles:")
    for i in range(len(productos)):
        print(f"{i + 1}. {productos[i]} - ${precios[i]}")


# Función de compra básica (sin estado avanzado)
def comprar_producto(carrito, total, presupuesto):
    mostrar_productos()

    try:
        opcion = int(input("\nSeleccione un producto: ")) - 1

        # validación básica
        if 0 <= opcion < len(productos):
            precio = precios[opcion]

            if total + precio <= presupuesto:
                carrito.append(productos[opcion])
                total += precio
                print("Producto agregado.")
            else:
                print("No hay presupuesto suficiente.")
        else:
            print("Opción inválida.")

    except ValueError:
        print("Entrada inválida.")

    return carrito, total


def juego_tienda():
    presupuesto = 1000
    carrito = []
    total = 0

    print("TIENDA ESCOLAR - INICIO")

    while True:
        print("\n1. Ver productos")
        print("2. Comprar")
        print("0. Salir")

        try:
            op = int(input("Opción: "))

            if op == 1:
                mostrar_productos()

            elif op == 2:
                carrito, total = comprar_producto(carrito, total, presupuesto)

            elif op == 0:
                print("Fin del programa")
                break

            else:
                print("Opción inválida")

        except ValueError:
            print("Error de entrada")


if __name__ == "__main__":
    juego_tienda()