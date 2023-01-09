#un set es un acoleccion de elementos unicos y es mutable

conjunto = {'Fernando', True, 16.2}
print(conjunto)
#set vacio
conjunto = {}
print(type(conjunto))
#set vacio correcto
conjunto = set()
print(conjunto)
print(type(conjunto))
#mutable
conjunto.add('Fern')
print(conjunto)
print(type(conjunto))
#contiene valores unicos
conjunto.add('Fernandpo')
print(conjunto)
#crear set a partid eun iterable
conjunto = set([4,5,6,3,2])
print(conjunto)
#pdemos agrgar mas elementos on incluso otro set
conjunto2 = {100,200,300,400}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([30,20,40,20])
print(conjunto)

#copiar un set(copia poco profunda, solo copia freferencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
#verificar igualdad
print(f'Es igual en contenido? {conjunto == conjunto_copia}')
print(f'Es la misma referencia? {conjunto is conjunto_copia}')

#operaciones de conjuntos con set, personas con distintas caracteristicas
pelo_negro = {'Fernando', 'Liliana', 'Pedro', 'Ailed'}
pelo_rubio = {'Lorenzo', 'Laura', 'marco'}
ojos_cafes = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'maria'}
#todos con ojos cafe y pelo rubio (union) ( no se repiten los elementos
print(ojos_cafes.union(pelo_rubio))
#invertir el orden con el mismo resultado (conmutativo)
print(pelo_rubio.union(ojos_cafes))

#interseccion
print(ojos_cafes.intersection(pelo_rubio))

#differencia
print(pelo_negro.difference(ojos_cafes))

#diferencia simetrica
print(pelo_negro.symmetric_difference(ojos_cafes))