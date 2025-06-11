primos=0
no_primos=0

while True:
    try:
        cantidad_codigos=int(input("ingresar la cantidad de codigos a evaluar: "))

        if cantidad_codigos > 0:
            print("ingreso válido")
            break
        else:
            print("ingrese un numero valido")
            continue
    except ValueError:
        print("ingrese un numero valido")

contador=0
while contador < cantidad_codigos:
    numero=int(input("ingrese un numero para saber si es primo o no: "))
    es_primo=True
    try:
        if numero ==1:
            es_primo=False
            
        elif numero==2:
            es_primo=True
        else:
            for i in range(2, numero):
                    
                if numero % i == 0:
                    es_primo=False
                    break

        if es_primo:
            print("Código válido")
            primos+=1
        else:
            print("Código inválido")
            no_primos+=1
        contador+=1
    except ValueError:
        print("ingresa un valor valido")
        
print(f"la cantidad de numeros primos es {primos}")
print(f"la cantidad de numeros no primos es {no_primos}")