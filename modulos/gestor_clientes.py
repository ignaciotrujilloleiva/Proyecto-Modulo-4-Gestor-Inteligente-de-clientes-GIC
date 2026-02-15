# Modulo Gestor de clientes
# Contiene la logica del sistema

#Importación desde cliente, las subclases de clientes
from modulos.cliente import ClienteRegular, ClientePremium, ClienteCorporativo
#Importación desde persistencias, funciones de persistencia para guardar y guardar en formato CSV o TXT
from modulos.persistencias import guardar_clientes_txt, cargar_clientes_txt, guardar_clientes_csv, cargar_clientes_csv
#Importación desde logs, funcion para registrar mensajes en archivo logs.txt
from modulos.logs import registrar_log



# Clase Gestor que administra todos los clientes del sistema
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
        # Registro de mensaje en archivo logs.txt
        registrar_log(f"Cliente agregado: {cliente.nombre} {cliente.apellido}")
        # Guardado automático
        self.guardar()

    # =========================
    #     LISTAR CLIENTES
    # =========================
    def listar_clientes(self):
        # Devuelve la lista de clientes
        return self.lista_clientes

    # =========================
    #  BUSCAR CLIENTE POR ID
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
    #     ELIMINAR CLIENTE
    # =========================
    def eliminar_cliente(self, id_cliente):
        # Reutilizamos el método buscar_cliente para no repetir código.
        cliente = self.buscar_cliente(id_cliente)

        if not cliente:
            registrar_log(f"Intento fallido eliminar ID {id_cliente}")
            raise ValueError("Cliente no encontrado")
        
        # .remove() busca el objeto exacto en la lista y lo borra.
        self.lista_clientes.remove(cliente)
        # Registro de mensaje en archivo logs.txt
        registrar_log(f"Cliente eliminado ID {id_cliente}")
        
        self.guardar()

    # =========================
    #      EDITAR CLIENTE
    # =========================

    def editar_cliente(self, id_cliente, nombre, apellido, email, telefono, direccion):
        cliente = self.buscar_cliente_por_id(id_cliente)

        if not cliente:
            raise ValueError("Cliente no encontrado")

        cliente.nombre = nombre
        cliente.apellido = apellido
        cliente.email = email
        cliente.telefono = telefono
        cliente.direccion = direccion

        registrar_log(f"Cliente editado ID {id_cliente}")
        
        self.guardar_datos()


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
