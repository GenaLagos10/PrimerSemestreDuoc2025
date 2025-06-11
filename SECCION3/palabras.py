def busca_palabras(texto, palabra):

    contador_palabra= 0
    palabras_en_texto = texto.split()

    for i in palabras_en_texto:
        if i == palabra:
            contador_palabra+=1

    return contador_palabra

texto1 = busca_palabras ("Hola Hola como te va va va va va va amigo mio", "va")
print(texto1) 


