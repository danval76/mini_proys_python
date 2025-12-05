import os
import time
import random
import sys

# Colores ANSI para la terminal
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"  # Amarillo brillante
ORANGE = "\033[33m"  # Naranja (Amarillo oscuro/standard)
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"

# --- ARTE ASCII ---

NUMERO_3 = YELLOW + r"""
    33333
   3333333
       33
       33
    3333
    3333
       33
       33
    333333
    3333
""" + RESET

NUMERO_2 = YELLOW + r"""
   22222
  2222222
       22
       22
       22
   2222222
   2222222
   22
   22
   222222
   2222222
""" + RESET

NUMERO_1 = YELLOW + r"""
      1111
    11 11
    11 11
    11 11
       11
       11
       11
    111111
    111111
""" + RESET

GO_TEXT = GREEN + r"""
   ¡¡ YA !!
""" + RESET

# --- FUNCIONES ---

def limpiar_pantalla():
    """Limpia la consola dependiendo del sistema operativo."""
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Mac/Linux
        os.system('clear')

def crear_bus(nombre, color):
    """
    Genera el arte ASCII del bus con el nombre personalizado dentro.
    Centra el nombre y lo recorta si es muy largo para mantener la forma.
    """
    # Recortamos a 18 caracteres máximo para que no rompa el dibujo
    # y lo centramos con espacios.
    nombre_ajustado = nombre[:18].center(18)
    
    bus = [
        color + r"   ____________________   " + RESET,
        color + r"  |__|__|__|__|__|__|__|  " + RESET,
        color + f"  |{nombre_ajustado}|)   " + RESET,
        color + r"  |---@-----------@--|)   " + RESET
    ]
    return bus

def mostrar_conteo():
    """Muestra la cuenta regresiva 3, 2, 1."""
    conteo = [NUMERO_3, NUMERO_2, NUMERO_1, GO_TEXT]
    for n in conteo:
        limpiar_pantalla()
        print("\n" * 5)
        lines = n.split('\n')
        for line in lines:
            print(" " * 20 + line)
        time.sleep(1)

def dibujar_pista(pos1, pos2, largo_pista, bus1_art, bus2_art):
    """
    Dibuja el estado actual de la carrera con los buses personalizados.
    """
    limpiar_pantalla()
    
    print(BOLD + "=== GRAN CARRERA DE AUTOBUSES ===" + RESET)
    print("=" * (largo_pista + 30)) # Techo de la pista
    
    # Dibujar Bus 1
    espacio1 = " " * pos1
    for linea in bus1_art:
        print(espacio1 + linea)
        
    print("-" * (largo_pista + 30)) # Divisor de carril
    
    # Dibujar Bus 2
    espacio2 = " " * pos2
    for linea in bus2_art:
        print(espacio2 + linea)
        
    print("=" * (largo_pista + 30)) # Suelo de la pista
    print(" " * (largo_pista + 20) + GREEN + "META" + RESET)

def seleccionar_configuracion(numero_bus):
    """Pide nombre y color para un bus específico."""
    print(f"\n{BOLD}--- CONFIGURACIÓN DEL BUS {numero_bus} ---{RESET}")
    nombre = input(f"Nombre del Bus {numero_bus}: ") or f"Bus {numero_bus}"
    
    # Lista de colores ampliada
    colores = {
        "1": ("Rojo", RED),
        "2": ("Verde", GREEN),
        "3": ("Amarillo", YELLOW),
        "4": ("Naranja", ORANGE),
        "5": ("Azul", BLUE),
        "6": ("Magenta", MAGENTA),
        "7": ("Cian", CYAN),
        "8": ("Blanco", WHITE)
    }
    
    print("Elige un color:")
    for k, (nom_color, cod_color) in colores.items():
        print(f"  {k}. {cod_color}{nom_color}{RESET}")
        
    eleccion = input("Opción (1-8): ")
    # Si la opción no es válida, usamos Blanco por defecto
    nombre_color, codigo_color = colores.get(eleccion, ("Blanco", WHITE))
    
    print(f"Has elegido: {codigo_color}{nombre} ({nombre_color}){RESET}")
    return nombre, codigo_color

def carrera():
    limpiar_pantalla()
    # Configuración inicial
    print(BOLD + "BIENVENIDO A LA CARRERA DE BUSES" + RESET)
    
    # Pedimos configuración para ambos buses
    nombre1, color1 = seleccionar_configuracion(1)
    nombre2, color2 = seleccionar_configuracion(2)
    
    # Generamos el arte de los buses con sus colores elegidos
    bus1_art = crear_bus(nombre1, color1)
    bus2_art = crear_bus(nombre2, color2)

    largo_pista = 60
    pos_bus1 = 0
    pos_bus2 = 0
    
    input(f"\n{BOLD}Presiona ENTER para iniciar el conteo...{RESET}")
    
    # 1. Iniciar Conteo
    mostrar_conteo()
    
    # 2. Bucle de la carrera
    ganador = None
    while pos_bus1 < largo_pista and pos_bus2 < largo_pista:
        # Movimiento aleatorio
        avance1 = random.randint(1, 3)
        avance2 = random.randint(1, 3)
        
        pos_bus1 += avance1
        pos_bus2 += avance2
        
        dibujar_pista(pos_bus1, pos_bus2, largo_pista, bus1_art, bus2_art)
        
        time.sleep(0.15)
        
    # 3. Determinar ganador usando los nombres ingresados
    if pos_bus1 >= largo_pista and pos_bus2 >= largo_pista:
        if pos_bus1 > pos_bus2:
            ganador = nombre1
        elif pos_bus2 > pos_bus1:
            ganador = nombre2
        else:
            ganador = "Empate (Foto Finish)"
    elif pos_bus1 >= largo_pista:
        ganador = nombre1
    else:
        ganador = nombre2
        
    # Mostramos el ganador con su color correspondiente (si ganó el 1 o el 2)
    color_ganador = WHITE
    if ganador == nombre1: color_ganador = color1
    if ganador == nombre2: color_ganador = color2
    
    print(f"\n\n{BOLD}¡El ganador es: {color_ganador}{ganador}{RESET}{BOLD}!{RESET}\n")

if __name__ == "__main__":
    try:
        carrera()
    except KeyboardInterrupt:
        print("\nCarrera cancelada.")