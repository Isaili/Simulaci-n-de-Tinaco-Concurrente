from multiprocessing import Process
from tinaco.TinacoContext import TinacoContext
from tinaco.proceso_pluvial import proceso_pluvial
from tinaco.proceso_cisterna import proceso_cisterna
from tinaco.proceso_jardin import proceso_jardin
from tinaco.proceso_lavaderos import proceso_lavaderos
from tinaco.proceso_banios import proceso_banios

if __name__ == "__main__":
    # Crear el tinaco con capacidad total de 100% y límite inferior de 10%
    tinaco = TinacoContext(capacidad_total=100, limite_inferior=10)

    # Crear procesos
    pluvial = Process(target=proceso_pluvial, args=(tinaco,))
    cisterna = Process(target=proceso_cisterna, args=(tinaco,))
    jardin = Process(target=proceso_jardin, args=(tinaco,))
    lavaderos = Process(target=proceso_lavaderos, args=(tinaco,))
    banios = Process(target=proceso_banios, args=(tinaco,))

    # Iniciar procesos
    pluvial.start()
    cisterna.start()
    jardin.start()
    lavaderos.start()
    banios.start()

    # esperar que los procesos terminen
    pluvial.join()
    cisterna.join()
    jardin.join()
    lavaderos.join()
    banios.join()