import random

#entradas

while True:
    rango1=int(input("ingrese un valor para el rango inferior en numeros enteros: "))
    rango2=int(input("ingrese un valor para el rango superior en numeros enteros: "))

    if rango1 >= rango2:
        print("el segundo valor debe ser mayor que el primero")
        continue
    else:
        break

adivina=random.randint(rango1, rango2)
ajuste=adivina // 4
adivina2=random.randint(adivina-ajuste, adivina+ajuste)


#juego

intentos_maximos= 3

for i in range (1, intentos_maximos +1):
    intentos_restantes = intentos_maximos - i + 1
    numero_usuario=int(input(f"ingresa el numero a adivinar, tienes {intentos_restantes} posibilidades: "))

    if numero_usuario==adivina2:
        if i == 1:
            print("WENA! adivinaste a la primera!!")
            break
        else:
            print("Wena, adivinaste!")
            break
    if numero_usuario > adivina2:
        print("te pasaste...")
    
    elif numero_usuario < adivina2:
        print("te quedaste corto...")

else:
    print(f"perdiste...el numero secreto era {adivina2}")





