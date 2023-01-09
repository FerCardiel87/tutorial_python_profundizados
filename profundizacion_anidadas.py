def calculadora(a,b, operacion='sumar'):
    #funcon anidada
    def sumar(a, b):
        return a + b

    def resta(a,b):
        return a - b

    #llamamos la funcion anidada
    if operacion == 'sumar':
        print(f'Resultado sumar_ {sumar(a,b)}')
    elif operacion == 'restar':
        print(f'Resultado resta_ {resta(a, b)}')


calculadora(5, 6)
calculadora(4, 5, operacion='restar')