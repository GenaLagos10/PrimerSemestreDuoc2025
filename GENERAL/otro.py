num=input("ingresa una lista de numeros separados por espacios: ")

lista=list(map(int, num.split()))

mayor=0

for i in lista:
    if max(lista):
        mayor=max(lista)

print("el numero mayor de la lista es:", mayor)