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

Autor
Isai Lopez

Licencia
Este proyecto está bajo la licencia MIT.
