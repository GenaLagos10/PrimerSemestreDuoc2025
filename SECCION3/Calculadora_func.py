#menu de calculadora
#funciones def
#repeticion para el menu
#try except
import time
#1er paso creacion de funciones

def sumar(num1, num2):
    resultado_suma = num1 + num2
    return (resultado_suma)

def restar(num1, num2):
    resultado_resta=num1-num2
    return (resultado_resta)

def multi(num1, num2):
    resultado_multi=num1*num2
    return (resultado_multi)

def divi(num1, num2):
    try:
        resultado_divi=num1/num2
        return (resultado_divi)

    except ZeroDivisionError:
        print("No se puede dividir por 0")
        time.sleep(3)

#no recibe argumentos ni retorna nada...
def mostrar_menu():

    print("=============================")
    print("    ***MENU CALCULADORA***   ")
    print("=============================")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("3.- Dividir")
    print("5.- Salir")

#funcion def que no recibe argumentos pero si retorna
def obtener_numeros():
    while True:
        try:

            num1=int(input("ingrese el primer numero a operar: "))
            num2=int(input("ingrese el segundo numero a operar: "))
            return (num1, num2)

        except ValueError:
            print("se ha ingresado un caracter no valido")
            time.sleep(3)

def main():
    while True:
        mostrar_menu()

        try:
            op = int(input("Ingrese una opcion de 1 a 5: "))


        except ValueError:
            print("Error. Ingrese un valor valido")
            time.sleep(3)

        if (op < 1) or (op > 5):
            print("Error. Ha ingresado una opcion no valida")
            time.sleep(3)
        
        #cuando la opcion ingresada sea entre 1 y 4
        #ingresa al codigo interno def if
        if op in [1,2,3,4]:
            #guardar en las variables num1 y num2 lo que esta retornando
            #la funcion obtener_numeros()
            num1, num2 = obtener_numeros()

            if op ==1:
                resultado= sumar(num1,num2)
                print(f"el resultado de la suma es: {resultado}")
                time.sleep(2)
            if op ==2:
                resultado= restar(num1,num2)
                print(f"el resultado de la resta es: {resultado}")
                time.sleep(2)

            if op==3:
                resultado= divi(num1,num2)
                print(f"el resultado de la division es: {resultado}")
                time.sleep(2)

            if op ==4:
                resultado= multi(num1,num2)
                print(f"el resultado de la multiplicacion es: {resultado}")
                time.sleep(2)
        if op==5:
            print("Gracias. Chau")
            exit()

main()