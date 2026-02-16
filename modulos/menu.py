# =========================================================
# MENÚ PRINCIPAL DEL SISTEMA
# =========================================================

from modulos.gestor_clientes import GestorClientes
from modulos.cliente import ClienteRegular, ClientePremium, ClienteCorporativo
from modulos.validaciones import validar_nombre, validar_apellido, validar_email, validar_telefono, validar_direccion

gestor = GestorClientes()

# =========================================================
# MENÚ
# =========================================================

def menu():
    while True:
        print("\n==============================")
        print("  GESTOR INTELIGENTE CLIENTES")
        print("==============================")
        print("1. Crear cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Editar cliente")
        print("5. Eliminar cliente")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                crear_cliente()

            elif opcion == "2":
                listar_clientes()

            elif opcion == "3":
                buscar_cliente()

            elif opcion == "4":
                editar_cliente()

            elif opcion == "5":
                eliminar_cliente()

            elif opcion == "6":
                print("Saliendo del sistema...")
                break

            else:
                print("❌ Opción inválida")

        except Exception as e:
            print(f"\n⚠ Error inesperado en menú: {e}")

# =========================================================
# INPUTS VALIDOS
# =========================================================

def pedir_nombre():
    while True:
        try:
            valor = input("Nombre: ")
            validar_nombre(valor)
            return valor
        except ValueError as e:
            print(f"❌ {e}")

def pedir_apellido():
    while True:
        try:
            valor = input("Apellido: ")
            validar_apellido(valor)
            return valor
        except ValueError as e:
            print(f"❌ {e}")

def pedir_email():
    while True:
        try:
            valor = input("Email: ")
            validar_email(valor)
            return valor
        except ValueError as e:
            print(f"❌ {e}")

def pedir_telefono():
    while True:
        try:
            valor = input("Teléfono: ")
            validar_telefono(valor)
            return valor
        except ValueError as e:
            print(f"❌ {e}")

def pedir_direccion():
    while True:
        try:
            valor = input("Dirección: ")
            validar_direccion(valor)
            return valor
        except ValueError as e:
            print(f"❌ {e}")

def pedir_tipo_cliente():
    while True:
        print("\nTipo de cliente:")
        print("1. Regular")
        print("2. Premium")
        print("3. Corporativo")

        op = input("Seleccione: ").strip()
        if op in ("1","2","3"):
            return op

        print("❌ Tipo inválido")

# =========================================================
# CREAR
# =========================================================

def crear_cliente():
    print("\n--- Crear cliente ---")

    nombre = pedir_nombre()
    apellido = pedir_apellido()
    email = pedir_email()
    telefono = pedir_telefono()
    direccion = pedir_direccion()
    tipo = pedir_tipo_cliente()

    try:
        if tipo == "1":
            cliente = ClienteRegular(nombre, apellido, email, telefono, direccion)

        elif tipo == "2":
            while True:
                try:
                    valor = input("Descuento (0.1 = 10% | Enter=10%): ").strip()
                    descuento = float(valor) if valor else 0.1
                    cliente = ClientePremium(nombre, apellido, email, telefono, direccion, descuento)
                    break
                except ValueError:
                    print("❌ Descuento inválido")

        elif tipo == "3":
            while True:
                empresa = input("Empresa: ").strip()
                if empresa:
                    cliente = ClienteCorporativo(nombre, apellido, email, telefono, direccion, empresa)
                    break
                print("❌ Debe ingresar empresa")

        gestor.agregar_cliente(cliente)
        print("\n✅ Cliente creado correctamente\n")

    except Exception as e:
        print(f"\n⚠ Error inesperado: {e}")

# Función 2° para listar clientes
def listar_clientes():
    print("\n--- Lista de clientes ---")

    clientes = gestor.listar_clientes()

    if not clientes:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print(cliente)

# Función 3° para buscar cliente mediante su ID
def buscar_cliente():
    print("\n--- Buscar cliente ---")

    try:
        id_cliente = int(input("Ingrese ID: "))
        cliente = gestor.buscar_cliente(id_cliente)

        if cliente:
            print(cliente)
        else:
            print("Cliente no existe")

    except ValueError:
        print("❌ ID inválido")

# Función 4° para edición de datos del cliente
def editar_cliente():
    print("\n--- Editar cliente ---")

    try:
        id_cliente = int(input("ID cliente: "))
        cliente = gestor.buscar_cliente(id_cliente)

        if not cliente:
            print("Cliente no encontrado")
            return

        print("Enter = mantener valor\n")

        nombre = input(f"Nombre ({cliente.nombre}): ") or cliente.nombre
        apellido = input(f"Apellido ({cliente.apellido}): ") or cliente.apellido
        email = input(f"Email ({cliente.email}): ") or cliente.email
        telefono = input(f"Teléfono ({cliente.telefono}): ") or cliente.telefono
        direccion = input(f"Dirección ({cliente.direccion}): ") or cliente.direccion

        gestor.editar_cliente(id_cliente, nombre, apellido, email, telefono, direccion)
        print("✅ Cliente actualizado")

    except Exception as e:
        print(f"Error: {e}")

# Función 5 para eliminar un cliente mediante el ID
def eliminar_cliente():
    print("\n--- Eliminar cliente ---")

    try:
        id_cliente = int(input("ID cliente: "))
        gestor.eliminar_cliente(id_cliente)
        print("✅ Cliente eliminado")

    except ValueError:
        print("❌ ID inválido")
