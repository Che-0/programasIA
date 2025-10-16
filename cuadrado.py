#Cuadrado
import random
import copy

# Función para dibujar el tablero
def dibujar_tablero(tablero):
    """Función para dibujar el tablero actual en la consola."""
    print("+---+---+---+")
    for fila in tablero:
        print(f"| {fila[0] if fila[0] != ' ' else ' '} | {fila[1] if fila[1] != ' ' else ' '} | {fila[2] if fila[2] != ' ' else ' '} |")
        print("+---+---+---+")

# Generar un tablero inicial con algunos números prellenados de manera consistente
def generar_tablero_inicial():
    """Genera un tablero vacío o con prellenados consistentes con un cuadrado mágico."""
    # Usamos la solución base y aplicamos una transformación válida (rotación o reflexión)
    solucion_base = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    
    # Aplicar una rotación o reflexión aleatoria para variedad
    transformaciones = [
        lambda m: m,  # Original
        lambda m: [list(reversed(col)) for col in zip(*m)],  # Rotación 90° clockwise
        lambda m: [list(reversed(row)) for row in m],  # Reflexión horizontal
        lambda m: [row[::-1] for row in m[::-1]],  # Rotación 180°
        # Se pueden agregar más si se desea
    ]
    transformacion = random.choice(transformaciones)
    solucion = transformacion(solucion_base)
    
    # Crear tablero vacío
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    
    # Poner algunos números prellenados (2 por defecto, consistentes)
    numeros_a_mostrar = 2
    posiciones = [(i, j) for i in range(3) for j in range(3)]
    random.shuffle(posiciones)
    for pos in posiciones[:numeros_a_mostrar]:
        i, j = pos
        tablero[i][j] = solucion[i][j]
    
    return tablero

# Verificar si un número puede colocarse (con más pruning para optimización)
def es_valido(tablero, fila, col, num):
    """Verifica si es válido colocar el número 'num' en la posición (fila, col)."""
    # Verificar duplicados
    if any(num == tablero[i][j] for i in range(3) for j in range(3) if tablero[i][j] != ' '):
        return False
    
    # Colocar temporalmente
    original = tablero[fila][col]
    tablero[fila][col] = num
    
    # Función para verificar suma parcial de una línea (fila, col o diag)
    def suma_parcial(linea):
        valores = [x for x in linea if x != ' ']
        k = len(valores)
        if k == 0:
            return True
        suma = sum(valores)
        restantes = 3 - k
        if restantes == 0:
            return suma == 15
        # Pruning optimizado: suma actual + min/max posibles para restantes
        usados = set(x for row in tablero for x in row if x != ' ')
        disponibles = [n for n in range(1, 10) if n not in usados]
        if not disponibles:
            return False
        min_rest = sum(sorted(disponibles)[:restantes])
        max_rest = sum(sorted(disponibles, reverse=True)[:restantes])
        return suma + min_rest <= 15 <= suma + max_rest
    
    # Verificar fila
    if not suma_parcial(tablero[fila]):
        tablero[fila][col] = original
        return False
    
    # Verificar columna
    if not suma_parcial([tablero[i][col] for i in range(3)]):
        tablero[fila][col] = original
        return False
    
    # Verificar diagonal principal si aplica
    if fila == col:
        if not suma_parcial([tablero[i][i] for i in range(3)]):
            tablero[fila][col] = original
            return False
    
    # Verificar diagonal secundaria si aplica
    if fila + col == 2:
        if not suma_parcial([tablero[i][2 - i] for i in range(3)]):
            tablero[fila][col] = original
            return False
    
    tablero[fila][col] = original
    return True

# Backtracking optimizado
def resolver_cuadrado_magico(tablero):
    """Resuelve el cuadrado mágico usando backtracking con pruning."""
    # Encontrar la siguiente celda vacía (priorizar centro u otras para optimizar, pero para 3x3 es rápido)
    vacia = None
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                vacia = (i, j)
                break
        if vacia:
            break
    if not vacia:
        return True  # Tablero lleno, y por pruning ya es válido
    
    fila, col = vacia
    for num in range(1, 10):
        if es_valido(tablero, fila, col, num):
            tablero[fila][col] = num
            if resolver_cuadrado_magico(tablero):
                return True
            tablero[fila][col] = ' '  # Backtrack
    return False

# Función principal
def main():
    print("¡Resolviendo el Cuadrado Mágico con la computadora!")
    tablero = generar_tablero_inicial()
    
    print("\n--- Tablero inicial ---")
    dibujar_tablero(tablero)
    
    if resolver_cuadrado_magico(tablero):
        print("\n--- Solución encontrada ---")
        dibujar_tablero(tablero)
    else:
        print("\nNo se pudo resolver el cuadrado mágico con las precondiciones dadas.")
    
    print("\n¡Proceso completado!")

if __name__ == "__main__":
    main()
    
#Integrantes del equipo
#Ledezma Mosqueda Mario Angel
#Mateo Tolentino Jose Manuel