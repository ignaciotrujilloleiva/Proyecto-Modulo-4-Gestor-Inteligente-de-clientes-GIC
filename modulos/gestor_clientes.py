# Modulo Gestor de clientes

#Importación desde cliente, las subclases de clientes
from modulos.cliente import ClienteRegular, ClientePremium, ClienteCorporativo
#Importación desde persistencias, funciones de persistencia para guardar y guardar en formato CSV o TXT
from modulos.persistencias import guardar_clientes_txt, cargar_clientes_txt, guardar_clientes_csv, cargar_clientes_csv
#Importación desde logs, funcion para registrar mensajes en archivo logs.txt
from modulos.logs import registrar_log



# Clase que administra todos los clientes del sistema
class GestorClientes:
    def __init__(self, formato="csv"):
        # Se deja por defecto el formato csv para la persistencia de datos
        self.formato = formato
        # Si se ingresa el (formato="txt") al llamar la clase GestorClientes(formato="txt") este guardara en archivo TXT 
        if formato == "txt":
            self.lista_clientes = cargar_clientes_txt()
        else:
            self.lista_clientes = cargar_clientes_csv()

    # =========================
    #     AGREGAR CLIENTE
    # =========================
    def agregar_cliente(self, cliente):
        # Recibe un objeto (ya validado por su propia clase) y lo guarda en la lista.
        self.lista_clientes.append(cliente)
        print("Cliente agregado correctamente.")
        # Registro de mensaje en archivo logs.txt
        registrar_log(f"Cliente agregado: {cliente.nombre} {cliente.apellido}")

    # =========================
    #     LISTAR CLIENTES
    # =========================
    def listar_clientes(self):
        # Verificación de seguridad: si la lista está vacía, avisa al usuario y sale de la función.
        if not self.lista_clientes:
            print("No hay clientes registrados.")
            return

        # Recorre la lista objeto por objeto.
        print("\n--- LISTA DE CLIENTES ---")
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
            # Registro de mensaje en archivo logs.txt
            registrar_log(f"Cliente eliminado ID {id_cliente}")
        else:
            # Si el ID no existía, informa el error.
            print("Cliente no encontrado.")
            # Registro de mensaje en archivo logs.txt
            registrar_log(f"Intento fallido de eliminar ID {id_cliente}")

    # =========================
    #    GUARDAR EN TXT y CSV
    # =========================
    def guardar(self):
        # Guarda la lista en el archivo CSV o TXT 
        if self.formato == "txt":
            guardar_clientes_txt(self.lista_clientes)
        else:
            guardar_clientes_csv(self.lista_clientes)

        # Registro de mensaje en archivo logs.txt
        registrar_log("Datos guardados en archivo")
        print("Datos guardados correctamente.")
