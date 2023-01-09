#first class ctizens

#definimos la funcion
def sumar(a,b):
    return a + b
#asignnar una funcion a una variable (no se usan parentesis)
mi_funcion = sumar

#verificar el tipo de variable
print(type(mi_funcion))

#llamamos la funcion a traves de la variavble
resultado = mi_funcion(5,8)
print(f'Resultado: {resultado}')

#2 funcion como argumento
def operacion(a,b, sumar_arg):
    print(f'Resultado synar: {sumar_arg(a,b)}')

operacion(4, 5, sumar)

#3 podemos retornar una funcion
def retornar_funcion():
    #retornamos una funcion
    return sumar

mi_funcion_retornada = retornar_funcion()
print(f'Resultado funcion retornada_ {mi_funcion_retornada(5,7)}')