from pprint import pprint

almacen_desactualizado = {
"Alcohol":
[
{ "nombre": "Linaje", "marca": "Santa Teresa", "grado": 40, "tipo": "Ron", "disponible": True
},
{ "nombre": "Black Label 18", "marca": "Jonnie Walker", "grado": 43, "tipo": "Whisky",
"disponible": True },
{ "nombre": "Solera Verde", "marca": "Polar", "grado": 6, "tipo": "Cerveza", "disponible":
True }
],
"Refresco":
[
{ "nombre": "Maltin Polar", "marca": "Polar", "azucar": 7, "sabor": "Malta", "disponible":
True },
{ "nombre": "Pepsi", "marca": "Pepsico", "azucar": 7, "sabor": "Cola", "disponible": True },
{ "nombre": "Chinoto", "marca": "The Coca-Cola Company", "azucar": 4, "sabor": "Limon",
"disponible": True }
]
}

class Bebida():
    def __init__(self, name, marca, disponible):
        self.name = name
        self.marca = marca
        self.disponible = disponible
    
    def mostrar():
        return "Datos de la bebida: Nombre: {}, Marca: {}, Disponible: {}".format(Bebida.name, Bebida.marca, Bebida.disponible)
    
class Refresco(Bebida):
  def __init__(self, name, marca, disponible, azucar, sabor):
        Bebida.__init__(self, name, marca, disponible)
        self.azucar = azucar
        self.sabor = sabor
    
class Alcohol(Bebida):
    def __init__(self, name, marca, disponible, grado, tipo):
        Bebida.__init__(self, name, marca, disponible)
        self.grado = grado
        self.tipo = tipo

vasito = Refresco("Vaso", "7UP", True)
print(vasito.mostrar())
