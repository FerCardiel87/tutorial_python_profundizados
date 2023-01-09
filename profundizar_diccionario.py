diccionario = {'Nombre': 'Fernando', 'Apelido': 'CardiellAvila', 'Edad': 30}
print(diccionario)

#si son mutables pero las llabes deben ser muytables
diccionario = {(1,2): 'Valor1'}
print(diccionario)

#se aagrega una llave si no se encuentra
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

#no hay valores duplicados en las llaves d eun diccionariio
diccionario['Nombre'] = 'Fernando Cardiel Avila'
print(diccionario)

#recuperar un valor indicando una llave
print(diccionario['Nombre'])

#si nno encuentra la llvave que lanza una excepcion
# print(diccionario['nombre'])

#metodo get recupera una llave, si no existe NO lanza excepcion, ademas podemos regresar un valor en caso que no exista la llave
print(diccionario.get('Nombres', 'No se encontro la llave'))

#setdefault si moficia el diccionario, ademas se agrega un valor por default
nombre = diccionario.setdefault('Nombre', 'Valor por default')
print(nombre)
print(diccionario)

#imprimir con pprint
from pprint import pprint as pp
pp(diccionario, sort_dicts=False)
