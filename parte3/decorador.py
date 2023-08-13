# def decorador(funcion): #3
#     def funcion_modificada(): #5
#         print('Antes de llamar a la función') #6
#         funcion() #7
#         print('Después de llamar a la función') #9
#     return funcion_modificada #4

# def saludo(): #8
#     print('Hola amigon')

# saludo_modificado = decorador(saludo) #2
# saludo_modificado() #1
#A mi entender, es básicamente una función que ejecuta otras funciones en un orden específico
#Lo anterior es una manera primitiva, a continuación viene la forma óptima

def decorador(funcion): 
    def funcion_modificada(): 
        print('Antes de llamar a la función') 
        funcion() 
        print('Después de llamar a la función') 
    return funcion_modificada 

@decorador #Este es el decorador, se coloca encima de la funcion. Sirve para hacer validaciones
def saludo():
    print('Hola amigon')

saludo()
#Un decorador agarra una función y le agrega funcionalidad antes o después de ejecutar una función