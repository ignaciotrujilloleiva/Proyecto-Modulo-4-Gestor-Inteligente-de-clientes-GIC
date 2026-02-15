# Modulo Validaciones

# librería de Expresiones Regulares de Python, diseñada para trabajar con patrones de texto, usada para validar que el email cumpla un patron de email.
import re


def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    # re.match compara el patrón con el email recibido, de ser igual el patron este retornara un true
    return re.match(patron, email) is not None


def validar_telefono(telefono):
    # Valida que el telefono cumpla que todos los caracteres sean digitos y tenga un largo = o mayor a 8 digitos
    return telefono.isdigit() and len(telefono) >= 8
