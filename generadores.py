#es una funcion, retorna una secuancia de valores, suspende la ejecion de funcion yield(producir) no se usa return
def generador():
    yield 1
    print('Se reanuda la ejecucion')
    yield 2
    print('Se reanunda la ejecucion')
    yield 3

#consumimos el generador a demanda
gen = generador()
#con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
#si tratamos de consumor mas valores de lo que produce el fggenerador, lanzara un error STOPITERATION

#consumiendo los valores del generador con un ciclo for
for valor in generador():
    print(f'Numero generado: {valor}')