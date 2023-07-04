class NodoVideo:
    def __init__(self, titulo, autor, duracion):
        self.titulo = titulo
        self.autor = autor
        self.duracion = duracion
        self.siguiente = None


class ListaReproduccion:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_video(self, titulo, autor, duracion):
        nuevo_video = NodoVideo(titulo, autor, duracion)

        if self.primero is None:
            self.primero = nuevo_video
            self.ultimo = nuevo_video
            nuevo_video.siguiente = nuevo_video
        else:
            nuevo_video.siguiente = self.primero
            self.ultimo.siguiente = nuevo_video
            self.ultimo = nuevo_video

    def mostrar_lista(self):
        if self.primero is None:
            print("La lista de videos está vacía.")
            return

        actual = self.primero
        while True:
            print("Título:", actual.titulo)
            print("Autor:", actual.autor)
            print("Duración:", actual.duracion)
            print("------")
            actual = actual.siguiente
            if actual == self.primero:
                break

    def buscar_video(self, titulo):
        if self.primero is None:
            print("La lista de videos está vacía.")
            return

        actual = self.primero
        while True:
            if actual.titulo == titulo:
                print("Título:", actual.titulo)
                print("Autor:", actual.autor)
                print("Duración:", actual.duracion)
                return
            actual = actual.siguiente
            if actual == self.primero:
                break

        print("El video no se encuentra en la lista.")

    def eliminar_video(self, titulo):
        if self.primero is None:
            print("La lista de videos está vacía.")
            return

        actual = self.primero
        anterior = None
        while True:
            if actual.titulo == titulo:
                if anterior is not None:
                    anterior.siguiente = actual.siguiente
                    if actual == self.ultimo:
                        self.ultimo = anterior
                else:
                    self.primero = actual.siguiente
                    if actual == self.ultimo:
                        self.ultimo = None
                del actual
                print("El video se ha eliminado.")
                return

            anterior = actual
            actual = actual.siguiente
            if actual == self.primero:
                break

        print("El video no se encuentra en la lista.")

    def esta_vacia(self):
        return self.primero is None


# Ejemplo de uso:
lista = ListaReproduccion()

# Agregar videos
lista.agregar_video("Video 1", "Autor 1", "10:00")
lista.agregar_video("Video 2", "Autor 2", "5:30")
lista.agregar_video("Video 3", "Autor 3", "8:45")

# Mostrar lista de videos
print("Lista de videos:")
lista.mostrar_lista()
print()

# Buscar video
print("Buscar video:")
lista.buscar_video("Video 2")
print()

# Eliminar video
print("Eliminar video:")
lista.eliminar_video("Video 2")
print()

# Verificar si la lista está vacía
if lista.esta_vacia():
    print("La lista de videos está vacía.")
else:
    print("La lista de videos no está vacía.")
