class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):#Esto es un getter, para obtener un valor al que no se debería poder acceder si es muy privado o simplemente privado
        return self.__nombre

    def set_nombre(self, nuevo_nombre):#Esto es un setter, para cambiarle el atributo a un valor al que no se debería de poder acceder
        self.__nombre = nuevo_nombre

Aaron = Persona('Aaron', 19)
Aaron.set_nombre('Pollo')
nombre = Aaron.get_nombre()

print(nombre)
