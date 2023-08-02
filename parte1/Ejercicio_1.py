class Estudiante:
    def __init__(self, Nombre, Edad, Grado):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Grado = Grado

    def Estudiar(self):
        print(f'{self.Nombre} esta estudiando las infintas bendiciones de Reinhardt... Parece que le falta poco')

Nombre = input('Ingrese el nombre del estudiante: ')
Edad = int(input(f'Ingrese la edad de {Nombre}: '))
Grado = input(f'Ingresa el grado de {Nombre}: ')

estudiante1 = Estudiante(Nombre, Edad, Grado)
print(f'{estudiante1.Nombre} tiene {estudiante1.Edad} anios y esta en grado {estudiante1.Grado}')
while True:
    pregunta = input(f'¿Que esta haciendo {estudiante1.Nombre}?: ').lower()
    if(pregunta == 'estudiar'):
        estudiante1.Estudiar()
    else:
        print(f'{estudiante1.Nombre} esta de vago, parece que se va a quedar en grado {estudiante1.Grado}')