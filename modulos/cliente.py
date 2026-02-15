# Modulo cliente

#Importaciones desde validaciónes
from modulos.validaciones import validar_email, validar_telefono

# =========================
#        CLASE PADRE
# =========================

class Cliente:
    contador_id = 1 #atributo de clase para generar ID's automáticos

    def __init__(self, nombre, apellido, email, telefono, direccion):
        self._id = Cliente.contador_id
        Cliente.contador_id += 1

        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

# Properties (Getters)
# Permiten leer el valor de un atributo protegido (_nombre) como si fuera público.
# Setters, actúan como "filtros de seguridad" antes de guardar un dato.

    #id
    @property
    def id(self):
        return self._id

    #Nombre
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        #Validación para evitar strings vacios
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

    #Apellido
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, valor):
        if not valor.strip():
            raise ValueError("El apellido no puede estar vacío")
        self._apellido = valor
    
    #Email
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        if not validar_email(valor):
            raise ValueError("Email inválido")
        self._email = valor

    #Telefono
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        #Validación pendiente
        if not validar_telefono(valor):
            raise ValueError("Teléfono inválido")
        self._telefono = valor

    #Dirección
    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, valor):
        if not valor.strip():
            raise ValueError("Dirección vacía")
        self._direccion = valor

# Métodos especiales

# Define cómo se verá el objeto al hacer el print del cliente
    def __str__(self):
        return f"[{self.id}] {self.nombre} {self.apellido} - {self.email} - {self.telefono}"

# Define la lógica de igualdad (cliente1 == cliente2)
# Verifica que el otro objeto sea de la misma clase y tengan el mismo ID
    def __eq__(self, other):
        return isinstance(other, Cliente) and self.id == other.id
    

# =========================
#        SUBCLASES
# =========================

# Aplicación de herencia
# super().__init__ llama al constructor de la clase padre (Cliente).
# self.tipo = es para el atributo específico para identificar el nivel del cliente.
# La subclase ClientePremium recibe un parámetro extra: 'descuento', que por defecto es 0.1 (10%).
# La subclase ClienteCorporativo recibe el paramentro extra: 'empresa'
# Se sobreescribe el método __str__ para que al imprimir el objeto según el cliente.

class ClienteRegular(Cliente):
    def __init__(self, nombre, apellido, email, telefono, direccion):
        super().__init__(nombre, apellido, email, telefono, direccion)
        self.tipo = "Regular"

    def __str__(self):
        return f"[{self.id}] {self.nombre} {self.apellido} (Regular)"


class ClientePremium(Cliente):
    def __init__(self, nombre, apellido, email, telefono, direccion, descuento=0.1):
        super().__init__(nombre, apellido, email, telefono, direccion)
        self.tipo = "Premium"
        self.descuento = descuento

    def __str__(self):
        return f"[{self.id}] {self.nombre} {self.apellido} (Premium - Desc:{self.descuento*100}%)"


class ClienteCorporativo(Cliente):
    def __init__(self, nombre, apellido, email, telefono, direccion, empresa):
        super().__init__(nombre, apellido, email, telefono, direccion)
        self.tipo = "Corporativo"
        self.empresa = empresa

    def __str__(self):
        return f"[{self.id}] {self.nombre} {self.apellido} ({self.empresa} - Corporativo)"
