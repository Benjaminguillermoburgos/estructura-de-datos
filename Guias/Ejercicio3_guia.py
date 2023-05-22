#Obtener la determinante de una matriz de 3 x 3 con sus elementos aleatorios. Se puede
#utilizar librerías para resolver el algoritmo.

import numpy as np

# Generar una matriz de 3x3 con elementos aleatorios
matriz = np.random.randint(1, 10, (3, 3))
print("Matriz:")
print(matriz)

# Calcular la determinante de la matriz
determinante = np.linalg.det(matriz)
print("Determinante:", determinante)