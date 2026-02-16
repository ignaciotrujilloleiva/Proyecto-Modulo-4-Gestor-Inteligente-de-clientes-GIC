**Codigo utilizado en Mermaid.ai para la generación del Diagrama**

```
classDiagram
    %% Relaciones principales
    Cliente <|-- ClienteRegular : Herencia
    Cliente <|-- ClientePremium : Herencia
    Cliente <|-- ClienteCorporativo : Herencia
    GestorClientes o-- "0..*" Cliente : Agregación (Lista)
    
    %% Dependencias de módulos (Opcional para mostrar arquitectura completa)
    Cliente ..> Validaciones : Usa
    GestorClientes ..> Persistencias : Usa
    GestorClientes ..> Logs : Usa

    class Cliente {
        #int _id
        #str _nombre
        #str _apellido
        #str _email
        #str _telefono
        #str _direccion
        +id() int
        +nombre() str
        +apellido() str
        +email() str
        +telefono() str
        +direccion() str
        +__init__(id, nombre, apellido, email, telefono, direccion)
        +__str__() str
        +__eq__(other) bool
    }

    class ClienteRegular {
        +str tipo
        +__init__(id, nombre, apellido, email, telefono, direccion)
    }

    class ClientePremium {
        +str tipo
        +float descuento
        +__init__(id, nombre, apellido, email, telefono, direccion, descuento)
    }

    class ClienteCorporativo {
        +str tipo
        +str empresa
        +__init__(id, nombre, apellido, email, telefono, direccion, empresa)
    }

    class GestorClientes {
        +str formato
        +list lista_clientes
        +__init__(formato)
        +agregar_cliente(cliente)
        +listar_clientes() list
        +buscar_cliente(id_cliente) Cliente
        +eliminar_cliente(id_cliente)
        +editar_cliente(id, nombre, apellido, email, telefono, direccion)
        +guardar()
    }

    class Validaciones {
        <<Module>>
        +validar_nombre(valor)
        +validar_apellido(valor)
        +validar_email(valor)
        +validar_telefono(valor)
        +validar_direccion(valor)
    }

    class Persistencias {
        <<Module>>
        +guardar_clientes_txt(lista)
        +cargar_clientes_txt()
        +guardar_clientes_csv(lista)
        +cargar_clientes_csv()
    }

    class Logs {
        <<Module>>
        +registrar_log(mensaje)
    }
    