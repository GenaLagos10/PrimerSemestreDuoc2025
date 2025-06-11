lista=list(map(int, input("ingrese una lista de numeros separados por espacios").split()))

lista2=[]
multi=1
i=0

while i < len(lista):
    if lista[i] > 10:
        lista2.append(lista[i])
        multi=multi * lista[i]

    i+=1

print(f"los cantidad de numeros mayores a 10 son: {len(lista2)}; los numeros son: {lista2}. y multiplicados dan: {multi}")