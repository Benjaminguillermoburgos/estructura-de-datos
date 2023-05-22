# Realizar un algoritmo donde se compruebe la identidad:
# A x A^-1 = I
# I = Matriz identidad
import sympy as sp
import random

print("Haga una matriz cuadrada, en este ejemplo, utilize el n° 3")
filas = int(input("Indique el n° de filas que usará: "))
columnas = int(input("Indique el n° de columnas que usará: "))

if not filas == columnas:
    print("No poseen el mismo n°, por ende, su matriz no es cuadrada")
else:
    def Matrizz(filas, columnas):
        m = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                elmnt = random.randint(1, 5)
                fila.append(elmnt)
            m.append(fila)
        return m


    def mulMatr(m, mInv):
        mf = []
        for i in range(len(m)):
            fila = []
            for j in range(len(mInv[0])):
                mult = m[i][j] * mInv[i][j]
                fila.append(mult)
            mf.append(fila)
        return mf

matriz_I = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
m = Matrizz(filas, columnas)
mInv = 2
#mf = mulMatr(m,mInv)
print("La matriz original es: ")
#print(m)
print("La matriz inversa es: ")
#print(mInv)
print("\nLa multiplicación da como resultado: ")
#print(mf)