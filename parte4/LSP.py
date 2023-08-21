class Ave():
    #Aquí se colocarían todas las características que tienen en común aves tanto voladoras como no voladoras, esto para cumplir el principio de LSP
    pass#

class AveVoladora(Ave):
    #Aquí se colocarían las características de las aves exclusivamente voladoras
    pass

class AveNoVoladora(Ave):
    #Aquí se colocarían las características de las aves exclusivamente NO voladoras
    pass

#En este caso se cumple el principio, la subclases son capaces de hacer todo lo que hace la clase base