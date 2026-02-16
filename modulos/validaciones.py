# Modulo Validaciones

# librería de Expresiones Regulares de Python, diseñada para trabajar con patrones de texto, usada para validar que el email cumpla un patron de email.
import re


def validar_nombre(valor):
    if not valor.strip():
        raise ValueError("El nombre no puede estar vacío")
    return valor


def validar_apellido(valor):
    if not valor.strip():
        raise ValueError("El apellido no puede estar vacío")
    return valor


def validar_email(valor):
    patron = r"[^@]+@[^@]+\.[^@]+"
    if not re.match(patron, valor):
        raise ValueError("Email inválido")
    return valor


def validar_telefono(valor):
    if not valor.isdigit() or len(valor) < 8:
        raise ValueError("Teléfono inválido")
    return valor


def validar_direccion(valor):
    if not valor.strip():
        raise ValueError("Dirección vacía")
    return valor