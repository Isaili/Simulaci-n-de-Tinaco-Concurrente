import time

def proceso_banios(tinaco):
    while True:
        tinaco.consumir_banios(7)  # Consume 7% cada 25 segundos
        time.sleep(25)  # Espera 25 segundos