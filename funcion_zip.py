# print(dir(__builtins__))
# help(zip)

numeros = [1,2,3]
letras = ['a', 'b', 'c', 'd']
identificadores = 321, 322, 323, 324, 325
conjunto = {6,4,0,8,0,14}
mexcla = zip(numeros, letras, identificadores, conjunto)
# print(mexcla)
print(list(mexcla))
# print(tuple(zip(numeros,letras)))
# print(type(mexcla))

#iterar en paralelo
for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    print(f'Numero: {numero}, Letra: {letra}, Id: {id}, Aleatorio: {aleatorio}')

nueva_lista = []
for numero, letra, id, aleatorio in zip (numeros, letras, identificadores, conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
print(nueva_lista)

#unzip
mezcla = [(1,'a'), (2, 'b'),(3,'c')]
numeros, letras = zip(*mezcla)
print(f'Numeros: {numeros}, Letras: {letras}')

#ordenamiento usando ZIP
letras = ['c', 'd', 'a', 'e', 'b']
numeros = [3,2,1,4,0]
mezcla = zip(letras, numeros)
#sin orden
print(tuple(mezcla))
#ordenar por letra (primer iterable)
print(sorted(zip(numeros, letras)))

# crear un diccionario con zip y dos iterables
llaves = ['Nombre', 'apellido', 'edad']
valores = ['Fernando', 'CardielAvila', 33]
diccionario = dict(zip(llaves, valores))
print(diccionario)

llave = ['edad']
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)