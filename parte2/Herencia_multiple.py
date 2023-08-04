class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def Hablar(self):
        print('Hola chavales')


class Empleado(Persona):#Para que herede de la clase Persona, se coloca el nombre de la clase padre en los parentesis como un parametro
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)#super referencia a lo que se quiere heredar de la clase padre
        self.trabajo = trabajo
        self.salario = salario

    def Hablar(self):
        print('NO')#Esto es una sobreescritura de metodos (O sobrecarga, segun yo)





class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def demostrar_habilidad(self):
        return f'Mi habilidad es: {self.habilidad}'


class EmpleadoArtista(Empleado, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def Presentarse(self):
        print(f'Soy: {self.nombre}, {super().demostrar_habilidad()}, trabajo en {self.empresa} y gano {self.salario} al mes.')#usando super se usa el metodo o atributo de la clase padre, si usara self y tuviera una reescritura de metodo entonces se usaria el metodo sobreescrito

aaron = EmpleadoArtista('Aaron', '19', 'Venezolano', 'Frontonear', '40,000','Pollo.inc')
aaron.Presentarse()
#LO anterior fue ejemplo de herencia multiple

subclase = issubclass(EmpleadoArtista, Artista)
instancia = isinstance(aaron, Persona)

print(subclase)
print(instancia)
