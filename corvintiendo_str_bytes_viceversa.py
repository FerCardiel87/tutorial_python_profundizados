string = 'Programacion de Python'
print('string original', string)

bytes = string.encode('UTF-8')
print('byutes codificado: ', bytes)

string2 = bytes.decode('UTF-8')
print('String decodificado:', string2)
print(string == string2)
