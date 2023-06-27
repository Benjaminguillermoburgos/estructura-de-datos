#Se crea un nodo
class Nodo:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.siguiente = None
        self.anterior = None
#Clase Lista de reproducciones
class ListaReproduccion:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    #Se verifica si la lista esta vacia
    def esta_vacia(self):
        return self.primero is None
    #Metodo Agregar Cancion
    def agregar_cancion(self, titulo, artista):
        nueva_cancion = Nodo(titulo, artista)
        if self.esta_vacia():
            self.primero = nueva_cancion
            self.ultimo = nueva_cancion
        else:
            nueva_cancion.anterior = self.ultimo
            self.ultimo.siguiente = nueva_cancion
            self.ultimo = nueva_cancion
    #Metodo de Eliminacion de Cancion
    def eliminar_cancion(self, titulo):
        if self.esta_vacia():
            return
        actual = self.primero
        while actual is not None:
            if actual.titulo == titulo:
                if actual.anterior is None:
                    self.primero = actual.siguiente
                    if self.primero is not None:
                        self.primero.anterior = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    if actual.siguiente is not None:
                        actual.siguiente.anterior = actual.anterior
                    if actual == self.ultimo:
                        self.ultimo = actual.anterior
                break

            actual = actual.siguiente
    #Metodo Mostrar Lista
    def mostrar_lista(self):
        if self.esta_vacia():
            print("La lista de reproducción está vacía.")
            return
        actual = self.primero
        while actual is not None:
            print("Título:", actual.titulo, "Artista:", actual.artista)
            actual = actual.siguiente

print("Ejemplos de uso")
print("Crear una instancia de la lista de reproducción")
lista = ListaReproduccion()

#Agregar canciones a la lista de reproducción
lista.agregar_cancion("Canción 1", "Artista 1")
lista.agregar_cancion("Canción 2", "Artista 2")
lista.agregar_cancion("Canción 3", "Artista 3")

print("Mostrar la lista de reproducción")
lista.mostrar_lista()

print("Eliminar canción de la lista de reproducción")
lista.eliminar_cancion("Canción 2")

print("Mostrar la lista de reproducción después de eliminar una canción")
lista.mostrar_lista()
