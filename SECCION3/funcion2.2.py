def saludar_persona(nombre):
    return (f"Hola {nombre}. Bienvenido/a al programa")

def sumar_dos_numeros(numero1, numero2):
    sumar= numero1 + numero2
    return sumar

def main():
    print()
    print("¡Vamos a saludarte!")
    print()
    nombre=input("ingresa tu nombre: ")
    mensaje_saludo=saludar_persona(nombre)
    print(mensaje_saludo)
    while True:
        print("\n--- Ahora vamos a sumar dos números ---")
        print()
        try:
            num1=int(input("ingresa un numero: "))
            num2=int(input("ingresa el otro numero: "))
            suma_ambos=sumar_dos_numeros(num1, num2)
            print(f"la suma de ambos numeros es: {suma_ambos}")
            
        except ValueError:
            print("ingrese un numero valido")
        break
           
                
if __name__ == "__main__":
    main()
    