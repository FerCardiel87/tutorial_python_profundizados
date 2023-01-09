#operaciones de conjuntos con set, personas con distintas caracteristicas
pelo_negro = {'Fernando', 'Liliana', 'Pedro', 'Ailed'}
pelo_rubio = {'Lorenzo', 'Laura', 'marco'}
ojos_cafes = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'maria'}
#rpeguntar si un set esta contenido en otro subset
print(menores_30.issubset(pelo_negro))

#preguntar si un set contiene a otro set
print(menores_30.issuperset(pelo_negro))

#disjoint
print(pelo_negro.isdisjoint(pelo_rubio))