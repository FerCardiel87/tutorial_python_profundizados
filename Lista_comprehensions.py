numeros = range(10)
lista_pares = []

#creamos una nueva lista con los valores pares multiplicados por si mismos
for numero in numeros:
    #revisamos si es un numero par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)

print(f'Lista PareS: {lista_pares}')

#hacemos lo mismo pero con List compreghensiones, [expresion for vr in colecion if condicion], condicion de if es opcional
lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero % 2 == 0]
print(f'Lista PareS con list comprehension: {lista_pares}')

#un ejemplo simila con dos conficiones (las condiciones son opcionales)
#solo se agrega el valor a la lista cuando el valor cumple ambas condificiones
#es decir, debe ser divisible entre 2 y divisible entre 6
pares = [numero for numero in range(50) if numero%2==0 if numero%6==0]
print(f'Lista divisible entre 2 y 6: {pares}')

#agregando if else
lista_pares = []
lista_impares = []
for numero in range(10):
    if numero%2==0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

#el mimso ejercicio usando list compregensions
lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero%2 == 0 else lista_impares.append(numero) for numero in range(10)]
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

#lista de listas
lista_listas = [[1,2,3],[4,5,6],[7,8,9,10]]
#convertimos la lista de listas en una sola lista
lista_simple = [valor for sublista in lista_listas for valor in sublista]
print(f'lista simple_ {lista_simple}')

#ahora cramos una lista de numeros pares a partir de la lista_listas, sin list compregension, ciclos for anidados
lista_pares = []
for sublista in  lista_listas:
    for valor in sublista:
        if valor%2 == 0:
            lista_pares.append(valor)
print(f'Lista pares: {lista_pares}')

#con list compregension, en una sola linea de codigo, no es necesario separar las lineas, solo mejor lectura de codigo
lista_pares = []
lista_pares = [valor for sublista in lista_listas for valor in sublista if valor%2==0]
print(f'Lista pares: {lista_pares}')