#Diccionario que almacena los países como claves y sus capitales como valores.
capitales = {
    "Argentina":"Buenos Aires",
    "Chile":"Santiago", 
    "Uruguay":"Montevideo", 
    "Perú":"Lima", 
    "México":"Ciudad de México",
    "Brasil":"Brasilia",
    "Bolivia":"La Paz",
    "Colombia":"Bogotá",
    "Ecuador":"Quito",
    "Venezuela":"Caracas"}

#Solicita el nombre del usuario que jugará, para luego identificarlo en el ranking.
def datos_usuario ():
    usuario = input("Ingrese su nombre de usuario: ")
    return usuario

#Menú principal del sistema para que el usuario elija entre jugar, ver el ranking o salir.
def menu_principal ():
    opcion = -1
    #Bucle while para repetirse hasta que el usuario elija salir.
    while opcion != 0:
        print ("1 - Jugar a Capitales del Mundo")
        print ("2 - Ver Ranking")
        print ("0 - Salir")

        try:
            opcion = int(input("\nIngrese una opción (1, 2 o 0): "))

            if opcion == 1:
                puntaje = jugar_capitales()
                guardar_puntaje(usuario, puntaje)
            elif opcion == 2:
                ver_ranking()
            elif opcion == 0:
                print ("Opción N°0 elegida. El programa finalizó.")
                break
        except ValueError:
            print ("Error. Ingrese un dato válido.")

#Librería importada para seleccionar capitales y paises de manera aleatoria.
import random

def seleccionar_pais():
#Selecciona de manera aleatoria una clave (pais) dentro de capitales.
    pais = random.choice(list(capitales.keys()))
    capital_correcta = capitales[pais]
    return pais, capital_correcta

#Función principal del juego.
def jugar_capitales():
    print("Bienvenido al juego.")
    pais, capital_correcta = seleccionar_pais()
    puntaje = 0
    #Crea una lista de capitales para generar opciones.
    lista_capitales = list(capitales.values())
    #Lista vacía para guardar las opciones incorrectas.
    incorrectas = []

    #Genera 3 capitales incorrectas:
    while len(incorrectas) < 3:
        #Se eligen capitales aleatiorias con random.choice.
        capital = random.choice(lista_capitales)
        if capital != capital_correcta and capital not in incorrectas:
            #Si la correcta no está dentro de las 3 incorrectas, la agrega a la lista de opciones.
            incorrectas.append(capital)
                
    #Agrega la correcta a las opciones.
    incorrectas.append(capital_correcta)
    #Mezcla las opciones con shuffle para que no queden en un orden fijo. Sino siempre la respuesta correcta estaría al final.
    random.shuffle(incorrectas)

    #Muestra la pregunta al usuario.
    print(f"\n¿Cuál es la capital de {pais}? ")

    #Recorre las respuestas incorrectas y las muestra numeradas.
    for i in range(len(incorrectas)):
        print(f"{i+1} - {incorrectas[i]}")

    #El usuario selecciona una opción.
    respuesta = int(input("\nIngrese una opción: "))
    #Se convierte la opción numérica en el valor real de la lista.
    capital_elegida = incorrectas [respuesta - 1]

    #Si acierta, suma un punto. Si falla, muestra la respuesta correcta.
    if capital_elegida == capital_correcta:
        print ("¡Correcto! Acertaste :). ¡Seguí jugando!")
        puntaje += 1
    else:
        print("Incorrecto.")
        print ("La respuesta correcta era: ", capital_correcta)
    return puntaje

#Guarda el nombre del usuario y su puntaje en un archivo.
def guardar_puntaje(usuario, puntaje):
    archivo = open ("ranking.txt", "a")
    archivo.write (usuario + "," + str(puntaje) + "\n")
    archivo.close()

#Lee el archivo del ranking.
def ver_ranking():
    print ("\n --- RANKING --- \n")

    try: 
        archivo = open ("ranking.txt", "r")

        for linea in archivo:
            datos = linea.strip().split(",")
            usuario = datos[0]
            puntaje = int(datos[1])

            print(usuario, "-", puntaje)
        archivo.close()
    except:
        print("No hay ranking aún.")

        
usuario = datos_usuario()
menu_principal()

#CORREGIR: SI INGRESO 0 NO TERMINA EL PROGRAMA