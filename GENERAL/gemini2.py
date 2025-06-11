import random

while True:
    num1=int(input("ingrese un numero entero como el umbral inferior: "))
    num2=int(input("ingrese un numero entero como el umbral superior: "))

    if num1 >= num2:
        print("el primer numero debe ser menor al segundo")
        continue
    else:
        break

numero_secreto1=random.randint(num1, num2)
numero_secreto2=random.randint(num1, num2)

producto=(numero_secreto1*numero_secreto2)
producto_ajustado=producto//3


print(f"tienes 3 intentos para adivinar el valor entre 1 y {producto_ajustado}")

#primer intento

numero_usuario1=int(input("ingrese un numero entero para adivinar el valor: "))

if numero_usuario1 == producto_ajustado:
    print("increible! acertaste a la primera")
elif numero_usuario1 > producto_ajustado:
    print("Ups...te pasaste")
elif numero_usuario1 < producto_ajustado:
    print("Ups...te faltó")

#segundo intento

numero_usuario2=int(input("ingrese un numero entero para adivinar el valor: "))

if numero_usuario2 == producto_ajustado:
    print("increible! acertaste")
elif numero_usuario2 > producto_ajustado:
    print("Ups...te pasaste")
elif numero_usuario2 < producto_ajustado:
    print("Ups...te faltó")

#tercer y ultimo intento

numero_usuario3=int(input("ingrese un numero entero para adivinar el valor: "))

if numero_usuario3 == producto_ajustado:
    print("increible! acertaste a la primera")
elif numero_usuario3 > producto_ajustado:
    print("Ups...te pasaste")
elif numero_usuario3 < producto_ajustado:
    print("Ups...te faltó")


print(f"se acabaron los intentos...has perdido...el numero secreto era {producto_ajustado}")