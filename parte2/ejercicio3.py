class Animal:
    def Comer(self):
        print('Estoy comiendo')

class Mamifero(Animal):
    def Amamantar(self):
        print('Estoy amamantando')

class Ave(Animal):
    def Volar(self):
        print('Estoy volando')

class Murcielago(Mamifero, Ave):
    pass

murci = Murcielago()
murci.Amamantar()
murci.Comer()
murci.Volar()