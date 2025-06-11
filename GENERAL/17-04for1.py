lista=list(map(int, input("ingresa una lista de numeros enteros separados por espacios: ").split()))
suma=0
lista2=[]

for i in lista:
    if i % 2 == 0:
        lista2.append(i)
        suma+=i

print(f"la lista de numeros pares es:{sorted(lista2)}. la cantidad de numeros pares es: {len(lista2)} y la suma de ellos es: {suma}")



