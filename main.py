from modulos.cliente import ClienteRegular, ClientePremium, ClienteCorporativo

c1 = ClienteRegular("Ignacio", "Trujillo", "ignacio@mail.com", "12345678", "Santiago")
c2 = ClientePremium("Ana", "Lopez", "ana@mail.com", "99999999", "Valparaiso", 0.2)
c3 = ClienteCorporativo("Carlos", "Perez", "carlos@mail.com", "88888888", "Santiago", "TechCorp")

print(c1)
print(c2)
print(c3)
