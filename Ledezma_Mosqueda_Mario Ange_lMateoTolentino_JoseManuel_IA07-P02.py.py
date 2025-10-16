#quince
import random

# Lista de todas las combinaciones ganadoras que suman 15
winning_combos = [
    (1, 5, 9), (1, 6, 8),
    (2, 4, 9), (2, 5, 8), (2, 6, 7),
    (3, 4, 8), (3, 5, 7),
    (4, 5, 6)
]

# Verifica si un conjunto de números contiene una combinación que suma 15
def check_win(numbers):
    for combo in winning_combos:
        if all(x in numbers for x in combo):
            return True
    return False

# Función minimax para evaluar el mejor movimiento de la IA
def minimax(available, player_nums, comp_nums, is_max):
    if check_win(player_nums):
        return -1  # Jugador gana (malo para IA)
    if check_win(comp_nums):
        return 1   # IA gana (bueno)
    if not available:
        return 0   # Empate si no hay más números

    if is_max:  # Turno de la IA
        max_score = -float('inf')
        for move in available:
            new_available = available - {move}
            new_comp = comp_nums | {move}
            score = minimax(new_available, player_nums, new_comp, False)
            max_score = max(max_score, score)
        return max_score
    else:  # Turno del jugador
        min_score = float('inf')
        for move in available:
            new_available = available - {move}
            new_player = player_nums | {move}
            score = minimax(new_available, new_player, comp_nums, True)
            min_score = min(min_score, score)
        return min_score

# Elige el mejor movimiento para la IA
def get_best_move(available, player_nums, comp_nums):
    best_score = -float('inf')
    best_move = None
    for move in available:
        new_available = available - {move}
        new_comp = comp_nums | {move}
        if check_win(new_comp):
            return move  # Gana inmediatamente si puede
        score = minimax(new_available, player_nums, new_comp, False)
        if score > best_score:
            best_score = score
            best_move = move
    if best_move is None:
        best_move = random.choice(list(available))
    return best_move

# Función principal del juego
def play_game():
    available = set(range(1, 10))
    player_nums = set()
    comp_nums = set()
    current_turn = 'player'

    print("¡Juego de suma a 15!")
    print("Elige números del 1 al 9. Gana quien forme un trío que sume 15.")
    print("Si nadie lo logra, es empate. La IA juega de forma óptima.")

    while available:
        print("\nNúmeros disponibles:", sorted(available))
        print("Tus números:", sorted(player_nums))
        print("Números de la IA:", sorted(comp_nums))

        if current_turn == 'player':
            while True:
                try:
                    pick = int(input("Elige un número: "))
                    if pick in available:
                        break
                    print("Número inválido o ya elegido.")
                except ValueError:
                    print("Ingresa un número válido.")
            player_nums.add(pick)
            available.remove(pick)
            if check_win(player_nums):
                print("\n¡Ganaste! Tus números:", sorted(player_nums))
                return
        else:
            pick = get_best_move(available, player_nums, comp_nums)
            comp_nums.add(pick)
            available.remove(pick)
            print("\nLa IA elige:", pick)
            if check_win(comp_nums):
                print("\n¡La IA ganó! Números de la IA:", sorted(comp_nums))
                return

        current_turn = 'comp' if current_turn == 'player' else 'player'

    print("\nEmpate: nadie formó un trío que sume 15.")
    print("Tus números:", sorted(player_nums))
    print("Números de la IA:", sorted(comp_nums))

# Iniciar el juego
if __name__ == "__main__":
    play_game()
    
#Integrantes del equipo
#Ledezma Mosqueda Mario Angel
#Mateo Tolentino Jose Manuel