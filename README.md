# Torre de Hanoi - Solución Recursiva con Visualización Gráfica

## Descripción
Este proyecto implementa una solución recursiva para el puzzle clásico de la **Torre de Hanoi** , **15**, **Cuadrado magico**, **Gato** y **NIM**    en Python. El programa resuelve el puzzle para un número dado de discos (`n`) y muestra gráficamente el estado de las tres varas después de cada movimiento, representándolas como listas (por ejemplo, `[321] [] []`). Además, calcula el número total de movimientos necesarios (`2^n - 1`) y numera cada movimiento para facilitar el seguimiento.

El código utiliza una función recursiva para mover los discos entre las varas (fuente, destino y auxiliar), respetando las reglas del puzzle: solo se puede mover un disco a la vez, y un disco grande nunca puede estar sobre uno más pequeño.

## Requisitos
- **Python**: Versión 3.13.15
