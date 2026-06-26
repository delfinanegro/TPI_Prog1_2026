# =========================
# TIENDA ESCOLAR - ETAPA 3
# Persistencia en archivo
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
        opcion = int(input("\nSeleccione: ")) - 1

        if 0 <= opcion < len(productos):
            precio = precios[opcion]

            if total + precio <= presupuesto:
                carrito.append(productos[opcion])
                total += precio
                print("✔ Agregado")
            else:
                print("✘ Sin presupuesto")

    except ValueError:
        print("Error")

    return carrito, total


def guardar_compra(carrito, total):
    # NUEVO: guardado en archivo
    with open("compras.txt", "a") as archivo:
        archivo.write(f"Productos: {carrito}\n")
        archivo.write(f"Total: {total}\n")
        archivo.write("----------------\n")


def juego_tienda():
    presupuesto = 1000
    carrito = []
    total = 0

    print("TIENDA ESCOLAR")

    while True:
        print("\n1. Comprar")
        print("0. Salir")

        try:
            op = int(input("Opción: "))

            if op == 1:
                carrito, total = comprar_producto(carrito, total, presupuesto)

            elif op == 0:
                # NUEVO: guardo al salir
                guardar_compra(carrito, total)
                print("Guardado en archivo")
                break

        except ValueError:
            print("Error")


if __name__ == "__main__":
    juego_tienda()