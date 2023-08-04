class A:
    def Hablar(self):
        print('Hola desde A')

class B(A):
    def Hablar(self):
        print('Hola desde B')

class C(A):
    def Hablar(self):
        print('Hola desde C')

class D(B,C):
    def Hablar(self):
        print('Hola desde D')

d = D()
d.Hablar()
print(D.mro())
"""Con este codigo se puede experimentar como funciona el mro y las prioridades que tiene python de manera interna, esto es importante a la hora de usar POO ya que hay que tener muy en cuenta estos factores a la hora de establecer un orden"""