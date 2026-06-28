import random
import time

def seleccionar_dificultad():
    """Solicita y valida la dificultad del juego."""
    while True:
        print("\n--- SELECCIONA LA DIFICULTAD ---")
        print("1. Fácil (Sumas y Restas)")
        print("2. Intermedio (Tablas de Multiplicar)")
        dificultad = int(input("Ingresa tu opción (1 o 2): "))
        
        try:
            if dificultad == 1 or dificultad == 2:
                return dificultad
            else:
                print("Por favor, elige una opción válida: 1 o 2.")
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