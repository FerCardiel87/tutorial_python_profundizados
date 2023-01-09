#expresion generadora (es un generador anonumo)

multiplicacion = (valor*valor for  valor in range(4))
print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

#ta,boem se íede ásar ima expresion generadora a una funcion (sin parentesir)
import math
suma = sum(valor*valor for valor in range(4))
print(f'Resultado suma: {suma}')

#tambien podemos usar una lista o cualquier iterator
lista = ['Fernando','CardielAvila']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

#crear un string a partir de un generador creado a partir de una lista
lista = ['Ailed', 'Ramirez', 33]
contador = 0
#definimos una funcion para incrementar el contador
def incrementar():
    global contador
    contador += 1
    return contador
#la primera para es el yield , la segunda es el flor, entre parentesis
generador = (f'{incrementar()}.{nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'Cadena generadA: {cadena}')