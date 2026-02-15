# Menú principal del sistema
# Encargado de solicitar los datos al usuario

from modulos.gestor_clientes import GestorClientes
from modulos.cliente import Cliente

gestor = GestorClientes()

# ===============================
#        MENÚ PRINCIPAL
# ===============================

def menu():
    while True:
        print("\n==============================")
        print("   GESTOR INTELIGENTE CLIENTES")
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
                print("\nSaliendo del sistema...")
                break

            else:
                print("❌ Opción inválida")

        except Exception as e:
            print(f"\n⚠ Error general en el sistema: {e}")


# ===============================
#     FUNCIONES DE INTERFAZ
# ===============================


# Función 1° para creación del cliente
def crear_cliente():
    print("\n--- Crear cliente ---")

    while True:
        try:
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            email = input("Email: ").strip()
            telefono = input("Teléfono: ").strip()
            direccion = input("Dirección: ").strip()

            cliente = Cliente(nombre, apellido, email, telefono, direccion)
            gestor.agregar_cliente(cliente)

            print("\n✅ Cliente creado correctamente\n")
            break

        except ValueError as e:
            print(f"\n❌ Error: {e}")
            print("Intente nuevamente...\n")

        except Exception as e:
            print(f"\n⚠ Error inesperado: {e}")
            break

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
    print("\n--- Buscar cliente por ID ---")

    try:
        id_cliente = int(input("Ingrese ID: "))
        cliente = gestor.buscar_cliente(id_cliente)

        if cliente:
            print("\nCliente encontrado:")
            print(cliente)
        else:
            print("Cliente no existe")

    except ValueError:
        print("ID inválido")

# Función 4° para edición de datos del cliente
def editar_cliente():
    print("\n--- Editar cliente ---")

    try:
        id_cliente = int(input("ID del cliente: "))
        cliente = gestor.buscar_cliente(id_cliente)

        if not cliente:
            print("Cliente no encontrado")
            return

        print("Deje vacío para mantener valor actual\n")

        nombre = input(f"Nombre ({cliente.nombre}): ") or cliente.nombre
        apellido = input(f"Apellido ({cliente.apellido}): ") or cliente.apellido
        email = input(f"Email ({cliente.email}): ") or cliente.email
        telefono = input(f"Teléfono ({cliente.telefono}): ") or cliente.telefono
        direccion = input(f"Dirección ({cliente.direccion}): ") or cliente.direccion

        gestor.editar_cliente(
            id_cliente,
            nombre,
            apellido,
            email,
            telefono,
            direccion
        )

        print("✅ Cliente actualizado")

    except ValueError as e:
        print(f"❌ Error: {e}")

    except Exception as e:
        print(f"Error inesperado: {e}")


# Función 5 para eliminar un cliente mediante el ID
def eliminar_cliente():
    print("\n--- Eliminar cliente ---")

    try:
        id_cliente = int(input("Ingrese ID del cliente: "))
        gestor.eliminar_cliente(id_cliente)
        print("✅ Cliente eliminado")

    except ValueError:
        print("❌ ID inválido")

    except Exception as e:
        print(f"Error: {e}")

