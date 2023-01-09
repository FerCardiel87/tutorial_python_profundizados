#declarar variables
a, b = 'Hola', 'Adios'
print(a,b)
#swap(intercambio)
a, b = b, a
print(a,b)

#regresar mulktiples valores en una funcion
def minmax(elementos):
    return  min(elementos), max(elementos)

min, max = minmax([1,2,3,4,5])
print(f'Valor min: {min}, Valor max: {max}')

#regresa ,la suma de una tupla  
resultado = sum((1,2,3,4,5))
print(f'Resultado: {resultado}')

def sumar(*args):
    return sum(args)

resultado = sumar(1,2,3,4,5)
print(f'Resultado: {resultado}')