def contar_vocales(texto):

    vocales = "aeiouAEIOU"
    cantidad_vocales = 0

    for i in texto:
        if i in vocales:
            cantidad_vocales+=1

    return cantidad_vocales

frase1 = contar_vocales(input("ingresa tu frase: "))
print(f"tu frase tiene {frase1} vocales")
      
