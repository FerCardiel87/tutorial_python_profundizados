#decorador es una funcion que recibe una funcion y regresa otra, y utlizamos para extender
#funcion decorador (A)
#funcion a decorar(b)
#funcion decorada (c)
def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print('Antes desde la funcion_Decorada_c')
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print('Despues desde la funcion decorada_c')
        return resultado
    return funcion_decorada_c

#definimos una funcion y vamos a extender su fincionalidad con un decorador
@funcion_decorador_a
def sumar(a, b):
    return a + b

resultado = sumar(5, 6)
print(f'Resultado suma: {resultado}')