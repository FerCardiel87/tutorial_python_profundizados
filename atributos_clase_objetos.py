class Persona:
    contador_personas = 0

    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

#mostrar los atrivutos de un objeto
persona1 = Persona('Fernando', 'CardielAvila')
print(persona1.__dict__)

#crear un atributo al vuelo
print(persona1.contador_personas) #accediendo al atributo de clase
#pero no es posible modificarlo con el objeto, sino con la clase
persona1.contador_persona = 10
print(persona1.__dict__)
#el atributo anterior oculta al atributo de clase
print(Persona.contador_personas) #atributo clase
print(persona1.contador_persona) #atributo del objeto

#un segundo objeto
persona2 = Persona('Ailed', 'Ramirez')
print(persona2.__dict__)
print(persona2.contador_personas)

#asociar un atributo de clase al buelo
Persona.contador2 = 20
print(Persona.contador2)