from urllib.request import urlopen
palabras = []
with urlopen('https://github.com/Kaiofprates/Cadastro_simples_C/blob/master/dados.txt') as mensaje:
    # contenido = mensaje.read()
    # contenido = mensaje.read().decode('utf-8')
    # print(contenido)

    # for linea in mensaje:
    #     palabras_por_linea = linea.decode('utf-8').split()
    #     print(palabras_por_linea)

    for linea in mensaje:
        palabras_por_linea = linea.decode('utf-8').split()
        for palabra in palabras_por_linea:
            palabras.append(palabra)
print(palabras)