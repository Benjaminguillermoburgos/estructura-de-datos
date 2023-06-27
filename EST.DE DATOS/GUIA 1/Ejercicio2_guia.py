# Realizar un algoritmo donde se compruebe la identidad:
# A x A^-1 = I
# I = Matriz identidad
import numpy as np

print("Haga una matriz cuadrada, en este ejemplo, utilize el n° 3")
filas = int(input("Indique el n° de filas que usará: "))
columnas = int(input("Indique el n° de columnas que usará: "))

if not filas == columnas:
    print("No poseen el mismo n°, por ende, su matriz no es cuadrada")
else:
    # Matriz con valores del 1 al 9
    m = np.random.randint(1, 10, size=(filas, columnas))
    print("Matriz:")
    for fila in m:
        print(fila)

    # Inversa Matriz
    mInv = np.linalg.inv(m)

    # Redondeo de inversa a 2 decimales
    mInvRound = np.around(mInv, decimals=2)
    print("\nInversa de la matriz:")
    print(mInvRound)

    # Multiplicacipon de la matriz por su inversa, redondeado
    mfRound = np.around(np.dot(m, mInv), decimals=0)
    print("\nMultiplicacion REDONDEADA de la matriz por su inversa:")
    print(mfRound)

    # Comprobar A x A^-1 = I
    mIde = np.identity(filas)
    if np.allclose(mfRound, mIde):
        print("\nEl resultado es igual a la matriz identidad"
              "\nPor lo tanto se comprueba que A x A^-1 = I, siendo I = Matriz identidad")
    else:
        print("El resultado no es igual a la matriz identidad")
