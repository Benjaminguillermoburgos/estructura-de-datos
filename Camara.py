from abc import ABC, abstractmethod
# Camara: Corresponde a una clase que tendrá el método transmitir, que permite que la cámara realice la clase.
# Los atributos de esta clase son: id, nombre y resolución.

class Camara:

    def __init__(self,idCam, nombre, resolucion):
        self.idCam = idCam
        self.nombre = nombre
        self.resolucion = resolucion
    @abstractmethod
    def transmitir(self):
        return 'La cámara "'+str(self.nombre)+'" comenzó a transmitir'