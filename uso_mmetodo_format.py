nombre = 'Fernnaod'
edad = 60
sueldo = 505000000
# mensaje_con_formato = 'Nombre {} Edad {} sueldop {:.2f}'.format(nombre,edad,sueldo)
# print(mensaje_con_formato)
#
# mensaje= 'Nombre {0} Edad{1} Sueldo {2:.2f}'.format(nombre,edad,sueldo)
# print(mensaje)
#
# mensaje1 = 'Sueldo:{2:.2f} Edad:{1} Nombre:{1}'.format(nombre,edad,sueldo)
# print(mensaje1)
#
# mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
# print(mensaje)

diccionario = {'nombre':'Fernando', 'edad':55, 'sueldo': 55005060.00}
mensaje3= 'Nombre {persona[nombre]} Edad {persona[edad]} Sueldo {persona[sueldo]}'.format(persona=diccionario)
print(mensaje3)