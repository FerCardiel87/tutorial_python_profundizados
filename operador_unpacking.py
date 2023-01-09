numeros = [1,2,3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')

#desempaquetando al momento de pasar un parametro a una funcion
def sumar(a, b, c):
    print(f'Resultado suma: {a + b + c}')

sumar(*numeros)

#extrar algunas partes de una lista
mi_lista = [1,2,3,4,5,6]
a, *b, c, d, = mi_lista
print(a,b,c,d)

#unir lista
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1, lista2]
print(f'Lista de listas {lista3}')
lista3 = [*lista1, *lista2]
print(f'unir listaS: {lista3}')

#unir diccionarios
dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'D': 4, 'E':5}
dic3 = {**dic1, **dic2}
print(f'Unir diccionarios: {dic3}')

#construir una lista a partir de un str
lista = [*'Hola mundo']
print(lista)
print(*lista, sep='')