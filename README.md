## Grupo 4
Una docente de informática en una secundaria revisa tareas impresas que sus estudiantes colocan sobre su escritorio. Siempre revisa primero la última tarea entregada. Implementa un sistema que permita agregar tareas (push), revisar una (pop), y mostrar cuál es la siguiente en revisar (peek), todo usando una pila.
## Prerequisitos
1. **Python 3.8** o superior. Verificá con:

- Linux/Mac:
  ```bash
  python3 --version
  ```
- Windows:
  ```bash
  py --version
  ```
2. **Git**. Necesario para clonar el repositorio
3. **Conexión a internet**. Para el CDN de Bootstrap
# Instalación
1. Cloná el repositorio
  ```bash
  git clone git@github.com:c04o/SIS0108-w7-gw.git
  cd SIS0108-w7-gw
  ```
2. Creá un entorno virtual
- Linux/Mac:
  ```bash
  python3 -m venv .venv
  ```
- Windows:
  ```bash
  py -3 -m venv venv
  ```
3. Activá el entorno virtual
- Linux/Mac:
  ```bash
  . .venv/bin/activate
  ```
- Windows:
  ```bash
  .venv\Scripts\activate
  ```
  > Vas a ver `(venv)` en la terminal, indicando que el entorno está activo
4. Instalá Flask dentro del entorno virtual
```bash
pip install flask
```
5. Ejecutá la aplicación
- Linux/Mac:
  ```bash
  python3 app.py
  ```
- Windows:
  ```bash
  py app.py
  ```
---
Deberías tener una salida similar en la terminal:
```plain
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 122-553-431
```
De ser el caso, podés usar la aplicacion accediendo a `http://127.0.0.1:5000` (o su equivalente) en tu navegador
