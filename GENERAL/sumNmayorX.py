nums=input("digita la lista de numeros separados por un espacio: ")
lista=list(map(int, nums.split()))
i=0
suma=0
numX=int(input("ingresa un numero entero"))

while i < len(lista):
    if lista[i] > numX:
        suma=suma + lista[i]
    i=i+1

print(f"la suma de los numeros mayores que X es: {suma}")

