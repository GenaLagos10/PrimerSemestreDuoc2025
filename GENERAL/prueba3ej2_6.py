#variables
entradas_restantes=100

# while y print
while True:
    print("***** Cine Estrella *****")
    print()
    print("Bienvenido al sistema de venta de entradas del Cine Estrella")
    print()
    print("1.- Ver cuántas entradas quedan.")
    print("2.- Comprar una cantidad de entradas.")
    print("3.- Cargar entradas.")
    print("4.- Salir de sistema.")
    print()
    try:
        opcion=int(input("ingrese una opcion válida: "))

        if opcion ==1:
            print(f"las entradas restantes son {entradas_restantes}")

        elif opcion ==2:
            
            comprar=int(input("Ingrese la cantidad de entradas que desea comprar: "))
            if comprar <= entradas_restantes:
                print("Compra exitosa!")
                entradas_restantes=entradas_restantes-comprar
            else:
                print(f"Quedan solo {entradas_restantes} entradas disponibles ¿Cuantas desea?")
            
        elif opcion ==3:
            cargar=int(input("Ingresa las cantidad de entradas a cargar: "))
            entradas_restantes=entradas_restantes+cargar
        elif opcion ==4:
            print("Gracias. Hasta pronto!!")
            break
    except ValueError: 
        print("ingrese un valor válido")