# Modulo cliente

#Importaciones desde validaciónes
from modulos.validaciones import validar_email, validar_telefono

# Clase padre
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

# Define cómo se verá el objeto al hacer: print(cliente)
    def __str__(self):
        return f"[{self.id}] {self.nombre} - {self.email} - {self.telefono}"

# Define la lógica de igualdad (cliente1 == cliente2)
# Verifica que el otro objeto sea de la misma clase y tengan el mismo ID
    def __eq__(self, other):
        return isinstance(other, Cliente) and self.id == other.id