lista=list(map(int, input("ingresa numeros separados por espacios: ").split()))

numX=int(input("ingresa un numero X que servirá de umbral: "))
i=0
lista2=[]
suma=0

while i < len(lista):
    if lista[i]>numX:
        lista2.append(lista[i])
        suma=suma+lista[i]
    i=i+1

print(f"cantidad de numeros: {len(lista2)}. los numeros son: {lista2}. y todos juntos suman: {suma}")







