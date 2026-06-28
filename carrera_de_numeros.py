import random

def seleccionar_dificultad():
    """Solicita y valida la dificultad del juego."""
    while True:
        print("\n--- SELECCIONA LA DIFICULTAD ---")
        print("1. Fácil (Sumas y Restas)")
        print("2. Intermedio (Tablas de Multiplicar)")
        print("0. Volver al menú principal.")
        
        try:
            opcion = int(input("Ingresa tu opción: "))
            if opcion == 1 or opcion == 2:
                return opcion
            elif opcion == 0:
                return None
            else:
                print("Por favor, elige una opción válida: 0, 1 o 2.")
        except ValueError:
            print("Error: Debes ingresar un número entero.")

def generar_operacion(dificultad):
    """Genera una pregunta matemática aleatoria y calcula su resultado."""
    operadores_facil = ["+", "-"]
    
    if dificultad == 1:
        num1 = random.randint(1, 40)
        num2 = random.randint(1, 20)
        operador = random.choice(operadores_facil)
        
        # Evitamos resultados negativos para nivel primario
        if operador == '-' and num1 < num2:
            num1, num2 = num2, num1 #Sobreescribe las variables intercambiandolas
            
        pregunta = f"¿Cuánto es {num1} {operador} {num2}?"
        if operador == '+':
            resultado_correcto = num1 + num2
        else:
            resultado_correcto = num1 - num2
    else:
        # Nivel Intermedio: Multiplicaciones
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        pregunta = f"¿Cuánto es {num1} x {num2}?"
        resultado_correcto = num1 * num2
        
    return pregunta, resultado_correcto

def dibujar_pista(usuario, pos_jugador, pos_bot):
    """Dibuja la pista de carreras en la consola."""
    largo_pista = 5
    print("\n" + "=" * 40)
    
    # LINEA DEL JUGADOR
    pista_jugador = ["-"] * largo_pista
    # # Reemplaza el guion ('-') por el emoji en el índice correspondiente a la posición del corredor
    if pos_jugador < largo_pista:
        pista_jugador[pos_jugador] = "🏃"
    #Transforma la lista en una cadena de texto para mostrarla en la consola
    pista_j_str = "".join(pista_jugador)
    print(f" {usuario.upper()}: [{pista_j_str}] 🏁")
    
    # LINEA DEL BOT
    pista_bot = ["-"] * largo_pista
    if pos_bot < largo_pista:
        pista_bot[pos_bot] = "🤖"
    pista_b_str = "".join(pista_bot)
    print(f" BOT    : [{pista_b_str}] 🏁")

    print("=" * 40 + "\n")

def juego_matematica(usuario):
    """Función principal del juego de matemática."""
    print(f'\n¡Bienvenido/a {usuario} a "La Carrera de números"!')
    dificultad = seleccionar_dificultad()
    pos_jugador = 0
    pos_bot = 0
    dibujar_pista(usuario, pos_jugador, pos_bot)