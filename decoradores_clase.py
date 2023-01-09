#decoradores de clase
#permiten transdformar de manera programatica nuestra clase, es similar a los decoradores de funciones(es metaprogramacion)
import inspect


def decorador_repr(cls):
    print('1. Se ejecuta decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')

    # Revisamos los atributos de la clase con el método vars
    atributos = vars(cls)
    # Iteramos cada atributo
    # for nombre, atributo in atributos.items():
    #     print(nombre, atributo)

    # Revisamos si se ha sobreescrito el método __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el método __init__')

    firma_init = inspect.signature(cls.__init__)
    print(f'Firma método __init__: {firma_init}')
    # Recuperamos los parámetros, excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parámetros init: {parametros_init}')

    # Revisamos si cada parámetro tiene un método property asociado
    for parametro in parametros_init:
        # property es un valor de tipo built-in para preguntar si
        # se está utilizando el decorador property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un método property para el parámetro: {parametro}')

    # Crear el método repr dinámicamente
    def metodo_repr(self):
        #obtenemos el nombre de la clase dinamicamente
        nombre_clase = self.__class__.__name__
        print(f'Nombre clase: {nombre_clase}')
        #obteenemos los nombres de propiedades y valores dinamico
        #expresion Generadora, crear nombre_atr=valor_atr
        generador_arg = (f'{nombre}={getattr(self, nombre)}' for nombre in parametros_init)
        #lista de generador
        lista_arg = list(generador_arg)
        print(f'Lista del generador: {lista_arg}')
        #creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos del metodo repr: {argumentos}')
        #creams la forma del metodoo __rerp __ sin su nmbre
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'
        print(f'Resultado metodo repr: {resultado_metodo_repr}')
        return resultado_metodo_repr

    # Agregar dinámicamente el método repr a nuestra clase
    setattr(cls, '__repr__', metodo_repr)

    return cls

@decorador_repr
class Persona:
    def __init__(self, nombre, apellido, edad):
        print('2. Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    # def __repr__(self):
    #     return f'Persona(nombre={self._nombre}, apellido={self._apellido})'

persona1 = Persona('Fernando', 'CardielAvila', 33)
print(persona1)
persona2 = Persona('Liliana', 'Gudiño', 33)
print(persona2)
#tiene los metodos de propuuedad nombre, apellido ,repr
print(dir(Persona))
#tiene el metodo repr sobreescrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)