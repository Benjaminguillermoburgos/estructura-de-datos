#Aplicar el metodo de Gauss para invertir una matriz aleatoria de 3 a 5 de dimensión sin
#utilizar librerias (excepto el uso de la libreria Random). Imprimir la matriz original y luego
#la matriz inversa. Recordar que si una matriz A es una matriz cuadrada no-singular, es
#decir, tal que su determinante es distinto de cero se puede utilizar el Metodo de Eliminacion Gaussiana.
#El calculo de la inversa se realiza ampliando la matriz A adosando la
#matriz identidad a su lado derecho, como se muestra a continuacion: 
import random

def crear_matriz(dim):
    matriz = []
    for i in range(dim):
        fila = []
        for j in range(dim):
            fila.append(random.randint(1, 9))
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def intercambiar_filas(matriz, fila1, fila2):
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]

def multiplicar_fila(matriz, fila, escalar):
    for i in range(len(matriz[fila])):
        matriz[fila][i] *= escalar

def sumar_filas(matriz, fila_destino, fila_origen, factor):
    for i in range(len(matriz[fila_destino])):
        matriz[fila_destino][i] += factor * matriz[fila_origen][i]

def matriz_identidad(dim):
    matriz = []
    for i in range(dim):
        fila = []
        for j in range(dim):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

def invertir_matriz(matriz):
    dim = len(matriz)
    identidad = matriz_identidad(dim)
    for i in range(dim):
        # Pivoteo parcial: buscar el mayor elemento en la columna
        max_value = abs(matriz[i][i])
        max_row = i
        for j in range(i + 1, dim):
            if abs(matriz[j][i]) > max_value:
                max_value = abs(matriz[j][i])
                max_row = j
        # Intercambiar filas si es necesario
        if max_row != i:
            intercambiar_filas(matriz, i, max_row)
            intercambiar_filas(identidad, i, max_row)
        # Hacer ceros debajo del pivote
        for j in range(i + 1, dim):
            factor = -matriz[j][i] / matriz[i][i]
            sumar_filas(matriz, j, i, factor)
            sumar_filas(identidad, j, i, factor)
    # Hacer unos en la diagonal principal
    for i in range(dim):
        escalar = 1 / matriz[i][i]
        multiplicar_fila(matriz, i, escalar)
        multiplicar_fila(identidad, i, escalar)
    return identidad

# Generar una matriz aleatoria de dimensiones 3 a 5
dimension = random.randint(3, 5)
matriz_original = crear_matriz(dimension)

# Imprimir la matriz original
print("Matriz original:")
imprimir_matriz(matriz_original)

# Invertir la matriz utilizando el método de Gauss
matriz_inversa = invertir_matriz(matriz_original)

# Imprimir la matriz inversa
print("Matriz inversa:")
imprimir_matriz(matriz_inversa)
