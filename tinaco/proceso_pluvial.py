import time

def proceso_pluvial(tinaco):
    while True:
        if tinaco.nivel_agua.value < tinaco.capacidad_total:
            tinaco.llenar_desde_pluvial(10)  # Llena 10% cada 5 segundos
        time.sleep(5)  # Espera 5 segundos