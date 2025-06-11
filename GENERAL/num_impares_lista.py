nums=input("ingresa una lista de numeros separados por espacios: ")
lista=list(map(int, nums.split()))
i=0
lista2=[3, 1]
while i < len(lista):
    if lista[i] % 2 != 0:
        lista2.append (lista[i])
    i=i+1

print("los numeros impares de la lista son: ", lista2)


