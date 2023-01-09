class Padre:
    def __init__(self):
        print('Inicializador Padre')

    def metodo(self):
        print('Metodo padre')

class Hijo(Padre):
    #se manda a llamar el metodo __init__ de la clase padre
#siempre yu cuando la clase hija no defina su propio metodo init

    #definimos el metodo init
    def __init__(self):
        #de manera opcional podemos llamar al metodo __init__ de la clase cpadre(super)

        print('Inicializando hijo')
        super().__init__()

    #Sobreescribimos el metodo heredado de la clase padre
    def metodo(self):
           print('Metodo sobreescrito hijo')
           super().metodo()

# padre1 = Padre()
# padre1.metodo()
hijo1 = Hijo()
hijo1.metodo()