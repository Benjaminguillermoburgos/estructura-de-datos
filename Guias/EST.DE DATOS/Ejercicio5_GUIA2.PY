#clase empleado
class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.subordinados = []
    #Metodo agregar
    def agregar_subordinado(self, subordinado):
        self.subordinados.append(subordinado)
    #Metodo eliminar
    def eliminar_subordinado(self, subordinado):
        self.subordinados.remove(subordinado)
    #Metodo obtener
    def obtener_subordinados(self):
        return self.subordinados

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"

#Clase Empresa
class Empresa:
    def __init__(self):
        self.raiz = None
    #Metodo agregar empleado
    def agregar_empleado(self, nombre, cargo, jefe_nombre):
        empleado = Empleado(nombre, cargo)

        if not self.raiz:
            self.raiz = empleado
        else:
            jefe = self.buscar_empleado(jefe_nombre)
            if jefe:
                jefe.agregar_subordinado(empleado)
            else:
                print(f"No se encontró al empleado {jefe_nombre}")
    #Metodo eliminar empleado
    def eliminar_empleado(self, nombre):
        empleado = self.buscar_empleado(nombre)
        if empleado:
            jefe = self.buscar_jefe_directo(nombre)
            subordinados = empleado.obtener_subordinados()

            if jefe:
                jefe.subordinados.extend(subordinados)
                jefe.subordinados.remove(empleado)
            else:
                self.raiz = None if empleado == self.raiz else self.raiz
    #Metodo Mostrar Jerarquia
    def mostrar_jerarquia(self):
        if self.raiz:
            self.mostrar_empleado(self.raiz, 0)
        else:
            print("No hay empleados en la empresa.")
    #Metodo Mostrar empleados
    def mostrar_empleado(self, empleado, nivel):
        print("\t" * nivel + str(empleado))
        subordinados = empleado.obtener_subordinados()
        for subordinado in subordinados:
            self.mostrar_empleado(subordinado, nivel + 1)
    #Metodos de busqueda de empleados
    def buscar_empleado(self, nombre):
        return self.buscar_empleado_recursivo(self.raiz, nombre)
    def buscar_empleado_recursivo(self, empleado, nombre):
        if empleado.nombre == nombre:
            return empleado
        for subordinado in empleado.obtener_subordinados():
            encontrado = self.buscar_empleado_recursivo(subordinado, nombre)
            if encontrado:
                return encontrado
        return None
    #Metodos de busqueda del jefe
    def buscar_jefe_directo(self, nombre):
        return self.buscar_jefe_directo_recursivo(self.raiz, nombre)
    def buscar_jefe_directo_recursivo(self, empleado, nombre):
        for subordinado in empleado.obtener_subordinados():
            if subordinado.nombre == nombre:
                return empleado
            encontrado = self.buscar_jefe_directo_recursivo(subordinado, nombre)
            if encontrado:
                return encontrado
        return None
# Ejemplo de uso
#Se crea Un objeto con la clase empresa, Se agrega un Jefe y cada empleado con su jerarquia en la empresa
empresa = Empresa()
empresa.agregar_empleado("Eduardo", "CEO", "")
empresa.agregar_empleado("Alex", "Gerente", "Eduardo")
empresa.agregar_empleado("Benjamin", "Supervisor", "Alex")
empresa.agregar_empleado("Cristofer", "Analista", "Benjamin")
empresa.agregar_empleado("Sebastian", "Analista", "Bob")
#Se muestra los datos agregados con su respectiva jerarquia
empresa.mostrar_jerarquia()

print("--------------------")
#Se despide al empleado alex y luego se vuelven a mostrar los datos con su jerarquia
empresa.eliminar_empleado("Alex")
empresa.mostrar_jerarquia()

print("--------------------")
#Se busca al empleado crsitofer para mostrar que cargo tiene
empleado_buscar = empresa.buscar_empleado("Cristofer")
#Se recorre la lista para encontrar el cargo y mostrar a su subordinado, si no lo tiene se menciona que no contiene 
if empleado_buscar:
    print(f"Cargo de {empleado_buscar.nombre}: {empleado_buscar.cargo}")
    subordinados = empleado_buscar.obtener_subordinados()
    if subordinados:
        print("Subordinados:")
        for subordinado in subordinados:
            print(f"\t{subordinado.nombre} - {subordinado.cargo}")
    else:
        print("No tiene subordinados.")

print("--------------------")
#Se muestra a un empleado y se da a entender cual es su superior
empleado_jefe = "Cristofer"
jefe_directo = empresa.buscar_jefe_directo(empleado_jefe)
if jefe_directo:
    print(f"Jefe directo de {empleado_jefe}: {jefe_directo.nombre} - {jefe_directo.cargo}")
else:
    print(f"No se encontró el jefe directo de {empleado_jefe}.")
