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
# operadores basicos
import numpy as np

# Creamos dos arreglos (matrices unidimensionales) para probar
a = np.array([2, 4, 6])
b = np.array([1, 2, 3])

print("--- Arreglos originales ---")
print("a =", a)
print("b =", b)

# 1. Suma
print("\n1. Suma (a + b):")
print(a + b)

# 2. Resta
print("\n2. Resta (a - b):")
print(a - b)

# 3. Multiplicación elemento por elemento
print("\n3. Multiplicación (a * b):")
print(a * b)

# 4. División
print("\n4. División (a / b):")
print(a / b)
# operaciones vectoriales
import numpy as np

# Imagina que u y v son dos vectores (por ejemplo, fuerzas o desplazamientos)
u = np.array([3, 4])
v = np.array([1, 2])

print("--- Vectores originales ---")
print("u =", u)
print("v =", v)

# 1. Combinación lineal (multiplicar por escalares y sumar: 2*u + 3*v)
resultado_lineal = 2 * u + 3 * v
print("\n1. Combinación lineal (2u + 3v):", resultado_lineal)

# 2. Producto punto (Dot Product) - muy usado en física para trabajo y ángulos
producto_punto = np.dot(u, v)  # También puedes usar u @ v
print("\n2. Producto punto (u • v):", producto_punto)

# 3. Magnitud o Norma de un vector (longitud geométrica)
norma_u = np.linalg.norm(u)
print("\n3. Longitud (norma) del vector u:", norma_u)

# 5. Potencia (cada elemento elevado al cuadrado)
print("\n5. Potencia (a ** 2):")
print(a ** 2)
