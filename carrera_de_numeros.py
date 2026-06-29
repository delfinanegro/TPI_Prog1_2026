import random
import time

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
    print(f" BOT: [{pista_b_str}] 🏁")

    print("=" * 40 + "\n")

def mostrar_ranking():
    """Lee y muestra las estadísticas guardadas en el archivo de texto."""
    print("\n===========================================")
    print("   📊 HISTORIAL DE LA CARRERA DE NÚMEROS   ")
    print("===========================================")
    try:
        with open("ranking_mate.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido.strip() == "":
                print("Aún no hay partidas registradas.")
            else:
                print(contenido)
    except FileNotFoundError:
        print("Aún no hay partidas registradas. ¡Sé el primero en jugar!")
    print("===========================================\n")

def juego_matematica(usuario):
    """Función principal del juego de matemática."""
    print(f'\n¡Bienvenido/a {usuario} a "La Carrera de números"!')

    dificultad = seleccionar_dificultad()
    if dificultad is None:
        print("Volviendo al menú principal...")
        return
    
    CONFIG_JUEGO = (0, 5) # (Posición inicial, Meta)
    pos_jugador = CONFIG_JUEGO[0]
    pos_bot = CONFIG_JUEGO[0]
    meta = CONFIG_JUEGO[1]
    aciertos = 0

    print("\n¡Preparados, listos... YA! 🏁")
    dibujar_pista(usuario, pos_jugador, pos_bot)

    while pos_jugador < meta and pos_bot < meta:
        
        # === TURNO DEL JUGADOR ===
        print(f"--- TURNO DE {usuario.upper()} ---")
        pregunta, respuesta_correcta = generar_operacion(dificultad)

        # Micro-bucle para validar que no ingrese letras
        while True:
            print(pregunta)
            respuesta_tipeada = input("Tu respuesta: ")
            
            try:
                respuesta_usuario = int(respuesta_tipeada)
                break  # Si el número es válido, sale del bucle de validación
            except ValueError:
                print("❌ ¡Entrada inválida! No ingresaste un número entero. Inténtalo de nuevo.\n")
        
        # Evalúa el resultado una única vez
        if respuesta_usuario == respuesta_correcta:
            print("¡Excelente! ¡Avanzas un casillero! 🎉")
            pos_jugador += 1
            aciertos += 1
        else:
            print(f"Incorrecto... El resultado real era {respuesta_correcta}. No avanzas.")
            
        dibujar_pista(usuario, pos_jugador, pos_bot)
        time.sleep(0.5)
        
        # Verificamos si el jugador ya ganó para frenar la ejecución
        if pos_jugador >= meta:
            break
            
        # === TURNO DEL BOT ===
        print("--- TURNO DEL BOT 🤖 ---")
        print("El BOT está pensando su respuesta...")
        time.sleep(2) 
        
        # El BOT tiene un 60% de probabilidad de acertar y avanzar
        if random.random() < 0.60:
            print("¡El BOT respondió correctamente y avanza! 🤖⚡")
            pos_bot += 1
        else:
            print("¡El BOT se equivocó de cálculo! Se queda en su lugar. ❌")

        dibujar_pista(usuario, pos_jugador, pos_bot)
        time.sleep(0.5)

    # --- DETERMINAR EL GANADOR Y GUARDAR EN ARCHIVO ---
    if pos_jugador >= meta:
        print(f"\n🏆 ¡FELICITACIONES {usuario.upper()}! ¡Ganaste la carrera y demostraste ser un/a genio/a de los números! 🎉")
        ranking(usuario, "Ganó", aciertos)
    else:
        print(f"\n🤖 El BOT llegó primero a la meta... ¡No te preocupes {usuario}, la próxima lo vas a vencer! 💪")
        ranking(usuario, "Perdió", aciertos)

    # --- SEGUNDO MENÚ (FIN DE JUEGO) ---
    while True:
        print("\n¿Qué deseas hacer ahora?")
        print("1. Volver a jugar (Revancha)")
        print("2. Ver historial de partidas (Ranking) 📊")
        print("0. Volver al menú principal")
        
        try:
            opcion_final = int(input("Ingresa tu opción: "))
            
            if opcion_final == 1:
                print("\n¡Preparando la pista para otra carrera!...")
                return juego_matematica(usuario) # Reinicia la partida
                
            elif opcion_final == 2:
                mostrar_ranking() # Imprime el bloc de notas y te vuelve a mostrar el menú
                
            elif opcion_final == 0:
                print("Volviendo al menú principal...")
                return # Destruye la función y regresa limpiamente al main.py
                
            else:
                print("Opción inválida. Por favor, elige 0, 1 o 2.")
        except ValueError:
            print("Error: Debes ingresar un número entero.")

#juego_matematica("Angelina")