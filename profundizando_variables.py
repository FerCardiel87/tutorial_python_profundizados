var_global = 'Variable global'
def imprimir():
    # Acceder a una variable global
    global var_global
    print(f'Variable global desde función: {var_global}')
    # Definición de variable local
    var_local = 'Variables local'
    print(f'Variable local desde función: {var_local}')
    var_global = 'Nuevo valor variable global'

    def funcion_anidada():
        print(f'Variable local dentro funcion anidada: {var_local}')

    funcion_anidada()

imprimir()
print(f'Var global fuera funcion_ {var_global}')
#no es pposible acceder variable locales fura del bloque donde se definieron
# print(f'Var local duera funcion: {var_local}')