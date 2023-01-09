from urllib.request import Request
from urllib.request import urlopen

import json

request = Request("http://globalmentoring.com.mx/api/clima.json")
# Añadir la cebecera User-Agent a la peticion
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')
respuesta = urlopen(request)
cuerpo_respuesta = respuesta.read()
# Procesamos la respuesta json
json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))
#print(json_respuesta)
#ejercicio1 Acceder a la descripcion del clima
#descripcion_clima = json_respuesta.get('clima')[0].get('descripcion')
descripcion_clima = json_respuesta['clima'][0]['descripcion']
print(f'Descripcion clima: {descripcion_clima}')
#ejercicio2 Mostrar emperatura minima y maxima
temp_min = json_respuesta.get('principal').get('temp_min')
print(f'Temperatura minima: {temp_min}')
temp_max = json_respuesta.get('principal').get('temp_max')
print(f'Temperatura maxima: {temp_max}')