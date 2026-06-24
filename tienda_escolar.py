# =========================
# TIENDA ESCOLAR - ETAPA 2
# Agrego estado del carrito
# =========================

productos = ["Cuaderno", "Lápiz", "Goma", "Regla"]
precios = [300, 100, 50, 150]


def mostrar_productos():
    print("\nProductos disponibles:")
    for i in range(len(productos)):
        print(f"{i + 1}. {productos[i]} - ${precios[i]}")


def comprar_producto(carrito, total, presupuesto):
    mostrar_productos()

    try:
        opcion = int(input("\nSeleccione un producto: ")) - 1

        if 0 <= opcion < len(productos):
            precio = precios[opcion]

            if total + precio <= presupuesto:
                carrito.append(productos[opcion])
                total += precio
                print("✔ Producto agregado")
            else:
                print("✘ Sin presupuesto suficiente")
        else:
            print("✘ Opción inválida")

    except ValueError:
        print("✘ Error de entrada")

    return carrito, total


# NUEVO: estado del carrito
def ver_estado(carrito, total, presupuesto):
    print("\n--- ESTADO ---")
    print("Productos:", carrito if carrito else "Vacío")
    print("Total:", total)
    print("Saldo:", presupuesto - total)


def juego_tienda():
    presupuesto = 1000
    carrito = []
    total = 0

    print("TIENDA ESCOLAR")

    while True:
        print("\n1. Ver productos")
        print("2. Comprar")
        print("3. Ver estado")
        print("0. Salir")

        try:
            op = int(input("Opción: "))

            if op == 1:
                mostrar_productos()

            elif op == 2:
                carrito, total = comprar_producto(carrito, total, presupuesto)

            elif op == 3:
                ver_estado(carrito, total, presupuesto)

            elif op == 0:
                print("Saliendo...")
                break

        except ValueError:
            print("Error")


if __name__ == "__main__":
    juego_tienda()