#Clase CLiente
class Cliente:
    def __init__(self, ticket, caja):
        self.ticket = ticket
        self.caja = caja
#Clase Cola
class FilaAtencion:
    def __init__(self):
        self.cola = []
        self.caja_actual = 0
    #Metodo Agregar Cliente
    def agregar_cliente(self, ticket):
        caja = self.obtener_siguiente_caja()
        cliente = Cliente(ticket, caja)
        self.cola.append(cliente)
    #Metodo de Caja Siguiente
    def obtener_siguiente_caja(self):
        self.caja_actual = (self.caja_actual + 1) % 3
        return self.caja_actual + 1
    #Se Atiende al Cliente
    def atender_cliente(self):
        if len(self.cola) > 0:
            cliente = self.cola.pop(0)
            print("Atendiendo cliente con ticket {} en la caja {}".format(cliente.ticket, cliente.caja))
        else:
            print("No hay clientes en la cola.")

print("Ejemplo de uso")
print("Se genera una cola de atencion")
cola = FilaAtencion()
print("Son 3 clientes los que estan en la cola")
cola.agregar_cliente(1)
cola.agregar_cliente(2)
cola.agregar_cliente(3)
print("Atiende al 1er cliente")
cola.atender_cliente() 
print("Atiende al 2do cliente" )
cola.atender_cliente()
print("Atiende al 3er cliente" )
cola.atender_cliente()
print("No hay más clientes en la cola")  
cola.atender_cliente()  
