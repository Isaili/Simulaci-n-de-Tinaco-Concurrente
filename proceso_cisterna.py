import time

def proceso_cisterna(tinaco):
    while True:
        if tinaco.nivel_agua.value < 50:  # Llena si el nivel es menor al 50%
            tinaco.llenar_desde_cisterna(20)  # Llena 20% cada 10 segundos
        time.sleep(10)  # Espera 10 segundos