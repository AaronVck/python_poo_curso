#properties son getters y setters
class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad



    @property #este decorador define la función como un getter, y provoca que ya no sea necesario el uso de parentesis, incluso aunque sea un atributo MUY privado
    def nombre(self):
        return self.__nombre




    @nombre.setter #Este decorador define esta funcion como un setter de otra funcion, ya que las funciones se llaman iguales, pero esto no es sobrecarga de metodos
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter #Este decorador funciona para poder eliminar el atributo, si no existiera no sería posible borrarlo. Se borraría con "del Aaron.nombre"
    def nombre(self):
        del self.__nombre




#Uso de getter
Aaron = Persona('Aaron', 19)
#NOTA: SI SE QUISIERA MODIFICAR EL ATRIBUTO, NO SE PODRÍA, PORQUE ESTÁ CONSIDERADO COMO UN GETTER Y NO UN SETTER, GRACIAS AL DECORADOR PROPERTY
nombre = Aaron.nombre
print(nombre)

#Uso de setter
Aaron.nombre = 'Chago'
nombre = Aaron.nombre
print(nombre)

#Uso de deletter
del Aaron.nombre
#nombre = Aaron.nombre #Si dejo esta linea el código va a dar error porque ya no existe ningun nombre
print(nombre)