num=int(input("ingresa un numero entero"))
lista=[]
i=0

while i < num:
    lista.append(i)
    i=i+3

print(f"los numeros multiplos de 3 menos que {num} son: ", lista)
