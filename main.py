from modulos.gestor_clientes import GestorClientes
from modulos.cliente import ClienteRegular, ClientePremium

#Prueba que consiste en crear un objeto lista (gestor) se crean y se agregan 2 clientes a la lista, se imprime la lista, se borra el cliente (1) y se vuelve a imprimir la lista


gestor = GestorClientes()

c1 = ClienteRegular("Ignacio", "Trujillo", "ignacio@mail.com", "12345678", "Santiago")
c2 = ClientePremium("Ana", "Lopez", "ana@mail.com", "99999999", "Valpo", 0.2)

gestor.agregar_cliente(c1)
gestor.agregar_cliente(c2)

gestor.listar_clientes()

gestor.eliminar_cliente(1)

print("----")
gestor.listar_clientes()
