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
        print("3. Eliminar cliente")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                crear_cliente()

            elif opcion == "2":
                listar_clientes()

            elif opcion == "3":
                eliminar_cliente()

            elif opcion == "4":
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

# Función 3 para eliminar un cliente mediante el ID
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

