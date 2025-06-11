
def analizar_numeros(lista_de_numeros):
    suma= sum (lista_de_numeros)
    promedio = suma / len (lista_de_numeros)
    mas_alto = max (lista_de_numeros)
    mas_bajo = min (lista_de_numeros)

    return suma, promedio, mas_alto, mas_bajo

lista_de_ejemplo= [3, 5, 7, 9, 12, 13]

suma, promedio, mas_alto, mas_bajo= analizar_numeros(lista_de_ejemplo)

print(f"Lista: {lista_de_ejemplo}")
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
print(f"Número más grande: {mas_alto}")
print(f"Número más pequeño: {mas_bajo}")

lista_ejemplo2= [1, 5, 15, 32, 66, 78, 42, 19]

suma, promedio, mas_alto, mas_bajo= analizar_numeros(lista_ejemplo2)

print(f"Lista: {lista_ejemplo2}")
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
print(f"Número más grande: {mas_alto}")
print(f"Número más pequeño: {mas_bajo}")
