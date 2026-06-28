# Importamos el archivo donde están los juegos
from tienda_escolar import juego_tienda
from carrera_de_numeros import juego_matematica
from animal_final import juego_animales


#Crear funcion para infgresar nombre de usuario del jugador
# Creamos un menú para que el usuario pueda elegir qué juego jugar

print("Bienvenido a Play.In EduGames")
usuario = input("Por favor, ingresa tu nombre de usuario: ")

def menu():
    print("--- Play.In EduGames ---")
    print('1. Jugar a la "Tienda Escolar"')
    print('2. Jugar a "Adivina el Animal"')
    print('3. Jugar a "Capitales de América"')
    print('4. Jugar a la "Carrera de Números"')
    print("0. Salir")
    opcion = input("Elegí una opción: ")
    

    if opcion == "1":
        juego_tienda()
    if opcion == "2":
        juego_animales()
    if opcion == "3":
        print("Capitales de América")
    if opcion == "4":
        juego_matematica(usuario)
    if opcion == "0":
        print("Gracias por jugar. ¡Hasta luego!")
    else:
        print("Opción inválida. Por favor, elige una opción del 1 al 4.")
        menu()  # Llamamos al menú nuevamente para que el usuario pueda elegir otra opción      

# Ejecutamos el menú
if __name__ == "__main__":
    menu()