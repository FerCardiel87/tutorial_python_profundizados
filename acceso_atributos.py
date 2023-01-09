#publicos, protegidos, privados

class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

objecto = MiClase('Valor publico', 'Valor protegido', 'Valor privado')
#acceso al atributo publico
print(objecto.publico)
#modificar al valor publico
objecto.publico = 'Nuevo valor publico'
print(objecto.publico)

#acceso al valor protegido
#solo dentro de la misma clase o clases hijas
objecto._protegido = 'Nuevo valor protegido'
print(objecto._protegido)

#acceder al valor privado
# print(objecto.__privado)
#pro convierte: objeto._clase__atributo_privado
print(objecto._MiClase__privado)
#modificar valor privado
objecto._MiClase__privado = 'Nuevo valor privado'
print(objecto._MiClase__privado)
