en la elaboracion de este proyecto utilize métodos y primitivas de sincronización del módulo multiprocessing de Python para garantizar que los procesos concurrentes accedan y modifiquen el estado del tinaco de manera segura, evitando condiciones de carrera y asegurando la consistencia de los datos.

1. Métodos Utilizados
Los métodos que implementé en la clase TinacoContext son los siguientes:

Métodos de Llenado
llenar_desde_pluvial(cantidad): Simula el llenado del tinaco desde la fuente pluvial.

llenar_desde_cisterna(cantidad): Simula el llenado del tinaco desde la cisterna.

Métodos de Consumo
consumir_jardin(cantidad): Simula el consumo de agua para el jardín.

consumir_lavaderos(cantidad): Simula el consumo de agua para los lavaderos.

consumir_banios(cantidad): Simula el consumo de agua para los baños.

Métodos de Control de la Bomba
activar_bomba(): Activa la bomba de presión.

desactivar_bomba(): Desactiva la bomba de presión.

2. Primitivas de Sincronización Utilizadas
Para garantizar que los procesos concurrentes no accedan o modifiquen el estado del tinaco de manera incorrecta, utilicé las siguientes primitivas de sincronización:

a) multiprocessing.Lock
Propósito: Un Lock (o cerrojo) es una primitiva de sincronización que permite que solo un proceso a la vez acceda a un recurso compartido.

Uso en el código:

En cada método que modifica el nivel de agua (llenar_desde_pluvial, llenar_desde_cisterna, consumir_jardin, etc.), utilicé un Lock para garantizar que solo un proceso pueda modificar el nivel de agua a la vez.

Ejemplo:
with self.lock:
    if self.nivel_agua.value + cantidad <= self.capacidad_total:
        self.nivel_agua.value += cantidad

Esto evita que dos procesos intenten modificar el nivel de agua simultáneamente, lo que podría causar inconsistencias.

b) multiprocessing.Event
Propósito: Un Event es una primitiva de sincronización que permite que un proceso notifique a otros procesos sobre un evento o condición.

Uso en el código:

Utilicé un Event para controlar el estado de la bomba de presión (bomba_activa).

Cuando el nivel de agua supera el 25%, se activa la bomba:

python
Copy
if self.nivel_agua.value > 25:
    self.bomba_activa.set()  # Activar bomba
Cuando el nivel de agua es menor o igual al 25%, se desactiva la bomba:

python
Copy
if self.nivel_agua.value <= 25:
    self.bomba_activa.clear()  # Desactivar bomba
Esto garantiza que la bomba solo se active o desactive cuando se cumplan las condiciones específicas.

c) multiprocessing.Manager
Propósito: Un Manager permite crear objetos compartidos entre procesos, como variables, listas o diccionarios.

Uso en el código:

Utilicé un Manager para crear una variable compartida (nivel_agua) que almacena el nivel de agua del tinaco.

Ejemplo:

python
Copy
self.nivel_agua = Manager().Value('i', 0)  # Variable compartida para el nivel de agua
Esto permite que todos los procesos accedan y modifiquen el mismo valor de nivel_agua de manera segura.

3. Métodos de Sincronización
Además de las primitivas, utilicé los siguientes métodos para garantizar la sincronización:

a) with self.lock:
Este bloque garantiza que el código dentro de él se ejecute de manera exclusiva (solo un proceso a la vez).

Ejemplo:

python
Copy
with self.lock:
    if self.nivel_agua.value + cantidad <= self.capacidad_total:
        self.nivel_agua.value += cantidad
b) self.bomba_activa.set() y self.bomba_activa.clear()
Estos métodos activan y desactivan el Event que controla la bomba de presión.

Ejemplo:

python
Copy
self.bomba_activa.set()  # Activar bomba
self.bomba_activa.clear()  # Desactivar bomba
4. Resumen de Primitivas y Métodos
Primitiva/Método	Propósito
multiprocessing.Lock	Garantiza que solo un proceso modifique el nivel de agua a la vez.
multiprocessing.Event	Controla el estado de la bomba de presión (activada/desactivada).
multiprocessing.Manager	Crea variables compartidas entre procesos (como nivel_agua).
with self.lock:	Bloquea el acceso a un recurso compartido mientras se ejecuta un bloque de código.
self.bomba_activa.set()	Activa la bomba de presión.
self.bomba_activa.clear()	Desactiva la bomba de presión.
5. Ejemplo de Sincronización en Acción
Supongamos que dos procesos intentan modificar el nivel de agua al mismo tiempo:

Proceso 1: Intenta llenar el tinaco desde la cisterna.

Proceso 2: Intenta consumir agua para el jardín.

Gracias al Lock, solo uno de los procesos puede modificar el nivel de agua a la vez. Por ejemplo:

El Proceso 1 adquiere el Lock y modifica el nivel de agua.

El Proceso 2 espera hasta que el Lock esté disponible.

Una vez que el Proceso 1 libera el Lock, el Proceso 2 puede adquirirlo y modificar el nivel de agua.

Esto evita que ambos procesos modifiquen el nivel de agua simultáneamente, lo que podría causar inconsistencias.

6. Conclusión
Utilicé Lock para sincronizar el acceso al nivel de agua.

Utilicé Event para controlar la bomba de presión.

Utilicé Manager para compartir el estado del tinaco entre procesos.

Estos métodos y primitivas garantizan que la simulación funcione correctamente en un entorno concurrente.

Métodos Implementados
Métodos de Llenado
llenar_desde_pluvial(cantidad): Simula el llenado del tinaco desde la fuente pluvial.

llenar_desde_cisterna(cantidad): Simula el llenado del tinaco desde la cisterna.

Métodos de Consumo
consumir_jardin(cantidad): Simula el consumo de agua para el jardín.

consumir_lavaderos(cantidad): Simula el consumo de agua para los lavaderos.

consumir_banios(cantidad): Simula el consumo de agua para los baños.

Métodos de Control de la Bomba
activar_bomba(): Activa la bomba de presión.

desactivar_bomba(): Desactiva la bomba de presión.

Ejecución del Proyecto
1. Requisitos
Python 3.x instalado.

No se requieren librerías externas, ya que se utilizan módulos nativos de Python (multiprocessing).

2. Instrucciones de Ejecución
Clona el repositorio o descarga los archivos del proyecto.

Abre una terminal en la carpeta del proyecto.

Ejecuta el archivo principal:

bash
Copy
python main.py
Observa la salida en la consola para ver cómo el nivel de agua cambia en función de los procesos de llenado y consumo.

Ejemplo de Salida
La salida en la consola mostrará mensajes como los siguientes:

Copy
Llenado desde pluvial: 10%, nivel actual: 10%
Llenado desde cisterna: 20%, nivel actual: 30%
Consumo de jardín: 5%, nivel actual: 25%
Bomba desactivada.
Consumo de baños: 7%, nivel actual: 18%
Error: No se puede consumir, nivel de agua bajo para jardín.
Documentación Técnica
Descripción de la Arquitectura
El proceso central es el TinacoContext, que gestiona el estado del tinaco (nivel de agua, bomba, etc.).

Los procesos de fuentes (pluvial, cisterna) y consumos (jardín, lavaderos, baños) se comunican con el TinacoContext para realizar operaciones de llenado y consumo.

Reglas de Llenado y Consumo
Cisterna: Añade agua si el nivel está por debajo del 50%.

Jardín: Consume agua si el nivel no está por debajo del 50% del límite inferior.

Lavaderos: Consume agua si el nivel no está por debajo del 3%.

Baños: Siempre consumen agua, a menos que el tinaco esté vacío.

Posibles Escenarios de Error
Si el tinaco llega al 100% de capacidad, no se puede llenar más.

Si el tinaco llega al 0%, no se puede consumir agua.

Conclusión
Este proyecto demuestra cómo gestionar recursos compartidos en un entorno concurrente utilizando primitivas de sincronización como Lock, Event y Manager. La simulación refleja las restricciones de llenado y consumo, y garantiza la consistencia del estado del tinaco.

Autor
Isai Lopez

Licencia
Este proyecto está bajo la licencia MIT.