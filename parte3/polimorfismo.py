class gato():
    def sonido(self):
        return "miau"

class perro():
    def sonido(self):
        return 'guau'


def hacer_sonido(animal):
    print(animal.sonido())

Perro = perro()
Gato = gato()
print(Gato.sonido())
hacer_sonido(Perro)
#Ejemplo simple de polimorfismo, esto se puede hacer en lenguajes de tipado dinámico, es decir, no hace falta relacionarlo con herencia