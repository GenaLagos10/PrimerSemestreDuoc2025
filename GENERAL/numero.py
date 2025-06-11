import random

def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanza de números!")
    print("Piensa en un número entre 1 y 100.")
    
    # Número secreto aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    intentos = 0
    adivinado = False
    
    # Bucle hasta que el usuario adivine el número
    while not adivinado:
        # Pide al usuario que ingrese su adivinanza
        adivinanza = int(input("Introduce tu adivinanza (un número entre 1 y 100): "))
        intentos += 1
        
        # Compara la adivinanza con el número secreto
        if adivinanza == numero_secreto:
            print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
            adivinado = True
        elif adivinanza < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")
            # Iniciar el juego
juego_adivinanza()