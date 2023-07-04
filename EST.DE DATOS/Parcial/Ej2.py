class Tarea:
    def __init__(self, identificador, titulo, descripcion, estado):
        self.identificador = identificador
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

class SistemaGestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, identificador, titulo, descripcion, estado):
        tarea = Tarea(identificador, titulo, descripcion, estado)
        self.tareas.append(tarea)

    def eliminar_tarea(self, identificador):
        for tarea in self.tareas:
            if tarea.identificador == identificador:
                self.tareas.remove(tarea)
                break

    def buscar_tarea(self, identificador):
        for tarea in self.tareas:
            if tarea.identificador == identificador:
                return tarea
        return None

    def cambiar_estado_tarea(self, identificador, nuevo_estado):
        tarea = self.buscar_tarea(identificador)
        if tarea:
            tarea.estado = nuevo_estado

    def mostrar_tareas_ordenadas(self):
        tareas_ordenadas = sorted(self.tareas, key=lambda tarea: tarea.identificador)
        for tarea in tareas_ordenadas:
            print(f"ID: {tarea.identificador}, Título: {tarea.titulo}, Descripción: {tarea.descripcion}, Estado: {tarea.estado}")


# Ejemplo de uso
sistema = SistemaGestionTareas()

sistema.agregar_tarea(1, "Tarea 1", "Calcular la derivada de 3 ejercicios", "pendiente")
sistema.agregar_tarea(3, "Tarea 3", "Calcula integral de lo siguientes", "en progreso")
sistema.agregar_tarea(2, "Tarea 2", "Sacar el nucleo y la dimension del nucleo de T", "completada")

sistema.mostrar_tareas_ordenadas()  # Mostrar las tareas en orden ascendente por identificador

tarea = sistema.buscar_tarea(2)  # Buscar una tarea específica
if tarea:
    print(f"Tarea encontrada: {tarea.titulo}")
else:
    print("Tarea no encontrada")

sistema.cambiar_estado_tarea(3, "completada")  # Cambiar el estado de una tarea

sistema.mostrar_tareas_ordenadas()  # Mostrar las tareas actualizadas
