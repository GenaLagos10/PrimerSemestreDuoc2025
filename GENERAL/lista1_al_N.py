num=int(input("ingresa un numero natural: "))
i=0
lista=[]
while i < num:
    if i % 2 !=0 and i % 3 !=0:
        lista.append(i)
    i=i+1

print(f"los numeros no divisibles ni por 2 ni por 3 de la lista menores a {num}, son: {lista}")

