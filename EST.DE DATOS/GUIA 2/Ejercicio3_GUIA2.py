import math

class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None



class ListaEnlazada():
    def __init__(self):
        self.first = None
        self.largo = 0
        self.total = 0

    def siguiente(self, dato):
        Nuevo_Nodo = Nodo(dato)
        if self.largo == 0:  #lo que le digo es que si el primer valor de la lista no es nada que el primer valor lo tome el nuevo 
            self.first = Nuevo_Nodo #valor ingresado
        
        else:
            current = self.first  #Current = actual o el dato actual que se encuentra 
            while current.siguiente != None: #un bucle que termine en cuanto el nodo siguiente sea None
                current = current.siguiente
            current.siguiente = Nuevo_Nodo

        self.largo += 1
        self.total += dato

    def remove(self, dato):
        if self.largo == 0:
            return False
        else:
            current = self.first
            try:
                while current.next.dato != dato: #Que recorra hasta que encuente el valor que se pide remover
                    if current.next == None:
                        return False
                    else:
                        current = current.next
                DeletedNone = current.next
                current.next = DeletedNone.next
            except AttributeError:
                return False

        self.largo -=1
        return DeletedNone
    

    def __len__(self):#Tamaño de la lista
        return self.largo
    

    def __str__(self):
        String = "["
        current = self.first
        for i in range(len(self)):
            String += str(current.dato)
            if i != len(self) - 1:
                String += str(", ")
            current = current.siguiente
        String += "]"

        return String

    def promedio(self):
        if self.largo == 0:
            return print("No se puede ejecutar el programa ya que no se ha ingresado ningun dato")
        else:
            media = self.total / self.largo
            return media


    def DesviacionEstandar(self):
        if self.largo == 0:
            print("No se puede ejecutar el programa")
        
        else:
            media = self.total / self.largo
            current = self.first
            suma = 0
            while current != None:
                suma += ((current.dato - media)** 2)
                current = current.siguiente
            
            Desviacion = suma / (self.largo - 1)
            DV = math.sqrt(Desviacion)
            return print(f"\nLa Desviacion Estandar de los datos ingresados es:\n {DV}")
        #se obtiene la media y a cada dato se le resta la media o promedio luego se eleva
        #al cuadrado y se divide por la cantidad de datos - 1
    def vacia(self):
        if self.largo == 0:
            return True
        else:
            return False

print("Elija la opcion a ejecutar:")
lista_Datos = ListaEnlazada()

i = False
h = False
while i != True:
    opcion = int(input("\n1.-Agregar datos\n2.-Calcular Media a los datos ingresados\n3.-Calcular Desviacion Estandar\n4.-Imprimir datos Ingresados\n5.-Verificar si no a ingresado ningun dato\n6.-Salir del programa\n"))
    if 1 <= opcion <= 6:
        if opcion == 1:
            indicador = False
            while indicador != True:
                dato = float(input("\nIngrese dato (Numero Real): "))
                lista_Datos.siguiente(dato)
                for j in range( True):
                    decision = int(input("\n¿Desea ingresar otro dato?\nIngrese 1 en caso de si quiere ingresar otro valor y 2 en caso contrario: "))
                    if decision == 1:
                        indicador = False
                        j = True
                    elif decision == 2:
                        indicador = True
                        j = True
                    else:
                        while h != True:
                            nueva_opcion = int(input("\nOpcion ingresada no valida, ingrese 1 o 2: "))
                            if nueva_opcion == 1 or nueva_opcion == 2:
                                if nueva_opcion == 1:
                                    indicador = False
                                    j = True
                                else:
                                    indicador = True
                                    j = True
                                h = True
                            else:
                                print("\nOpcion no valida")
                                h = False
                            
            i = False
        elif opcion == 2:
            media = lista_Datos.promedio()
            print(f"\nLa media de los datos ingresados es: {media}")
            i = False
        elif opcion == 3:
            lista_Datos.DesviacionEstandar()
            i = False
        elif opcion == 4:
            print("\nLos datos almacenados en la lista son los siguientes:")
            print(lista_Datos)
            i = False
        elif opcion == 5:
            print(f"\nEsta vacia la lista: {lista_Datos.vacia()}")
            i = False
        elif opcion == 6:
            print("Adios")
            i = True
    else:
        print("\nOpcion no valida, Ingrese nuevamente su eleccion: \n")
