# help(str.split)}

cursos = 'java ppython javascript angular spring excel'
lista_cursos = cursos.split()
print(f'Lista cursos: {lista_cursos}')
print(type(lista_cursos))

cursos_separados_coma = 'Java, Python, Javascript, angular, spring, excel'
lista_cursos = cursos_separados_coma.split(', ')
print(f'Lista cursos: {lista_cursos}')
print(len(lista_cursos))

lista_cursos = cursos_separados_coma.split(', ', 2)
print(f'Lista cursos: {lista_cursos}')
print(len(lista_cursos ))