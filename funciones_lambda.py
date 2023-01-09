#no es posible asignar una funcion a una varibale
#mi_funcion = def sumar(a,b):
 #   return a + b

 #con una funcion lambda (anonima sin nombre y una sola linea de codigo, no se necesita agregar parentesis para los parametros
 #no se necesita usar la palara return,ppero si debe regresar una expresion
mi_funcion_lambda= lambda a, b: a + b

resultado = mi_funcion_lambda(4,5)
print(f'Resultado sumar con fuuncion lambda: {resultado }')

#no recibe argumentos
mi_funcion_lambda = lambda: 'funcion sin argumentos'
print(f'LLmaar funcion lambda sin argumentos: {mi_funcion_lambda()}')

#funcion lambda con parametros por default
mi_funcion_lambda = lambda a=2, b=3: a + b
print(f'Resultado argumentos por default: {mi_funcion_lambda(4,6)}')

#funcion lambda ocn argumentos variables **argsa y ***kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado argumentos variables111: {mi_funcion_lambda(1,2,3, a= 5, b= 6)}')

#fuciones lambda con argumentos, argumentos variables y valores por default
mi_funcion_lambda = lambda  a, b, c=3, *args, **kwargs: a+b+c+len(args)+len((kwargs))
print(f'Resultado funcion lambd3232a {mi_funcion_lambda(1,2,3,4,5,6,7, e= 5, f=7)}')