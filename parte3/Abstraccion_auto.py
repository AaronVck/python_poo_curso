class Auto():
    def __init__(self):
        self._estado = 'apagado'

    def encender(self):
        self._estado = 'encendido'
        print('El auto está encendido')

    def conducir(self):
        if self._estado == 'apagado':
            self.encender()
        print('Conduciendo auto')

mi_auto = Auto()
mi_auto.conducir()
#Abstracción es ocultar toda la lógica al usuario para que la funcionalidad del programa sea simple. 