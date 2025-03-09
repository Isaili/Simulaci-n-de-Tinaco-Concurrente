# 🌌 Simulación de Tinaco Concurrente

## 🖍 Descripción
Este proyecto simula el manejo concurrente de un tinaco que recibe agua de dos fuentes (pluvial y cisterna) y suministra agua para tres usos (jardín, lavaderos, baños). Se utiliza el módulo multiprocessing de Python para gestionar los procesos y la sincronización.

## ✨ Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- 🌫**main.py**: Punto de entrada. Inicia el tinaco y los procesos.
- ⛈**tinaco_context.py**: Contiene la clase TinacoContext que gestiona el estado del tinaco.
- 💧**proceso_pluvial.py**: Simula el llenado desde la fuente pluvial.
- 🎊**proceso_cisterna.py**: Simula el llenado desde la cisterna.
- 🎍**proceso_jardin.py**: Simula el consumo de agua para el jardín.
- 🎎**proceso_lavaderos.py**: Simula el consumo de agua para los lavaderos.
- 🧨**proceso_banios.py**: Simula el consumo de agua para los baños.

---
## 🏛️ Arquitectura
**Procesos**
- 1 **Tinaco**:(Proceso Central):
  - Mantiene el estado compartido del tinaco ** (nivel_agua).**
  - Controla los límites superior e inferior del tinaco.
  - Expone métodos para llenar y consumir agua.

- 2 **Fuentes de Agua:**
  - **Pluvial:** Llena el tinaco cuando se simula lluvia.
  - **Cisterna:**  Llena el tinaco cuando el nivel está por debajo de un mínimo.

- 3 **Consumos de Agua:**
  - **Jardín:** Consume agua si el nivel no está por debajo del 50%.
  - **Lavaderos:** Consume agua si el nivel no está por debajo del 3%.
  - **Baños:** Siempre consume agua, a menos que el tinaco esté vacío.
 
- 4 **Bomba de Presión:**
  - Se activa cuando el nivel de agua supera el 25%.
  - Se desactiva cuando el nivel es menor o igual al 25%.
---

### 📜 Métodos Expuestos
  - **llenar_desde_pluvial(cantidad):**  Llena el tinaco desde la fuente pluvial.
  - **llenar_desde_cisterna(cantidad):** Llena el tinaco desde la cisterna.
  - **consumir_jardin(cantidad):** Consume agua para el jardín.
  - **consumir_lavaderos(cantidad):** Consume agua para los lavaderos.
  - **consumir_banios(cantidad):** Consume agua para los baños.
  - **activar_bomba():** Activa la bomba de presión.
  - **desactivar_bomba():** Desactiva la bomba de presión.

#### 🔒 Primitivas de Sincronización
1. **multiprocessing.Lock**:
   - **Propósito:** Un **Lock** (o cerrojo) es una primitiva de sincronización que permite que solo un proceso a la vez acceda a un recurso compartido.

2. **multiprocessing.Event)**:
  - **Propósito:** Un **Event** es una primitiva de sincronización que permite que un proceso notifique a otros procesos sobre un evento o condición.
    
3. **multiprocessing.Manager**:
  -  **Propósito:** Un **Manager** permite crear objetos compartidos entre procesos, como variables, listas o diccionarios.
  
---
## 🗂️ Estructura del Proyecto


tinaco2/
  ├── 📁 tinaco   # Punto de entrada
    ├── 📁 __pycache__   # cache de los archivos
    ├── 🗍 main.py   # Lógica de concurrencia
    ├── 🗍 proceso_banios.py    # Scripts de fuentes y consumos
    ├── 🗍 proceso_cisterna.py    # Scripts de fuentes y consumos        
    ├── 🗍 proceso_jardin.py    # Scripts de fuentes y consumos
    ├── 🗍 proceso_lavaderos.py    # Scripts de fuentes y consumos
    ├── 🗍 proceso_pluvial.py   # Scripts de fuentes y consumos
    ├── 🗍 TinacoContext.py   #Gestion del tinaco
  ├── 🗍 README.md    # Documentación

---

## 🚀 Instalación y Ejecución

### 1⃣ Clonar el repositorio
```bash
git clone https://github.com/Isaili/Simulaci-n-de-Tinaco-Concurrente.git
```

### 2⃣ Ejecutar la aplicación
```bash
python main.py
```
---
## 📌 Restricciones y Manejo de Errores
  **Restricciones de Llenado**
  - 1 **Pluvial y Cisterna**: No pueden llenar el tinaco si superan la capacidad total (100%).
  - Si se intenta llenar más allá del límite, se muestra un mensaje de error:
  ```bash
Error: No se puede llenar, capacidad excedida.
```


---

Autor
Isai Lopez

Licencia
Este proyecto está bajo la licencia MIT.
