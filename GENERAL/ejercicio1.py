def multiplo_de_3(numero):
    if numero % 3 == 0:
        return True
    else:
        return False

numero = int(input("Introduce un numero para saber si es o no multiplo de 3: "))
if multiplo_de_3(numero):
    print(f"{numero} es multiplo de 3")
else:
    print(f"{numero} no es multiplo de 3")