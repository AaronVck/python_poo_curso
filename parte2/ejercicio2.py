class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def Datos(self):
        print(f'Soy {self.nombre} y tengo {self.edad} años.')


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def MuestraGrado(self):
        print(f'{self.nombre} está en grado {self.grado}.')

alumno = Estudiante('Aaron', 19, '3')
alumno.Datos()
alumno.MuestraGrado()