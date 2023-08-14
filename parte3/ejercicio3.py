class Personaje():
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __add__(self, personaje2):
        FuerzaMultiplicada = (self.fuerza + personaje2.fuerza) ** 1.4
        VelocidadMultiplicada = (self.velocidad + personaje2.velocidad) ** 1.4
        return (f'Un nuevo héroe ha sido creado, su nombre es: {self.nombre + personaje2.nombre} su fuerza es de {FuerzaMultiplicada} y su velocidad de {VelocidadMultiplicada}!!!!')

    def getNombre(self):
        return self.nombre





personajes = []
while True:
    print('1.-Crear personaje')
    print('2.-Fusionar personajes')
    print('3.-Mostrar personajes')
    print('4.-Salir')
    opc = int(input(': '))

    if opc == 1:
        nom = input('Ingrese el nombre de su personaje: ')
        fuer = int(input(f'Ingrese la fuerza de {nom}: '))
        vel = int(input(f'Ingrese la velocidad de {nom}: '))
        creacion = Personaje(nom, fuer, vel)
        personajes.append(creacion)
        print('Personaje creado con éxito')
    elif opc == 2:
        heroe1=[]
        heroe2=[]
        print('A quienes deseas fusionar? (Ingresa el numero de tu personaje)')
        for i in range(0,len(personajes)):
            print('**************************')
            print('')
            print(f'{str(i+1)}.- {personajes[i].nombre}')
            print('')
            print('**************************')
        indice1 = int(input('Personaje1: '))-1
        indice2 = int(input('Personaje2: '))-1

        heroe1 = personajes[indice1]
        heroe2 = personajes[indice2]
        nuevo_heroe = heroe1 + heroe2
        #personajes.append(nuevo_heroe)
        print(nuevo_heroe)
        creacion = Personaje(personajes[indice1].nombre+personajes[indice2].nombre, personajes[indice1].fuerza + personajes[indice2].fuerza, personajes[indice1].velocidad+personajes[indice2].velocidad)
        personajes.append(creacion)
    elif opc == 3:
        for i in range(0,len(personajes)):
            print('**************************')
            print('')
            print(f'{str(i+1)}.- {personajes[i].nombre}')
            print('')
            print('**************************')
    elif opc == 4:
        print('Adios')
        break
    else: 
        print('Seleccione una opción válida')

