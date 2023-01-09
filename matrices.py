#Matrices en Python
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f'Matriz Original: {matriz}')
print(f'Rengoln 0, Columna 0: {matriz[0][0]}')
print(f'Renglon 0, Columna 1: {matriz[0][1]}')
print(f'Renglon 2, Columna 3: {matriz[2][3]}')
matriz[2][0] = 65
print(f'Matriz modificada: {matriz}')

lista_listas = [[10, 15, 54, 65, 44], [3, 4, 5, 6], [3, 5, 7, 44, 34, 34, 22]]
lista_listas.sort(key=len)
print(f'Ordenar lista: {lista_listas}')

#sorted built-in
nombres1 = ['Giancalro', 'Ailed', 'Pedro', 'Esperanza']
nombres1 = sorted(nombres1)
print(nombres1)
#ordenar de manera descentente
nombres1 = sorted(nombres1, reverse=True)
print(nombres1)
#ordenar por la cantidad de caracteres(largo)
nombres1 = sorted(nombres1, key=len)
print(nombres1)

#built in reversed
nombres1 = reversed(nombres1)
print(list(nombres1))