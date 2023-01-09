#generador de numeros del 1 a 5
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('Se reanunda la ejecucion de la funcion')

#utilizamos el generador
generador = generador_numeros()
print(f'Objeto generador: {generador}')
print(type(generador))

#cponsumimos los valores del generador
for valor in generador:
    print(f'Numero producido: {valor}')

#consumir a demanda,
generador = generador_numeros()
try:
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
except StopIteration as e:
    print(f'Error al consumir generador: {e}')

#otra forma de consumir un generador
generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print(f'Impresion valor generado_ {valor}')
    except StopIteration as e:
        print('Se termino de iterar el generador')
        break