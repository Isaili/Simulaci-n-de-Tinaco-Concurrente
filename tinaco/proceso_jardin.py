import time

def proceso_jardin(tinaco):
    while True:
        tinaco.consumir_jardin(5)  # Consume 5% cada 15 segundos
        time.sleep(15)  # Espera 15 segundos