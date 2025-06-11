import random

#bucle para pedir numeros al usuario

while True:
    num1=int(input("ingrese el numero correspondiente al umbral inferior: "))
    num2=int(input("ingrese el segundo numero correspondiente al umbral superior: "))

    if num1 >= num2:
        print("el primer numero debe ser menor que el segundo")
        continue
    else:
        break

#obtencion de numero al azar entre los rangos

aleatorio=random.randint(num1, num2)
adivina=int(aleatorio//4)

print(adivina)

#primer intento
numero_usuario=int(input("ingresa tu numero, tienes 3 posibilidades para adivinar: "))

if numero_usuario > adivina:
    print("Ups...te pasaste")
elif numero_usuario < adivina:
    print("Ups...te faltó")
elif numero_usuario==adivina:
    print("correcto! adivinaste a la primera")
    
    
#segundo intento
numero_usuario2=int(input("ingresa tu numero, tienes 2 posibilidades para adivinar: "))

if numero_usuario2 > adivina:
    print("Ups...te pasaste")
elif numero_usuario2 < adivina:
    print("Ups...te faltó")
elif numero_usuario2==adivina:
    print("correcto! el numero secreto era {adivina}")
    
#tercer intento 
numero_usuario3=int(input("ingresa tu numero, tienes 1 posibilidades para adivinar: "))

if numero_usuario3 > adivina:
    print("Ups...te pasaste")
elif numero_usuario3 < adivina:
    print("Ups...te faltó")
elif numero_usuario3==adivina:
    print("correcto! el numero secreto era {adivina}")

else:
    print(f"perdiste...el numero secreto era: {adivina}")
    