numeros = [12, -7, 0, 25, 8, -3, 10, 1]

pares=[]
impares=[]
par_mayores10=[]
par_menorde10=[]
impar_menores10=[]
impar_mayorde10=[]

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
        if num >= 10:
            par_mayores10.append(num)
        else:
            par_menorde10.append(num)


    else:
        impares.append(num)
        if num < 10:
            impar_menores10.append(num)
        else:
            impar_mayorde10.append(num)

print(numeros)
print(pares)
print(impares)
print(par_mayores10)
print(par_menorde10)
print(impar_mayorde10)
print(impar_menores10)

