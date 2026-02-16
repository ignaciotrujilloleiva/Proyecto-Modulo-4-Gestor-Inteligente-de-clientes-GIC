# Modulo persistencia

# Importa para leer y escribir en el archivo CSV
import csv
# Import para que Python pueda interactuar con windows, mac o linux para poder manipular carpetas y archivos
import os
# Import de las subclases ubicadas en cliente.py
from modulos.cliente import ClienteRegular, ClientePremium, ClienteCorporativo

# Direcciones para guardar los clientes
RUTA_TXT = "data/clientes.txt"
RUTA_CSV = "data/clientes.csv"

# =========================
#   PERSISTENCIA CON TXT
# =========================

def guardar_clientes_txt(lista_clientes):
    # "makedirs" crea la carpeta llamada "data" y si esta existe el "exist_ok=True" evita que el programa falle.  
    os.makedirs("data", exist_ok=True)

    # Abrimos el archivo en modo "w" para escribir. 'encoding="utf-8"' es para que acepte tildes y la ñ.
    with open(RUTA_TXT, mode="w", encoding="utf-8") as archivo:
        for c in lista_clientes:
            # Creamos una cadena de texto con los datos del cliente
            linea = f"{c.tipo}|{c.id}|{c.nombre}|{c.apellido}|{c.email}|{c.telefono}|{c.direccion}"

            # Algunos clientes tienen datos extra, revisamos qué tipo de cliente es
            if isinstance(c, ClientePremium):
                linea += f"|{c.descuento}"
            elif isinstance(c, ClienteCorporativo):
                linea += f"|{c.empresa}"
            else:
                linea += "|"

            # Se guarda la línea en el archivo y saltamos a la siguiente con "\n".
            archivo.write(linea + "\n")


def cargar_clientes_txt():
    clientes = []

    # Si el archivo no existe todavía, devolvemos la lista vacía.
    if not os.path.exists(RUTA_TXT):
        return clientes

    with open(RUTA_TXT, mode="r", encoding="utf-8") as archivo:
        for linea in archivo:
            # .strip() quita el salto de línea y .split("|") corta el texto donde haya un "|" creando una lista.
            datos = linea.strip().split("|")

            tipo = datos[0]
            nombre = datos[2] # El índice 1 es el ID que se genera automaticamente
            apellido = datos[3]
            email = datos[4]
            telefono = datos[5]
            direccion = datos[6]
            # Si hay un dato en la posición 7, lo guardamos; si no, queda vacío.
            extra = datos[7] if len(datos) > 7 else ""

            # Se crea el objeto segun el tipo de cliente
            if tipo == "Regular":
                cliente = ClienteRegular(nombre, apellido, email, telefono, direccion)

            elif tipo == "Premium":
                cliente = ClientePremium(nombre, apellido, email, telefono, direccion, float(extra))

            elif tipo == "Corporativo":
                cliente = ClienteCorporativo(nombre, apellido, email, telefono, direccion, extra)

            else:
                continue

            clientes.append(cliente)

    return clientes

# =========================
#   PERSISTENCIA CON CSV
# =========================


def guardar_clientes_csv(lista_clientes):
    os.makedirs("data", exist_ok=True)

    # 'newline=""' es importante en CSV para que no deje filas en blanco extra en Windows.
    with open(RUTA_CSV, mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)

        # Escribimos la primera fila con los títulos de las columnas.
        writer.writerow([
            "tipo", "id", "nombre", "apellido", "email", "telefono", "direccion", "extra"
        ])

        for c in lista_clientes:
            extra = ""

            # Identificamos el dato especial según la clase.
            if isinstance(c, ClientePremium):
                extra = c.descuento
            elif isinstance(c, ClienteCorporativo):
                extra = c.empresa

            writer.writerow([
                c.tipo,
                c.id,
                c.nombre,
                c.apellido,
                c.email,
                c.telefono,
                c.direccion,
                extra
            ])


def cargar_clientes_csv():
    clientes = []

    if not os.path.exists(RUTA_CSV):
        return clientes

    with open(RUTA_CSV, mode="r", encoding="utf-8") as archivo:
        # DictReader sirve para leer la primera fila y permite usar los nombres (ej: fila["nombre"]).
        reader = csv.DictReader(archivo)

        for fila in reader:
            tipo = fila["tipo"]
            #Se incorpora ID para uso en los tipos de clientes
            id_cliente = int(fila["id"]) 

            # Sacamos los datos usando las etiquetas que pusimos en la cabecera.
            if tipo == "Regular":
                cliente = ClienteRegular(
                    id_cliente,
                    fila["nombre"],
                    fila["apellido"],
                    fila["email"],
                    fila["telefono"],
                    fila["direccion"]
                )

            elif tipo == "Premium":
                cliente = ClientePremium(
                    id_cliente,
                    fila["nombre"],
                    fila["apellido"],
                    fila["email"],
                    fila["telefono"],
                    fila["direccion"],
                    float(fila["extra"]) if fila["extra"] else 0
                )

            elif tipo == "Corporativo":
                cliente = ClienteCorporativo(
                    id_cliente,
                    fila["nombre"],
                    fila["apellido"],
                    fila["email"],
                    fila["telefono"],
                    fila["direccion"],
                    fila["extra"]
                )
            else:
                continue

            clientes.append(cliente)

    return clientes