#Snake_Case separa_todo_con_espacios
#PascalCase SeparaTodoUsandoLaPrimeraLetraEnMayúsculas
#class palabra reservada para crear clases 
"""Info que ya sabía: 
Un objeto es una instancia de una clase
Los objetos en python se guardan en la ram"""
class Personaje:
    def __init__(self, Nombre, Bendicion, Arma):#Metodo constructor que se ejecuta al crear un objeto, self hace referencia asimismo
        self.Nombre = Nombre
        self.Bendicion = Bendicion
        self.Arma = Arma
    
    def Saludo(self):#Esto es un método, un método es una accion/función
        print(f'{self.Nombre} te esta saludando.')#Self siempre se debe de usar para que se referencie a los atributos que tiene el objeto

    def Enojo(self):
        print(f'{self.Nombre} esta enojado contigo y te amenaza con {self.Arma}')



personaje1 = Personaje('Subaru', 'Retorno de la muerte', 'Latigo')
personaje2 = Personaje('Crusch', 'Lectura del viento', 'Espada de la familia Lugunica')
print(f'{personaje1.Nombre} tiene la bendicion {personaje1.Bendicion} y tiene como arma {personaje1.Arma}.')
print(f'{personaje2.Nombre} tiene la bendicion {personaje2.Bendicion} y tiene como arma {personaje2.Arma}.')
personaje2.Saludo()
personaje1.Enojo()
