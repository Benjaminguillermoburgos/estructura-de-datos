#Clase Supermercado
class Supermercado:
    def __init__(self):
        self.pila_productos_recibidos = []
        self.cola_productos_despachar = []
    #Metodo Agregar Productos
    def agregar_producto(self, producto):
        self.pila_productos_recibidos.append(producto)
    #Mostrar Productos a Despachar
    def despachar_producto(self):
        if self.cola_productos_despachar:
            producto = self.cola_productos_despachar.pop(0)
            print("Producto despachado:", producto)
        else:
            print("No hay productos disponibles para despachar.")
    #Verificar Pila vacia
    def verificar_pila_vacia(self):
        if not self.pila_productos_recibidos:
            print("La pila de productos recibidos está vacía.")
        else:
            print("La pila de productos recibidos no está vacía.")
    #Verificar Cola vacia
    def verificar_cola_vacia(self):
        if not self.cola_productos_despachar:
            print("La cola de productos para despachar está vacía.")
        else:
            print("La cola de productos para despachar no está vacía.")
    #Metodo Imprimir Productos
    def imprimir_productos_recibidos(self):
        print("Lista de productos recibidos:")
        for producto in self.pila_productos_recibidos:
            print(producto)
    #Metodo Imprimir Productos a Despachar
    def imprimir_productos_despachar(self):
        print("Lista de productos para despachar:")
        for producto in self.cola_productos_despachar:
            print(producto)
    #Se muestra la cantidad total de productos 
    def mostrar_cantidad_total_productos(self):
        total_productos = len(self.pila_productos_recibidos) + len(self.cola_productos_despachar)
        print("Cantidad total de productos en el almacén:", total_productos)

# Ejemplo de uso
supermercado = Supermercado()
#Se agragan Productos
supermercado.agregar_producto("Leche")
supermercado.agregar_producto("Mantequilla")
supermercado.agregar_producto("Harina")
#Se verifica si la pila 
supermercado.verificar_pila_vacia()
supermercado.verificar_cola_vacia()
#Se imprime la lista de productos 
supermercado.imprimir_productos_recibidos()
#Se muestra que producto se despachara y se imprime
supermercado.despachar_producto()
supermercado.imprimir_productos_despachar()
#Se muestra cantidad de profuctos a mostrar
supermercado.mostrar_cantidad_total_productos()