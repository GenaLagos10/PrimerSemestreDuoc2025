
lista_par=[]
lista_impar=[]


def validar_lista_numeros():
    while True:
        lista=list(map(int, input("ingresa numeros enteros positivos separados por espacio: "). split()))
        return lista
    
def clasificar_numeros(lista):

    for numero in lista:
        if numero %2==0:
            lista_par.append(numero)
        elif numero %2 != 0:
            lista_impar.append(numero)

lista_principal=validar_lista_numeros()
clasificar_numeros(lista_principal)
            
print(lista_par)
print(lista_impar)