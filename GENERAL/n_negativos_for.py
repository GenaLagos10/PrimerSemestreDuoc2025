nums=input("ingresa una lista de numeros negativos y positivos")
lista=list(map(int, nums.split()))
lista2=[]
suma=0

for i in lista:
    if i < 0:
        lista2.append(i)
        suma=suma+i

print(f"la cantidad de numeros negativos son: {len(lista2)} y son: {lista2}. Además, sumados dan: {suma}")