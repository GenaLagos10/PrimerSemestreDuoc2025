lista_nombres=[]

def agregar_nombres():
    while True:
        nombre=(input("ingrese un nombre (o 'no' para terminar): "))
        lista_nombres.append(nombre)
        if nombre.lower() == "no":
            break
    del lista_nombres[-1]        
agregar_nombres()

print(lista_nombres)