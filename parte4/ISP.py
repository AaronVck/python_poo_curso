# from abc import ABC, abstractmethod

# class Trabajador(ABC):#Esta plantilla se considera una interfaz

#     @abstractmethod
#     def comer(self):
#         pass

#     @abstractmethod
#     def trabajar(self):
#         pass

#     @abstractmethod
#     def dormir(self):
#         pass

# class Humano(Trabajador):

    
#     def comer(self):
#         print('El humano está comiendo')

    
#     def trabajar(self):
#         print('El humano está trabajando')

    
#     def dormir(self):
#         print('El humano está durmiendo')

# class Robot(Trabajador):

#     def comer(self):
#         pass

    
#     def trabajar(self):
#         print('El robot está trabajando')

    
#     def dormir(self):
#         pass
#La clase robot viola el principio ISP debido a que no se puede obligar a prescindir de los métodos comer y dormir

from abc import ABC, abstractmethod

class Comedor(ABC):#Esta plantilla se considera una interfaz

    @abstractmethod
    def comer(self):
        pass

class Trabajador(ABC):

    @abstractmethod
    def trabajar(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador, Durmiente, Comedor):

    
    def comer(self):
        print('El humano está comiendo')

    
    def trabajar(self):
        print('El humano está trabajando')

    
    def dormir(self):
        print('El humano está durmiendo')

class Robot(Trabajador):


    
    def trabajar(self):
        print('El robot está trabajando')

    
ROBOT = Robot()

ROBOT.trabajar()

#Así se cumple el principio ISP