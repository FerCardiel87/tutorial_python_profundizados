class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos})'

class ListOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        #ordenamos siempre los elementos una vez incializados
        self.ordenar()
    def agregar(self, elemento):
        super().agregar(elemento)
        #ordenamos el nuevo elemento
        self.ordenar()

#lista solo acepta numeros
class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
            #una vez validados los elementos, los agregamos
            super().__init__(elementos)
    def _validar(self, elemento):
        #validamos si ele emento es de itpo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')

    #sobreescribimos el metodo agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        #una vez validado lo agrgamos a la lista
        super().agregar(elemento)

#lista de enteros ordenada
class ListaEnterosOrdenada(ListaEnteros, ListOrdenada):
    pass



#lista smple
lista_simple = ListaSimple([3,4,1,2])
print(lista_simple)
#lista ordenada
lista_ordenada = ListOrdenada([5,2,5,1,10,4.-22])
print(lista_ordenada)
lista_ordenada.agregar(-13)
print(lista_ordenada)
print(len(lista_ordenada))
#lista enteros
lista_enteros = ListaEnteros([1,2,4,-23])
print(lista_enteros)
#lista enteros ordenada
lista_enteros_ordenada = ListaEnterosOrdenada([4,3,-1,4,5,12])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(-20)
print(lista_enteros_ordenada)
#saber las clases padre y su orden
print(ListaEnterosOrdenada.__bases__)
#MRO Method Resolution Orden
print(ListaEnterosOrdenada.__mro__)
#isisntance
print('Es entero?', isinstance(10, int))
print('Es cadena?', isinstance('Hola', str))
print('Es lista ent ord?', isinstance(lista_enteros_ordenada, ListaEnterosOrdenada))
print('Es lista ent?', isinstance(lista_enteros_ordenada, ListaEnteros))
print('Es lista ord?', isinstance(lista_enteros_ordenada, ListOrdenada))
print('Es lista simple?', isinstance(lista_enteros_ordenada,ListaSimple))
print('Es object?', isinstance(lista_enteros_ordenada, object))
print('Es de varios tipos?', isinstance(lista_enteros_ordenada, (ListaEnteros, ListaSimple)))