lista=[]
sum=0

numero=int(input("ingresa la la cantidad de numeros"))

while len(lista) < numero:
    valor=int(input("ingresa un numero:"))
    if valor % 2 ==0:
        sum+=valor
    lista.append(valor)

print(f"la suma de los numeros pares es {sum}")