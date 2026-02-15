# Modulo Logs

from datetime import datetime
import os

# Ruta para archivo logs.txt
RUTA_LOG = "data/logs.txt"

# Función para el registro de mensaje en el logs.txt
# Guarda un mensaje en el archivo logs.txt con fecha y hora.
def registrar_log(mensaje):
    
    # Crea el directorio con la carpeta data, exist_ok=True es para que no presente error si la carpeta existe
    os.makedirs("data", exist_ok=True)

    # Almacena en variable la fecha y hora exacta en la que se ejecuta la función, da formato a el tiempo en formato de cadena
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Se abre la ruta del archivo log en modo "a" para añadir terto al final y dejar el mensaje en el log
    with open(RUTA_LOG, "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] {mensaje}\n")
