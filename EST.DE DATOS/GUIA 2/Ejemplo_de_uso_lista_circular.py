class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero = nuevo_nodo
            self.ultimo.siguiente = self.primero

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero
            self.ultimo = nuevo_nodo

    def eliminar_inicio(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        if self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

    def eliminar_final(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        if self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
        else:
            actual = self.primero
            while actual.siguiente != self.ultimo:
                actual = actual.siguiente
            actual.siguiente = self.primero
            self.ultimo = actual

    def mostrar_lista(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        actual = self.primero
        while actual.siguiente != self.primero:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print(actual.dato, end=" -> ")
        print("Inicio")


# Ejemplo de uso
lista = ListaCircular()

lista.insertar_final(1)
lista.insertar_final(2)
lista.insertar_final(3)
lista.insertar_final(4)

lista.mostrar_lista()  # Salida: 1 -> 2 -> 3 -> 4 -> Inicio

lista.eliminar_inicio()
lista.eliminar_final()

lista.mostrar_lista()  # Salida: 2 -> 3 -> Inicio
