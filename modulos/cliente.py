# Modulo cliente
# Encargado de contener la Clase padre Cliente, Subclases, Validaciones con @propertu y uso de ValueError

#Importaciones desde validaciónes
from modulos.validaciones import (validar_nombre, validar_apellido, validar_email, validar_telefono, validar_direccion)

# =========================
#        CLASE PADRE
# =========================

class Cliente:
    contador_id = 1 #atributo de clase para generar ID's automáticos

    def __init__(self, nombre, apellido, email, telefono, direccion):
        # Asignación de ID automática
        self._id = Cliente.contador_id
        Cliente.contador_id += 1

        #Setters con validación
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

# Properties (Getters)
# Permiten leer el valor de un atributo protegido (_nombre) como si fuera público.
# Setters, actúan como "filtros de seguridad" antes de guardar un dato.

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = validar_nombre(valor)

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = validar_apellido(valor)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = validar_email(valor)

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        self._telefono = validar_telefono(valor)

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, valor):
        self._direccion = validar_direccion(valor)

# Método especial
# Define cómo se verá el objeto al hacer el print del cliente
    def __str__(self):
        return f"[{self.id}] {self.nombre} {self.apellido} - {self.email} - {self.telefono}"

# =========================
#        SUBCLASES
# =========================

# Aplicación de herencia
# super().__init__ llama al constructor de la clase padre (Cliente).
# self.tipo = es para el atributo específico para identificar el nivel del cliente.
# La subclase ClientePremium recibe un parámetro extra: 'descuento', que por defecto es 0.1 (10%).
# La subclase ClienteCorporativo recibe el paramentro extra: 'empresa'
# Se sobreescribe el método __str__ para que al imprimir el objeto según el cliente.

# =========================
#    SUBCLASE: REGULAR
# =========================
class ClienteRegular(Cliente):
    def __init__(self, nombre, apellido, email, telefono, direccion):
        super().__init__(nombre, apellido, email, telefono, direccion)
        self.tipo = "Regular"

# =========================
#    SUBCLASE: PREMIUM
# =========================
class ClientePremium(Cliente):
    def __init__(self, nombre, apellido, email, telefono, direccion, descuento=0.1):
        super().__init__(nombre, apellido, email, telefono, direccion)
        self.tipo = "Premium"
        self.descuento = descuento

# =========================
#   SUBCLASE: CORPORATIVO
# =========================
class ClienteCorporativo(Cliente):
    def __init__(self, nombre, apellido, email, telefono, direccion, empresa):
        super().__init__(nombre, apellido, email, telefono, direccion)
        self.tipo = "Corporativo"
        self.empresa = empresa
