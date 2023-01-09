
#help(str.join)

tupla_str = ('Hola', 'Mundo', 'Python')
mensaje = ' '.join(tupla_str)
print(f'mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular', 'C#']
mensaje = ', '.join(lista_cursos)
print(f'mensaje: {mensaje}')

cadena = 'Holamundo'
mensaje = '.'.join(cadena)
print(f'mensaje: {mensaje}')

diccionario = {'nombre': 'Blanqiuta', 'apellido': 'Avila', 'Edad': '55'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'lllaves: {llaves}, type: {type(llaves)}')
print(f'valores: {valores}, type: {type(valores)}')