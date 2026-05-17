# CRUD de Posts con Python y JSONPlaceholder

Este es un proyecto de consola en Python que implementa un sistema CRUD (Create, Read, Update, Delete) básico consumiendo una API REST falsa utilizando la librería `requests`. Además, cuenta con una interfaz de menú interactiva a color en la terminal mediante `colorama`.

## 🚀 Características

- **Consumo de API:** Conexión interactiva con [JSONPlaceholder](https://jsonplaceholder.typicode.com/).
- **Peticiones Seguras:** Manejo robusto de errores mediante bloques `try-except` para capturar fallos de conexión, códigos HTTP inesperados y timeouts.
- **Interfaz Colorida:** Menú visualmente organizado y estilizado por colores en la terminal.
- **Operaciones CRUD Completas:**
  - **Ver (GET):** Lista los primeros posts disponibles.
  - **Crear (POST):** Envía un nuevo post simulado a la API.
  - **Actualizar (PUT):** Modifica los datos de un post por su ID.
  - **Eliminar (DELETE):** Borra un post del servidor por su ID.

## 🛠️ Requisitos Previos

Asegurate de tener Python instalado (versión 3.x recomendada) y las librerías necesarias.

### Instalación de Dependencias

Podés instalar los paquetes necesarios ejecutando:

```bash
pip install -r requirements.txt