# Importamos los archivos donde están los juegos
from tienda_escolar import juego_tienda
from carrera_de_numeros import juego_matematica
from animal_final import juego_animales
from juego_capitales_final import juego_capitales


# Bienvenida al programa
print("══════════════════════════════════════")
print("        🎮 PLAY.IN EDUGAMES 🎮")
print("══════════════════════════════════════")

# Solicitamos el nombre del usuario una sola vez
usuario = input("\n Ingresá tu nombre de usuario: ")


# Función que muestra el menú principal
def menu():

    print("\n══════════════════════════════════════")
    print("           MENÚ PRINCIPAL")
    print("══════════════════════════════════════")

    print("1. 🛒 Tienda Escolar")
    print("2. 🐾 Adivina el Animal")
    print("3. 🌎 Capitales de América")
    print("4. 🔢 Carrera de Números")
    print("0. 🚪 Salir")

    opcion = input("\nSeleccione una opción: ")

    # Según la opción elegida se ejecuta el juego correspondiente

    if opcion == "1":
        juego_tienda()
        menu()      # Al finalizar el juego vuelve al menú

    elif opcion == "2":
        juego_animales(usuario)
        menu()

    elif opcion == "3":
        juego_capitales(usuario)
        menu()

    elif opcion == "4":
        juego_matematica(usuario)
        menu()

    elif opcion == "0":
        print("\n¡Gracias por jugar en Play.In EduGames! ") #algun emoji?

    else:
        print("\nOpción inválida. Por favor, elegí una opción del 0 al 4.")
        menu()      # Si se equivoca, vuelve a mostrar el menú


# Punto de entrada del programa
if __name__ == "__main__":
    menu()