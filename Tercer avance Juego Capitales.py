# Diccionario que almacena los países como claves y sus capitales como valores.
capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Perú": "Lima",
    "México": "Ciudad de México",
    "Brasil": "Brasilia",
    "Bolivia": "La Paz",
    "Colombia": "Bogotá",
    "Ecuador": "Quito",
    "Venezuela": "Caracas"
}

# Librería importada para seleccionar países y capitales de manera aleatoria.
import random

# Solicita el nombre del usuario que jugará.
def datos_usuario():
    usuario = input("Ingrese su nombre de usuario: ")
    return usuario

# Selecciona un país al azar.
def seleccionar_pais():
    pais = random.choice(list(capitales.keys()))
    capital_correcta = capitales[pais]
    return pais, capital_correcta

# Función principal del juego.
def jugar_capitales():

    pais, capital_correcta = seleccionar_pais()
    puntaje = 0

    lista_capitales = list(capitales.values())
    incorrectas = []

    while len(incorrectas) < 3:
        capital = random.choice(lista_capitales)

        if capital != capital_correcta and capital not in incorrectas:
            incorrectas.append(capital)

    incorrectas.append(capital_correcta)
    random.shuffle(incorrectas)

    print(f"\n¿Cuál es la capital de {pais}?")

    for i in range(len(incorrectas)):
        print(f"{i + 1} - {incorrectas[i]}")

    # Validación de respuesta
    while True:
        try:
            respuesta = int(input("\nIngrese una opción: "))

            if 1 <= respuesta <= 4:
                break

            print("Debe ingresar un número entre 1 y 4.")

        except ValueError:
            print("Ingrese un número válido.")

    capital_elegida = incorrectas[respuesta - 1]

    if capital_elegida == capital_correcta:
        print("\n¡Correcto! Acertaste.")
        puntaje += 1
    else:
        print("\nIncorrecto.")
        print("La respuesta correcta era:", capital_correcta)

    return puntaje

# Muestra un resumen de la partida.
def mostrar_resultado(usuario, puntaje):
    print("\n═══════════════════════")
    print("📋 RESUMEN DE PARTIDA")
    print("═══════════════════════")
    print("Jugador:", usuario)
    print("Puntaje:", puntaje)
    print("═══════════════════════")

# Guarda el puntaje en un archivo.
def guardar_puntaje(usuario, puntaje):
    archivo = open("ranking.txt", "a")
    archivo.write(usuario + "," + str(puntaje) + "\n")
    archivo.close()

# Lee el archivo del ranking y suma los puntajes de cada jugador.
def ver_ranking():
    print("\n══════════════════════════")
    print("🏆 RANKING DE JUGADORES 🏆")
    print("══════════════════════════\n")

    try:
        archivo = open("ranking.txt", "r")

        ranking = {}

        for linea in archivo:
            datos = linea.strip().split(",")

            usuario = datos[0]
            puntaje = int(datos[1])

            if usuario in ranking:
                ranking[usuario] += puntaje
            else:
                ranking[usuario] = puntaje

        archivo.close()

        # Ordena de mayor a menor puntaje
        ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

        posicion = 1

        for usuario, puntaje in ranking_ordenado:
            print(f"{posicion}. {usuario} - {puntaje} puntos")
            posicion += 1

    except:
        print("No hay ranking aún.")

# Menú principal.
def menu_principal():
    opcion = -1

    print("\n══════════════════════════════════")
    print("🌎 CAPITALES DE AMÉRICA LATINA 🌎")
    print("══════════════════════════════════")

    while opcion != 0:

        print("\n1 - Jugar a Capitales de América Latina")
        print("2 - Ver Ranking")
        print("0 - Salir")

        try:
            opcion = int(input("\nIngrese una opción (1, 2 o 0): "))

            if opcion == 1:
                puntaje = jugar_capitales()
                mostrar_resultado(usuario, puntaje)
                guardar_puntaje(usuario, puntaje)

            elif opcion == 2:
                ver_ranking()

            elif opcion == 0:
                print("\n══════════════════════════════")
                print("🗺️   Gracias por jugar 🗺️")
                print("¡Hasta la próxima!")
                print("══════════════════════════════")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Error. Ingrese un dato válido.")

# Programa principal
usuario = datos_usuario()
menu_principal()
