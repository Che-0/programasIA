# Función para resolver el puzzle de la Torre de Hanoi con salida gráfica
def TowerOfHanoi(n, source, destination, auxiliary, move_count=[0], towers=None):
    # Inicializar las torres si no se proporcionan (primera llamada)
    if towers is None:
        towers = {
            '1': list(range(n, 0, -1)),  # Vara fuente con discos [n, n-1, ..., 1]
            '2': [],                     # Vara auxiliar, inicialmente vacía
            '3': []                      # Vara destino, inicialmente vacía
        }
    
    # Calcular e imprimir el total de movimientos requeridos: 2^n - 1
    if move_count == [0]:
        total_moves = (2 ** n) - 1
        print(f"Total de movimientos requeridos para {n} discos: {total_moves}")
        print_towers(towers)  # Mostrar estado inicial
    
    # Caso base: mover un disco
    if n == 1:
        move_count[0] += 1
        disk = towers[source].pop()  # Retirar disco de la vara fuente
        towers[destination].append(disk)  # Colocar disco en la vara destino
        print(f"Movimiento {move_count[0]}: Mover disco 1 de vara {source} a vara {destination}")
        print_towers(towers)  # Mostrar estado de las torres después del movimiento
        return
    
    # Paso recursivo 1: Mover n-1 discos de fuente a auxiliar
    TowerOfHanoi(n-1, source, auxiliary, destination, move_count, towers)
    
    # Mover el disco n de fuente a destino
    move_count[0] += 1
    disk = towers[source].pop()  # Retirar disco de la vara fuente
    towers[destination].append(disk)  # Colocar disco en la vara destino
    print(f"Movimiento {move_count[0]}: Mover disco {n} de vara {source} a vara {destination}")
    print_towers(towers)  # Mostrar estado de las torres después del movimiento
    
    # Paso recursivo 2: Mover n-1 discos de auxiliar a destino
    TowerOfHanoi(n-1, auxiliary, destination, source, move_count, towers)

# Función auxiliar para imprimir el estado actual de las torres
def print_towers(towers):
    print(f"Torres: [{''.join(map(str, towers['1']))}] [{''.join(map(str, towers['2']))}] [{''.join(map(str, towers['3']))}]")
    print()  # Línea en blanco para mayor legibilidad

# Código principal
n = 8  # Número de discos
# Llamar a la función con varas '1' (fuente), '3' (destino), '2' (auxiliar)
TowerOfHanoi(n, '1', '3', '2')


#Integrantes del equipo
#Ledezma Mosqueda Mario Angel
#Mateo Tolentino Jose Manuel
