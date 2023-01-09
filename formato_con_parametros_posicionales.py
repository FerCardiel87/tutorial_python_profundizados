nombre = 'Blanquita'
edad = 55
mensaje_con_formato = 'Mi nombre es %s y tengo %d  años'%(nombre, edad)
print(mensaje_con_formato)

persona = ('Karla', 'Gomez', 5000.44)
mensaje_con_formato = 'Hola %s %s. Tu saldo es: %.2f'%persona
print(mensaje_con_formato)
mensaje_con_formato = 'Hola %s %s. tu saldo es: %.2f'
print(mensaje_con_formato%persona)