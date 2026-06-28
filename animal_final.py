
# Librería para seleccionar un animal al azar
import random

# Lista de animales disponibles para jugar
animales = ["PERRO", "GATO", "LEON", "JIRAFA", "MONO", "OSO", "TIGRE"]

# Solicita el nombre del jugador
def datos_usuario():
    usuario = input("Ingrese su nombre: ")
    return usuario

# Selecciona un animal al azar de la lista
def seleccionar_animal():
    return random.choice(animales)

# Muestra el estado actual del juego
# Recorre el animal letra por letra y muestra las adivinadas
# Las que todavía no fueron descubiertas aparecen como "_"
# Devuelve la cantidad de letras encontradas
def mostrar_estado(animal, letras):
    completas = 0

    print("\nAnimal:")

    for letra in animal:
        if letra in letras:
            print(letra, end=" ")
            completas += 1
        else:
            print("_", end=" ")

    print()

    return completas

# Guarda el resultado de la partida en un archivo de texto
# Se utiliza el modo "a" para agregar cada partida sin borrar las anteriores
def guardar_partida(usuario, puntaje):

    with open("ranking.txt", "a") as archivo:
        archivo.write(f"{usuario},{puntaje}\n")

# Muestra el ranking guardado en el archivo
# Si el archivo no existe informa que todavía no hay partidas registradas
def ver_ranking():

    print("\n------ RANKING ------")

    try:
        with open("ranking.txt", "r") as archivo:

            for linea in archivo:
                print(linea.strip())

    except FileNotFoundError:
        print("Todavía no hay partidas registradas.")

# Muestra el resultado final de la partida
# Indica el animal que salió y si el jugador ganó o perdió
def ver_resultado(animal, puntaje):

    print("\n..............................")
    print("      RESULTADO FINAL")
    print("..............................")

    print("Animal:", animal)

    if puntaje == 1:
        print("Estado: GANASTE")
    else:
        print("Estado: PERDISTE")

    print("..............................")

# Función principal del juego
# Controla los intentos, las letras ingresadas y determina si el jugador gana o pierde
def jugar(usuario):

    # Selecciona un animal al azar
    animal = seleccionar_animal()

    # Lista donde se guardan las letras ingresadas
    letras = []

    # Cantidad máxima de intentos
    intentos = 6

    # Puntaje inicial
    puntaje = 0

    # El juego continúa mientras queden intentos
    while intentos > 0:

        # Muestra el estado actual de la palabra
        completas = mostrar_estado(animal, letras)

        # Si descubrió todas las letras gana la partida
        if completas == len(animal):

            print("\n¡Ganaste!")

            puntaje = 1

            # Guarda automáticamente el resultado
            guardar_partida(usuario, puntaje)

            # Muestra el resultado final
            ver_resultado(animal, puntaje)

            return

        # Solicita una letra al jugador
        letra = input("Ingrese una letra: ").upper()

        # Solo agrega la letra si todavía no fue ingresada
        if letra not in letras:

            letras.append(letra)

            # Si la letra no pertenece al animal pierde un intento
            if letra not in animal:

                intentos -= 1

                print("Incorrecto.")

        else:
            print("Esa letra ya fue ingresada.")

        # Muestra los intentos restantes
        print("Intentos restantes:", intentos)

    # Si se queda sin intentos pierde la partida
    print("\nPerdiste.")
    print("El animal era:", animal)

    # Guarda el resultado en el archivo
    guardar_partida(usuario, puntaje)

    # Muestra el resultado final
    ver_resultado(animal, puntaje)

# Función principal del programa
# Muestra el menú y permite acceder a las distintas opciones
def juego_animales():

    usuario = datos_usuario()

    print("\n༘˚⋆ 🐾 ADIVINA EL ANIMAL 🐾 ༘˚⋆")

    while True:

        print("\n───────── MENÚ ─────────")
        print("1. JUGAR")
        print("2. VER RANKING")
        print("0. VOLVER AL MENU PRINCIPAL")

        try:

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                jugar(usuario)

            elif opcion == 2:
                ver_ranking()

            elif opcion == 0:
                print("\n¡Gracias por jugar!")
                return

            else:
                print("Opción inválida.")

        except ValueError:
            print("Entrada inválida.")

# Permite ejecutar el juego directamente sin necesidad de otro programa
if __name__ == "__main__":
    juego_animales()