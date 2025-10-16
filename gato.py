import random
import time

# Definimos el tablero como una lista, donde cada posición es un espacio vacío
tablero = [' ' for x in range(10)]

# --- Funciones de Juego ---

def dibujar_tablero(tablero):
    """Función para dibujar el tablero en la consola."""
    print('   |   |')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
    print('---+---+---')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('---+---+---')
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('   |   |')

def es_espacio_libre(pos):
    """Verifica si la posición elegida está libre."""
    if pos < 1 or pos > 9:
        return False
    return tablero[pos] == ' '

def insertar_ficha(ficha, pos):
    """Inserta la ficha (X u O) en la posición indicada."""
    tablero[pos] = ficha

def tablero_esta_lleno():
    """Verifica si el tablero está completamente lleno."""
    return tablero.count(' ') == 1

def checar_ganador(tablero, ficha):
    """
    Verifica si una ficha ha ganado el juego.
    Retorna True si la ficha ha completado una línea de tres.
    """
    return ((tablero[1] == ficha and tablero[2] == ficha and tablero[3] == ficha) or
            (tablero[4] == ficha and tablero[5] == ficha and tablero[6] == ficha) or
            (tablero[7] == ficha and tablero[8] == ficha and tablero[9] == ficha) or
            (tablero[1] == ficha and tablero[4] == ficha and tablero[7] == ficha) or
            (tablero[2] == ficha and tablero[5] == ficha and tablero[8] == ficha) or
            (tablero[3] == ficha and tablero[6] == ficha and tablero[9] == ficha) or
            (tablero[1] == ficha and tablero[5] == ficha and tablero[9] == ficha) or
            (tablero[3] == ficha and tablero[5] == ficha and tablero[7] == ficha))

# --- Lógica de la Computadora ---

def movimiento_computadora(tablero, ficha_jugador):
    """
    La computadora elige un movimiento basado en la estrategia: 
    Ganar > Bloquear > Centro > Esquinas > Lados
    """
    posibles_movimientos = [x for x, letra in enumerate(tablero) if letra == ' ' and x != 0]
    ficha_oponente = 'X' if ficha_jugador == 'O' else 'O'

    # 1. Checar si la computadora puede GANAR
    for i in posibles_movimientos:
        tablero_copia = tablero[:]
        tablero_copia[i] = ficha_jugador
        if checar_ganador(tablero_copia, ficha_jugador):
            insertar_ficha(ficha_jugador, i)
            return

    # 2. Checar si el oponente puede ganar (y BLOQUEARLO)
    for i in posibles_movimientos:
        tablero_copia = tablero[:]
        tablero_copia[i] = ficha_oponente
        if checar_ganador(tablero_copia, ficha_oponente):
            insertar_ficha(ficha_jugador, i)
            return

    # 3. Tomar el CENTRO si está disponible
    if 5 in posibles_movimientos:
        insertar_ficha(ficha_jugador, 5)
        return

    # 4. Tomar una ESQUINA
    esquinas_abiertas = [i for i in posibles_movimientos if i in [1, 3, 7, 9]]
    if len(esquinas_abiertas) > 0:
        insertar_ficha(ficha_jugador, random.choice(esquinas_abiertas))
        return

    # 5. Tomar un LADO
    lados_abiertos = [i for i in posibles_movimientos if i in [2, 4, 6, 8]]
    if len(lados_abiertos) > 0:
        insertar_ficha(ficha_jugador, random.choice(lados_abiertos))
        return

# --- Lógica del Humano ---

def movimiento_humano():
    """Solicita al jugador humano que ingrese una posición válida."""
    while True:
        try:
            pos = int(input("Ingresa tu movimiento (1-9): "))
            if es_espacio_libre(pos):
                insertar_ficha('X', pos)
                break
            else:
                print("Posición inválida o ya ocupada. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número entre 1 y 9.")

# --- Selección del Modo de Juego ---

def elegir_modo_juego():
    """Pregunta al usuario si quiere jugar contra la computadora o ver dos computadoras."""
    while True:
        modo = input("¿Quieres jugar contra la computadora (C) o ver dos computadoras jugar (D)? [C/D]: ").strip().upper()
        if modo in ['C', 'D']:
            return modo
        print("Opción inválida. Ingresa 'C' para jugar contra la computadora o 'D' para dos computadoras.")

# --- Bucle Principal del Juego ---

def main():
    """Función principal que ejecuta el juego."""
    print("¡Bienvenido al Gato!")
    modo = elegir_modo_juego()
    
    if modo == 'C':
        print("Tú eres 'X' y la computadora es 'O'.")
    else:
        print("Computadora 'X' vs Computadora 'O'.")
    
    dibujar_tablero(tablero)
    turno = 'X'  # Comienza el jugador 'X'

    while True:
        if modo == 'C' and turno == 'X':
            print("Tu turno (X)...")
            movimiento_humano()
        else:
            print(f"Turno de la Computadora ({turno})...")
            time.sleep(1)  # Pausa para visualizar el juego
            movimiento_computadora(tablero, turno)

        dibujar_tablero(tablero)

        if checar_ganador(tablero, turno):
            if modo == 'C' and turno == 'X':
                print("¡Has ganado!")
            else:
                print(f"¡La Computadora ({turno}) ha ganado!")
            break

        if tablero_esta_lleno():
            print("¡Empate! ¡Qué buen juego!")
            break

        # Cambiar turno
        turno = 'O' if turno == 'X' else 'X'

# Ejecutar el juego
main()

#Integrantes del equipo 
#Ledezma Mosqueda Mario Angel
#Mateo Tolentino Jose Manuel