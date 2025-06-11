numeros=input("ingresa una lista de numeros separados por espacios: ")

lista=list(map(int, numeros.split()))

contador_suma=0
contador=0
for i in lista:
    if i > 10:
        contador_suma+=i
        contador=contador+1
        

promedio=contador_suma / contador

print(f"el promedio final es de: {promedio}")












   
















