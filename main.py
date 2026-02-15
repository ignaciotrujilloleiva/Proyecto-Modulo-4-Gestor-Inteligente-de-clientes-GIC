from modulos.gestor_clientes import GestorClientes
from modulos.cliente import ClienteRegular, ClientePremium

#Prueba que consiste en crear un objeto lista (gestor) se crean 2 clientes con sus atributos, se listan los clientes en el archivo csv y los guarda para comprobar la persistencia, se implementa la opcion mediante el atributo formato se pueda guardar en archivo TXT, en caso de no dar formato por defecto guarda en CSV

gestor = GestorClientes(formato="txt")

print("---- PRUEBA LOGS ----")

c1 = ClienteRegular("Ignacio", "Trujillo", "ignacio@mail.com", "12345678", "Santiago")
c2 = ClientePremium("Ana", "Lopez", "ana@mail.com", "99999999", "Valpo", 0.2)

gestor.agregar_cliente(c1)
gestor.agregar_cliente(c2)
gestor.listar_clientes()
gestor.eliminar_cliente(c1.id)
gestor.guardar()
print("Revisa data/logs.txt")