#los metodos especiales son los que inician con dos__ y terminan con__ como __init__
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):#Este metodo representa la manera en que se va a mostrar en pantalla como cadena de texto, de manera personalizada
        return f'Persona(nombre={self.nombre},edad={self.edad})'


    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)


Aaron = Persona('Aaron', 19)
Cesar = Persona('Cesar',19)
nuevapersona = Aaron + Cesar
print(nuevapersona.edad)
