from Camara import Camara
# Sesion: Representa a la grabacion de una clase. Los atributos son:
# id, nombre asignatura, nombre profesor, sala, fecha de la clase, hora inicio, hora fin, cámara en uso y lista de camaras.
# Tiene el método de iniciarTransmision, terminarTransmision y cambiarCamara,
# lo que permite utilizar la cámara del siguiente dispositivo en la lista de camaras.

class Sesion:
    def __init__(self, idSes, NomAs, NomProf, sala, FeClase, HIni, HFin):
        self.idSes = idSes
        self.NomAs = NomAs
        self.NomPro = NomProf
        self.sala = sala
        self.FeClase = FeClase
        self.HIni = HIni
        self.HFin = HFin
        self.CamInUse = None
        self.CamList = []

    def agregarCam(self, camara):
        self.CamList.append(camara)

    def cambiarCamara(self, indice):
        if indice < len(self.CamList):
            self.CamInUse = self.CamList[indice]
            print(f"Cambiando a la cámara {self.CamInUse.nombre}")
        else:
            print("Índice de cámara inválido")

    def agregar_camara(self, camara):
        self.CamList.append(camara)

    def crearCam(self):
        idcam = input("Ingrese el ID de la cámara: ")
        nombre = input("Ingrese el nombre de la cámara: ")
        resolucion = input("Ingrese la resolución de la cámara: ")
        camara = Camara(idcam, nombre, resolucion)
        self.agregar_camara(camara)

    def verCamList(self):
        print("\nLista de cámaras:")
        for i, camara in enumerate(self.CamList):
            print(f"Indice: {i} \tId: {camara.idCam} \tNombre: {camara.nombre} ({camara.resolucion})")

    def iniciarTransmision(self):
        if self.CamInUse is not None:
            print(self.CamInUse.transmitir())

    def cambiar_camara(self, indice):
        if indice < len(self.CamList):
            self.CamInUse = self.CamList[indice]
            print(f"Cambiando a la cámara {self.CamInUse.nombre}")
        else:
            print("Índice de cámara inválido")

    def terminarTransmision(self):
        print("Transmisión finalizada")
