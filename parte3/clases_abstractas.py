#una clase abstracta es una clase que no se puede instanciar pero hace la funcion de plantilla
from abc import ABC, abstractclassmethod#abstractclassmethod es un decorador

class Persona(ABC):
    @abstractclassmethod#Este método es abstracto porque solo hará la función de plantilla ya que cada persona tiene su nombre, edad, sexo, etc.
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod#Al igual que el anterior método, no todos tienen las mismas actividades, por eso esta clase es abstracta 
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f'Hola me llamo: {self.nombre} y tengo {self.edad} años')

#Al crear clases abstractas no se nos permitirá instanciar de manera común. Ahora se deberá de instanciar/implementar mediante otra clase 

class Estudiante(Persona):
    def __init__(self,nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Estoy estudiando: {self.actividad}')

class Trabajador(Persona):
    def __init__(self,nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Trabajo en el campo de: {self.actividad}')

Aaron = Estudiante('Aaron', 19, 'Masculino', 'Programación')
Cesar = Trabajador('Cesar', 19, 'Masculino', 'Programación')
Aaron.presentarse()
Aaron.hacer_actividad()
Cesar.presentarse()
Cesar.hacer_actividad()