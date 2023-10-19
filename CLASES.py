cambio 1

class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

class Personal(Persona):
    def __init__(self, nombre, apellido, rol, dni):
        super().__init__(nombre, apellido, dni)
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol
        self.tareas_asignadas = {}  # Lista de tareas asignadas al empleado

    def asignar_tarea(self, tarea, contraseña):
        if self.nombre not in self.tareas_asignadas:
            self.tareas_asignadas[self.nombre] = {}
            if contraseña not in self.tareas_asignadas[self.nombre]:
                self.tareas_asignadas[self.nombre][contraseña] = tarea
                print("Se ha asignado la tarea correctamente.")
        elif self.nombre in self.tareas_asignadas:
            if contraseña in self.tareas_asignadas[self.nombre]:
                self.tareas_asignadas[self.nombre][contraseña] = tarea
                print("Se ha cambiado la tarea asignada correctamente.")
            else:
                print("La contraseña no existe para el nombre especificado.")
        

    def registrar_ingreso(self):
        pass

    def registrar_egreso(self):
        pass

class Cliente(Persona):
    def _init_(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.reservas = []

    def hacer_reserva(self, reserva):
        self.reservas.append(reserva)

    def calcular_gasto_total(self):
        total_gasto = 0
        for reserva in self.reservas:
            total_gasto += reserva.calcular_costo_total()
        return total_gasto

class Habitacion:
    def _init_(self, numero, tipo, capacidad, precio, tiene_baño_privado, tiene_ventana_balcon):
        self.numero = numero  # Número de la habitación
        self.tipo = tipo  # Tipo de habitación (simple, doble, suite, familiar)
        self.capacidad = capacidad  # Capacidad máxima de ocupación
        self.precio = precio  # Precio por noche
        self.tiene_baño_privado = tiene_baño_privado  # True si tiene baño privado, False en caso contrario
        self.tiene_ventana_balcon = tiene_ventana_balcon  # True si tiene ventana o balcón, False en caso contrario
        self.estado = "Disponible"  # Estado inicial de la habitación (puede ser "Disponible", "Ocupada", "Mantenimiento", etc.)

    def reservar(self):
        # Método para marcar la habitación como ocupada al hacer una reserva
        self.estado = "Ocupada"

    def liberar(self):
        # Método para liberar la habitación cuando un cliente hace check-out
        self.estado = "Disponible"

    def poner_en_mantenimiento(self):
        # Método para marcar la habitación como en mantenimiento
        self.estado = "Mantenimiento"



Santiago = Personal("Santiago", "Hernandez", "Limpieza")
Santiago.asignar_tarea("Fregar pisos", "salchicha")
print(Santiago.tareas_asignadas)
Santiago.asignar_tarea("Cagar", "Ashe")
print(Santiago.tareas_asignadas)
