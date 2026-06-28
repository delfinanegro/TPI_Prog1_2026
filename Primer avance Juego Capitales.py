capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Perú": "Lima",
    "México": "Ciudad de México"
}


def datos_usuario():
    usuario = input("Ingrese su nombre de usuario: ")
    return usuario


def menu_principal():
    opcion = -1

    while opcion != 0:
        print("\n1 - Jugar a Capitales del Mundo")
        print("2 - Ver Ranking")
        print("0 - Salir")

        opcion = int(input("\nIngrese una opción (1, 2 o 0): "))

        if opcion == 1:
            jugar_capitales()

        elif opcion == 2:
            print("Opción N°2 elegida.")

        elif opcion == 0:
            print("Opción N°0 elegida. El programa finalizó.")

        else:
            print("Error. Ingrese un dato válido.")


# Se selecciona aleatoriamente un país del diccionario.
# (Investigado con ayuda de IA utilizando random.choice)
import random

def seleccionar_pais():
    pais = random.choice(list(capitales.keys()))
    capital_correcta = capitales[pais]

    return pais, capital_correcta


def jugar_capitales():

    print("\nBienvenido al juego.")

    pais, capital_correcta = seleccionar_pais()

    # Lista con todas las capitales del diccionario.
    lista_capitales = list(capitales.values())

    # Lista donde se almacenarán las opciones incorrectas.
    incorrectas = []

    # Obtener tres capitales incorrectas distintas.
    while len(incorrectas) < 3:

        capital = random.choice(lista_capitales)

        if capital != capital_correcta and capital not in incorrectas:
            incorrectas.append(capital)

    # Agregar la respuesta correcta.
    incorrectas.append(capital_correcta)

    # Mezclar todas las opciones.
    random.shuffle(incorrectas)

    # Mostrar la pregunta.
    print(f"\n¿Cuál es la capital de {pais}?")

    # Mostrar las cuatro opciones.
    for i in range(len(incorrectas)):
        print(f"{i + 1} - {incorrectas[i]}")

    respuesta = int(input("\nIngrese una opción: "))

    capital_elegida = incorrectas[respuesta - 1]

    if capital_elegida == capital_correcta:
        print("¡Correcto!")
    else:
        print("Incorrecto.")
        print("La respuesta correcta era:", capital_correcta)