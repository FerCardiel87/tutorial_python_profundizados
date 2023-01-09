#clousere es una funcion que defina a ora y ademas la regresa, puede acceder a variables locales definidas, en la funcion o pexternal

#funcion
def operacion(a,b):
    #definimos una funcion iterna o anidada
    def sumar():
        return a + b

    #retornar la funcion
    return sumar

mi_funcion_closure = operacion(5,7)
print(f'Resultado de la funcion closuer: {mi_funcion_closure()}')

#llamar funcion refgresada al vuelo
print(f'Resultado de la funcion closure al vuelo:{operacion(2,3)()}')