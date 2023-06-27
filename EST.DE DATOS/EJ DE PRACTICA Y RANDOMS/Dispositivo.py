from Camara import Camara
# Dispositivo: Representa a cada dispositivo con cámara que se utilizarán.
# Esta clase hereda de Cámara.
# Los atributos de esta clase son: marca y modelo

class 

Dispositivo(Camara):
    def __init__(self, idCam, nombre, resolucion, marca, modelo):
        super().__init__(idCam, nombre, resolucion)
        self.marca = str(marca)
        self.modelo = str(modelo)

c1 = Camara(5645, "vista aerea", "1900x720")
p1 = Dispositivo(5645, "vista aerea", "1900x720", "lenovo", "legion 5 15ach6")
print(p1.transmitir())