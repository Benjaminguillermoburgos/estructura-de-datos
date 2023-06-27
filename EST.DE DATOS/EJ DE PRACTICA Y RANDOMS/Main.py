from Sesion import Sesion

class Main:
    def __init__(self):
        self.sesion = None

    def crearSesion(self):
        self.sesion = Sesion(input("Ingrese el ID de la sesión: "),
                             input("Ingrese el nombre de la asignatura: "),
                             input("Ingrese el nombre del profesor: "),
                             input("Ingrese el nombre de la sala: "),
                             input("Ingrese la fecha de la clase (en formato AAAA-MM-DD): "),
                             input("Ingrese la hora de inicio de la clase (en formato HH:MM): "),
                             input("Ingrese la hora de fin de la clase (en formato HH:MM): "))
        print(f"Sesión creada con ID {self.sesion.idSes}")

    def crearCam(self):
        self.sesion.crearCam()

    def cambiarCamara(self):
        indice = int(input("\nIngrese el índice de la cámara a la que desea cambiar: "))
        self.sesion.cambiarCamara(indice)

    def ejecutar(self):
        opcion = input("\n¿Desea crear una sesión? (s/n): ")
        if opcion == "s":
            self.crearSesion()
        while True:
            opcion = input("\nIngrese 'c' para crear una cámara, 's' para cambiar de cámara o 'salir' para terminar: ")
            if opcion == "c":
                self.crearCam()
            elif opcion == "s":
                self.sesion.verCamList()
                self.cambiarCamara()
            elif opcion == "salir":
                break


main = Main()
main.ejecutar()