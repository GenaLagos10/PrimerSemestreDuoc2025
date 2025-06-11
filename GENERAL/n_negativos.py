nums=input("ingresa una lista de numeros negativos y positivos")
lista=list(map(int, nums.split()))
i=0
lista2=[]
suma=0
while i < len(lista):
    if lista[i]<0:
        lista2.append(lista[i])
        suma=suma+lista[i]
    i+=1

print(f"la cantidad de numeros negativos son: {len(lista2)} y son: {lista2}. Además, sumados dan: {suma}")


