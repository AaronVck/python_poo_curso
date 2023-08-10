class MiClase:
    def __init__(self):
        self._atributo_privado = 'valor' #con el "_" despues de self, se sobreentiende que hablamos de un atributo privado

objeto = MiClase()
print(objeto._atributo_privado)

#SIN EMBARGO, si se le agregan 2 guiones bajos, "__" se le considera un atributo muy privado,  ya no es posible acceder al mismo de manera convencional
#El encapsulmaiento mejora la legibilidad del código
#Nota: tambien se puede hacer metodos muy privados usando el doble guin bajo "__"