# Modulo Gestor de clientes

#Importacion desde cliente, las subclases de clientes
from modulos.cliente import ClienteRegular, ClientePremium, ClienteCorporativo


class GestorClientes:
    def __init__(self):
        # Inicializa una lista vacía que servirá como "base de datos" temporal
        # donde se guardarán todos los objetos de tipo cliente.
        self.lista_clientes = []

    # =========================
    #     AGREGAR CLIENTE
    # =========================
    def agregar_cliente(self, cliente):
        # Recibe un objeto (ya validado por su propia clase) y lo guarda en la lista.
        self.lista_clientes.append(cliente)
        print("Cliente agregado correctamente.")

    # =========================
    #     LISTAR CLIENTES
    # =========================
    def listar_clientes(self):
        # Verificación de seguridad: si la lista está vacía, avisa al usuario y sale de la función.
        if not self.lista_clientes:
            print("No hay clientes registrados.")
            return

        # Recorre la lista objeto por objeto.
        for cliente in self.lista_clientes:
            # Aquí ocurre el polimorfismo: se llama al método __str__ de cada cliente.
            print(cliente)

    # =========================
    #      BUSCAR POR ID
    # =========================
    def buscar_cliente(self, id_cliente):
        # Itera por toda la lista buscando una coincidencia de ID.
        for cliente in self.lista_clientes:
            # Compara el ID solicitado con la @property 'id' de cada objeto
            if cliente.id == id_cliente:
                return cliente # Si lo encuentra, devuelve el objeto completo.
        # Si termina el ciclo for y no encontró nada, devuelve None.
        return None

    # =========================
    #         ELIMINAR
    # =========================
    def eliminar_cliente(self, id_cliente):
        # Reutilizamos el método buscar_cliente para no repetir código.
        cliente = self.buscar_cliente(id_cliente)

        if cliente:
            # .remove() busca el objeto exacto en la lista y lo borra.
            self.lista_clientes.remove(cliente)
            print("Cliente eliminado.")
        else:
            # Si el ID no existía, informa el error.
            print("Cliente no encontrado.")
