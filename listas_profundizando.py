nombres1 = ['Fernando', 'ailed', 'Daniela']
nombres2 = 'Laura Maria Gonzalo enresto'.split()
#sumarlista
print(f'sumar listas {nombres1 + nombres2}')
#extender una lista con otra lista
nombres1.extend(nombres2)
print(f'Extender la lista1 con la lista2 {nombres1}')
#lista de numeros
numeros1 = [10, 40, 13, 34, 23, 45, 33]
#ontener el indice del primer elemento encontrado en un alista
print(f'Lista Original: {numeros1}')
print(f'Indice 4: {numeros1.index(40)}')

#invertir el orden de elementos en una lista
numeros1.reverse()
print(f'Lista invertida: {numeros1}')

#ordenar los leelmentos de la lista
numeros1.sort()
print(f'Lista ordenadad: {numeros1}')

#ordenar de manera descendente
numeros1.sort(reverse=True)
print(f'Ñista orderannada descenten _ {numeros1}')

#obtener el valor min y max de una lista
print(f'Valor minimo: {min(numeros1)}')
print(f'Valor maximo: {max(numeros1)}')

#copiar los elementos de la lista
numeros2 = numeros1.copy()
print(numeros1)
print(numeros2)
print(f'Misma Referencia?: {numeros1 is numeros2}')
print(f'Mismo Contenido? {numeros1 == numeros2}')

#podemos usar el constructor de la lista
numeros2 = list(numeros1)
print(f'Misma Referencia?: {numeros1 is numeros2}')
print(f'Mismo Contenido? {numeros1 == numeros2}')

#Slicing
numeros2 = numeros1[:]
print(f'Misma Referencia?: {numeros1 is numeros2}')
print(f'Mismo Contenido? {numeros1 == numeros2}')

#multiplicacion listas
listA_multiplicacion = 5*[[2, 5]]
print(listA_multiplicacion)
print(f'Misma referencia_ {listA_multiplicacion[0] is listA_multiplicacion[1]}')
print(f'Misma contenido_ {listA_multiplicacion[0] is listA_multiplicacion[1]}')
listA_multiplicacion[2].append(10)
print(listA_multiplicacion)
listA_multiplicacion[3].append(11)
print(listA_multiplicacion)

