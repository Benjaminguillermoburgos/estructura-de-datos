import networkx as nx
import random

# Crear el laberinto
laberinto = nx.Graph()
laberinto.add_nodes_from([(i, j) for i in range(5) for j in range(5)])
for i in range(5):
    for j in range(5):
        if i < 4:
            laberinto.add_edge((i, j), (i + 1, j))
        if j < 4:
            laberinto.add_edge((i, j), (i, j + 1))

# Eliminar aristas aleatoriamente para crear un laberinto
num_aristas_eliminar = random.randint(10, 20)
for _ in range(num_aristas_eliminar):
    arista = random.choice(list(laberinto.edges()))
    laberinto.remove_edge(*arista)

# Función para crear el mapa
def crear_mapa(pos_jugador=None):
    mapa = []
    for i in range(5):
        fila = []
        for j in range(5):
            if pos_jugador == (i, j):
                fila.append("P")  # Representa la posición del jugador
            elif (i, j) in laberinto.edges():
                fila.append(" ")  # Representa los pasillos
            else:
                fila.append("#")  # Representa las paredes
        mapa.append(fila)
    
    return mapa

# Mostrar el mapa
mapa = crear_mapa()
for fila in mapa:
    print(" ".join(fila))
