num=input("ingresa una lista de numeros separados por espacios: ")
lista=list(map(int, num.split()))
i=0
lista2=[]
while i < len(lista):
    if lista[i] % 2 !=0:
        lista2.append(lista[i])
    i+=1

print(f"los numeros impares de la lista son: {lista2}")
