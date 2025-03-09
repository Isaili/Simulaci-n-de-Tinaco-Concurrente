from multiprocessing import Manager, Lock, Event

class TinacoContext:
    def __init__(self, capacidad_total, limite_inferior):
        self.capacidad_total = capacidad_total
        self.limite_inferior = limite_inferior
        self.nivel_agua = Manager().Value('i', 0)  # Nivel de agua como valor compartido
        self.lock = Lock()  # Para sincronizar el acceso al nivel de agua
        self.bomba_activa = Event()  # Para controlar la bomba de presión

    def llenar_desde_pluvial(self, cantidad):
        with self.lock:
            if self.nivel_agua.value + cantidad <= self.capacidad_total:
                self.nivel_agua.value += cantidad
                print(f"Llenado desde pluvial: {cantidad}%, nivel actual: {self.nivel_agua.value}%")
                if self.nivel_agua.value > 25:
                    self.bomba_activa.set()  # Activar bomba si el nivel supera el 25%
                return True
            else:
                print("Error: No se puede llenar, capacidad excedida.")
                return False

    def llenar_desde_cisterna(self, cantidad):
        with self.lock:
            if self.nivel_agua.value + cantidad <= self.capacidad_total:
                self.nivel_agua.value += cantidad
                print(f"Llenado desde cisterna: {cantidad}%, nivel actual: {self.nivel_agua.value}%")
                if self.nivel_agua.value > 25:
                    self.bomba_activa.set()  # Activar bomba si el nivel supera el 25%
                return True
            else:
                print("Error: No se puede llenar, capacidad excedida.")
                return False

    def consumir_jardin(self, cantidad):
        with self.lock:
            if self.nivel_agua.value >= self.limite_inferior * 0.5:  # Solo consume si el nivel es >= 50% del límite inferior
                self.nivel_agua.value -= cantidad
                print(f"Consumo de jardín: {cantidad}%, nivel actual: {self.nivel_agua.value}%")
                if self.nivel_agua.value <= 25:
                    self.bomba_activa.clear()  # Desactivar bomba si el nivel es <= 25%
                return True
            else:
                print("Error: No se puede consumir, nivel de agua bajo para jardín.")
                return False

    def consumir_lavaderos(self, cantidad):
        with self.lock:
            if self.nivel_agua.value >= self.limite_inferior * 0.03:  # Solo consume si el nivel es >= 3% del límite inferior
                self.nivel_agua.value -= cantidad
                print(f"Consumo de lavaderos: {cantidad}%, nivel actual: {self.nivel_agua.value}%")
                if self.nivel_agua.value <= 25:
                    self.bomba_activa.clear()  # Desactivar bomba si el nivel es <= 25%
                return True
            else:
                print("Error: No se puede consumir, nivel de agua bajo para lavaderos.")
                return False

    def consumir_banios(self, cantidad):
        with self.lock:
            if self.nivel_agua.value > 0:  # Siempre consume, a menos que el tinaco esté vacío
                self.nivel_agua.value -= cantidad
                print(f"Consumo de baños: {cantidad}%, nivel actual: {self.nivel_agua.value}%")
                if self.nivel_agua.value <= 25:
                    self.bomba_activa.clear()  # Desactivar bomba si el nivel es <= 25%
                return True
            else:
                print("Error: No se puede consumir, tinaco vacío.")
                return False

    def activar_bomba(self):
        self.bomba_activa.set()
        print("Bomba activada.")

    def desactivar_bomba(self):
        self.bomba_activa.clear()
        print("Bomba desactivada.")