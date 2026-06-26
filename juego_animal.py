# Librería para elegir un animal al azar
import random

# Lista de animales del juego
animales = ["PERRO", "GATO", "LEON", "JIRAFA", "MONO", "OSO", "TIGRE"]

# Pide el usuario del jugador
def datos_usuario():
    usuario = input("Ingrese su nombre: ")
    return usuario

# Elige un animal al azar
def seleccionar_animal():
    animal = random.choice(animales)
    return animal

# Juego principal
def jugar_animal():

    # Selecciona un animal
    animal = seleccionar_animal()

    # Guarda las letras ingresadas
    letras = []

    # Cantidad de intentos
    intentos = 6

    # Puntaje inicial
    puntaje = 0

    # Se repite mientras queden intentos
    while intentos > 0:

        completas = 0

        print("\nAnimal:")

        # Recorre cada letra del animal
        for letra in animal:

            # Si la letra ya fue adivinada la muestra
            if letra in letras:
                print(letra, end=" ")
                completas += 1

            # Si no fue adivinada muestra _
            else:
                print("_", end=" ")

        print()

        # Si completó toda la palabra gana
        if completas == len(animal):
            print("¡Ganaste!")
            puntaje = 1
            return puntaje

        # Pide una letra
        letra = input("Ingrese una letra: ").upper()

        # Guarda la letra en la lista
        letras.append(letra)

        # Si la letra no existe pierde un intento
        if letra not in animal:
            intentos -= 1
            print("Incorrecto")
            print("Intentos:", intentos)

    # Si se queda sin intentos pierde
    print("Perdiste")
    print("El animal era:", animal)

    return puntaje

# Guarda el puntaje en un archivo
def guardar_puntaje(usuario, puntaje):

    archivo = open("ranking.txt", "a")

    archivo.write(usuario + "," + str(puntaje) + "\n")

    archivo.close()

# Muestra el ranking
def ver_ranking():

    print("\n--- RANKING ---")

    try:

        archivo = open("ranking.txt", "r")

        for linea in archivo:
            print(linea.strip())

        archivo.close()

    except:
        print("No hay ranking.")

# Menú principal
def menu_principal():

    usuario = datos_usuario()

    opcion = -1

    # Se repite hasta elegir salir
    while opcion != 0:

        print("\n1 - Jugar Adivina el Animal")
        print("2 - Ver Ranking")
        print("0 - Salir")

        try:

            opcion = int(input("Ingrese una opción: "))

            if opcion == 1:

                puntaje = jugar_animal()

                guardar_puntaje(usuario, puntaje)

            elif opcion == 2:

                ver_ranking()

            elif opcion == 0:

                print("Programa finalizado.")

        except ValueError:

            print("Ingrese un número válido.")

# Inicia el programa
menu_principal()