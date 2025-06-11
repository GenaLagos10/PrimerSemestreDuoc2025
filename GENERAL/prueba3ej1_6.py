#variables principales
masde10=0
menosde10=0

#numero de empleados a ingresar
while True:
    try:
        numero_empleados=int(input("ingrese el numero de empleados: "))

        if numero_empleados > 0:
            print(f"ud ha ingreasado: {numero_empleados} empleados")
            break
        
        else:
            print("ingrese un valor valido")
            continue
    except ValueError:
        print("ingrese un valor valido")

#bucle while para nombre y años trabajados
contador=0
while contador < numero_empleados:
    try:
        nombre=input("ingrese su nombre: ")
        ages=int(input("ingrese sus años trabajados: "))
        if ages >10:
            print("Más de 10 años de antiguedad")
            masde10+=1
        elif ages >-1 and ages < 11:
            print("10 o menos años de antiguedad")
            menosde10+=1
        else:
            print("ingrese un valor valido")
        contador+=1    
    except ValueError:
        print("ingrese un valor valido")
    

print(f"los empleados con mas de 10 años de antiguedad son: {masde10}")
print(f"los empleados con 10 o menos años de antiguedad son: {menosde10}")

