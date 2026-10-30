# Prácticas de NumPy con Python
import numpy as np

# 1. Crear matriz de 3x3 ordenada del 0 al 8
arreglo_ordenado = np.arange(9).reshape(3, 3)
print("--- Matriz Original ---")
print(arreglo_ordenado)

# 2. Slicing: Fila 1 completa desde la columna 1 en adelante
print("\n--- Recorte 1: arreglo_ordenado[1, 1:] ---")
print(arreglo_ordenado[1, 1:])

print("-" * 28)

# 3. Slicing: Desde la fila 1 hasta el final, y hasta antes de la columna 2
print("\n--- Recorte 2: arreglo_ordenado[1:, :2] ---")
print(arreglo_ordenado[1:, :2])

print("-" * 28)

# 4. Slicing: Desde la fila 1 hasta el final, y desde la columna 1 hasta el final
print("\n--- Recorte 3: arreglo_ordenado[1:, 1:] ---")
print(arreglo_ordenado[1:, 1:])

print("-" * 28)
