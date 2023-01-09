from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int=0

@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor nombre vacio: {self.nombre}')

domicilio1 = Domicilio('Saturno', 15)
persona1 = Persona('Fernando', 'Cardiel', domicilio1)
print(persona1)
print(f'{persona1!r}')
#variable de clase
print(f'Variable clase: {Persona.contador_personas}')
#Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}')
#variable con valores vacios
persona_vacia = Persona('Ailed','', None)
print((f'Persona vacia: {persona_vacia}'))
#revisar igualdas entre objetpos (__eq__)
persona2 = Persona('Fernando', 'Cardiel', Domicilio('Saturno', 15))
print(f'Objetos iguales?: {persona1 == persona2}')
#agregar esta clase a una colecciones
coleccion = {persona1, persona2}
print(coleccion)
# forzen = True
# coleccion[0].nombre='Fernandito'
# persona1.nombre = 'Fernandito'