import random

animales = ["PERRO", "GATO", "LEON", "JIRAFA", "MONO", "OSO", "TIGRE"]

# 🔧 Asegura que el archivo de ranking exista desde el inicio
open("ranking_animales.txt", "a").close()

def seleccionar_animal():
    return random.choice(animales)

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

def guardar_partida(usuario, puntaje):
    with open("ranking_animales.txt", "a") as archivo:
        archivo.write(f"{usuario},{puntaje}\n")

def ver_ranking():

    print("\n------ RANKING ANIMALES ------")

    with open("ranking_animales.txt", "r") as archivo:
        contenido = archivo.readlines()

        if len(contenido) == 0:
            print("No hay partidas todavía.")
        else:
            for linea in contenido:
                print(linea.strip())

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

def jugar(usuario):

    animal = seleccionar_animal()
    letras = []
    intentos = 6
    puntaje = 0

    while intentos > 0:

        completas = mostrar_estado(animal, letras)

        if completas == len(animal):

            print("\n¡Ganaste!")
            puntaje = 1

            guardar_partida(usuario, puntaje)
            ver_resultado(animal, puntaje)

            return

        letra = input("Ingrese una letra: ").upper()

        if not letra.isalpha() or len(letra) != 1:
            print("Error: ingrese SOLO una letra.")
            continue

        if letra not in letras:

            letras.append(letra)

            if letra not in animal:
                intentos -= 1
                print("Incorrecto.")

        else:
            print("Esa letra ya fue ingresada.")

        print("Intentos restantes:", intentos)

    print("\nPerdiste.")
    print("El animal era:", animal)

    guardar_partida(usuario, puntaje)
    ver_resultado(animal, puntaje)

def juego_animales(usuario):

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

if __name__ == "__main__":
    usuario = input("Ingrese su nombre: ")
    juego_animales(usuario)