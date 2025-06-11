import random

dificultad=input("ingresa nivel de dificultad (facil/medio/dificil)")


while True:
    if dificultad== "facil":
        secreto=random.randint(1, 10)
        print("tienes 3 intentos para adivinar el numero correcto entre 1 y 10")
        break
    elif dificultad == "medio":
        secreto=random.randint(1, 20)
        print("tienes 3 intentos para adivinar el numero correcto entre 1 y 20")
        break
    elif dificultad=="dificil":
        secreto=random.randint(1, 30)
        print("tienes 3 intentos para adivinar el numero correcto entre 1 y 30")
        break
    else:
        ("ingrese una dificultad valida")
        continue

#intento1
numero_usuario=int(input("ingresa un numero: "))
if secreto==numero_usuario:
    print("BIEN! has acertado")
elif secreto > numero_usuario:
    print("ups...te faltó")
elif secreto < numero_usuario:
    print("ups, te pasaste...")

#intento2
numero_usuario2=int(input("ingresa un numero: "))
if secreto==numero_usuario2:
    print("BIEN! has acertado")
elif secreto > numero_usuario2:
    print("ups...te faltó")
elif secreto < numero_usuario2:
    print("ups, te pasaste...")

#comparacion intento 1 y 2
numero_usuario=abs(numero_usuario-secreto)
numero_usuario2=abs(numero_usuario2-secreto)

if numero_usuario < numero_usuario2:
    print("tu primer intento estuvo mas cerca")
elif numero_usuario > numero_usuario2:
    print("tu segundo intento estuvo mas cerca")

#intento3
numero_usuario3=int(input("ingresa un numero: "))
if secreto==numero_usuario3:
    print("BIEN! has acertado")
elif secreto > numero_usuario3:
    print("ups...te faltó")
elif secreto < numero_usuario3:
    print("ups, te pasaste...")


  
print(f"el numero secreto era {secreto}")