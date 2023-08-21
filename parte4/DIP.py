from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def Verificar_palabra(self, palabra):
        #Lógica para verificar que la palabra está en el diccionario
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        #Usamos el verificador para corregir el texto
        pass

#Correcta implementación del principio DIP
