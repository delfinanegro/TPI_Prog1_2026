# Importamos el archivo donde están los juegos
from tienda_escolar import juego_tienda

def menu():
    print("--- Play.In EduGames ---")
    print("1. Jugar a la Tienda Escolar")
    opcion = input("Elegí una opción: ")
    
    if opcion == "1":
        # Llamamos a la función que importamos arriba
        juego_tienda()

# Ejecutamos el menú
if __name__ == "__main__":
    menu()