class Asistencia:
    def __init__(self):
        self.Presentes = []

    def AddEstudiante(self):
        NumEst = int(input("Ingrese el número total de estudiantes a ingresar: "))
        for i in range(NumEst):
            nombre = input("Ingrese el nombre y apellido del estudiante {}: ".format(i + 1)).split(" ")
            self.Presentes.append(nombre)


    def mostrarPresentes(self):
        print("\nLista de estudiantes presentes:")
        print("{:<10} {:<15} {:<15}".format("Número", "Nombre", "Apellido"))
        for i, estudiante in enumerate(self.Presentes):
            print("{:<10} {:<15} {:<15}".format(i + 1, estudiante[0], estudiante[1]))


# Create an object of the class
mi_asistencia = Asistencia()
mi_asistencia.AddEstudiante()
mi_asistencia.mostrarPresentes()
