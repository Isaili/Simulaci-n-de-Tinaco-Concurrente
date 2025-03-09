import time

def proceso_lavaderos(tinaco):
    while True:
        tinaco.consumir_lavaderos(3)  # Consume 3% cada 20 segundos
        time.sleep(20)  # Espera 20 segundos