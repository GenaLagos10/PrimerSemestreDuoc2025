num=input("ingresa una lista de numeros enteros separados por espacio:")
lista=list(map(int, num.split()))
i=0
lista2=[]
while i < len(lista):
    if lista[i] % 2==0:
        lista2.append(lista[i])
    i+=1

print("los numeros pares de la lista son", lista2)
print("los numeros pares son", len(lista2))
