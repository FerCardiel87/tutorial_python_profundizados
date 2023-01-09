#ejemplo de herencia simple
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
        return f'{self.__class__.__name__}({self._elementos!r})'

class ListOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        #ordenamos siempre los elementos una vez inicializados
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        #Ordenamos el nuevo elemento
        self.ordenar()

#lista solo acepta numeros
class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        #una vez validados los elementos, los agregamos
        super().__init__(elementos)

    def _validar(self, elemento):
        #Validamos si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')

    #sobreescribimios el metodo agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        #una vez validado lo agregamos a la lista
        super().agregar(elemento)
#lista simple
lista_simple = ListaSimple([5,6,3,5])
print(lista_simple)
#lista ordenada
Lista_ordenada = ListOrdenada([5,4,2,10,2,9,-1])
print(Lista_ordenada)
Lista_ordenada.agregar(-12)
print(Lista_ordenada)
print(len(Lista_ordenada))
#lista enteros
lista_enteros = ListaEnteros([1,2,4, -15])
print(lista_enteros)