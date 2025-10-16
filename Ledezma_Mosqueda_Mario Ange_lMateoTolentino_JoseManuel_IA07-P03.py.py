#NIM
import random

def formato(x):
    """
    Divide un número x en dos partes, una de las cuales puede ser 1 carta mayor si x es impar.
    """
    filas = x // 2  # División de enteros para la primera fila
    resto = x % 2   # El resto será 1 si el número es impar, 0 si es par
    
    print(f"Las filas son: {x}")
    print("|" * (filas + resto)) # Sumamos el resto a la primera fila
    print("|" * filas)          # La segunda fila siempre tendrá la parte entera de la división

def ai_move(n):
    """
    Calcula el movimiento óptimo o aleatorio para el jugador.
    Intenta dejar al oponente en una posición perdedora (n % 10 en {0, 1, 2}).
    """
    if n < 3:
        return 0  # No se llama en este caso
    possible = list(range(3, min(7, n) + 1))
    good = [k for k in possible if (n - k) % 10 in (0, 1, 2)]
    if good:
        return random.choice(good)
    else:
        return random.choice(possible)

def juego(c):
    cartasTotales = c
    current_player = 1  # Empieza el Jugador 1
    
    while cartasTotales >= 3:
        print(f"Jugador {current_player}")
        retirar = ai_move(cartasTotales)
        print(f"retira: {retirar}")
        cartasTotales -= retirar
        formato(cartasTotales)
        
        if cartasTotales < 3:
            print(f"Jugador {current_player} gana!")
            break
        
        current_player = 3 - current_player  # Cambiar jugador: 1 -> 2, 2 -> 1

def instrucciones():
    """
    Genera un número aleatorio de cartas y muestra las pilas.
    """
    cartas = random.randint(27, 60)
    print("--------NIM-------")
    print(f"Número de cartas a tomar: {cartas}")
    print("minimo de cartas a retirar: 3")
    print("maximo de cartas a retirar: 7")
    formato(cartas)
    juego(cartas)

# Ejecutar el juego
instrucciones()

#Integrantes del equipo
#Ledezma Mosqueda Mario Angel
#Mateo Tolentino Jose Manuel