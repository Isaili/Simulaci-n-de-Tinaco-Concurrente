# 🌌 Simulación de Tinaco Concurrente

## 🖍 Descripción
Este proyecto simula el manejo concurrente de un tinaco que recibe agua de dos fuentes (pluvial y cisterna) y suministra agua para tres usos (jardín, lavaderos, baños). Se utiliza el módulo multiprocessing de Python para gestionar los procesos y la sincronización.

## ✨ Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- 🌫 main.py: Punto de entrada. Inicia el tinaco y los procesos.
- ⛈ tinaco_context.py: Contiene la clase TinacoContext que gestiona el estado del tinaco.
- 💧 proceso_pluvial.py: Simula el llenado desde la fuente pluvial.
- 🎊 proceso_cisterna.py: Simula el llenado desde la cisterna.
- 🎍 proceso_jardin.py: Simula el consumo de agua para el jardín.
- 🎎 proceso_lavaderos.py: Simula el consumo de agua para los lavaderos.
- 🧨 proceso_banios.py: Simula el consumo de agua para los baños.

---




---
Autor
Isai Lopez

Licencia
Este proyecto está bajo la licencia MIT.
