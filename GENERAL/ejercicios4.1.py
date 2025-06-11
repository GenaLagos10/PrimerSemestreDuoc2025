
#pedimos al usuario los datos del quintil y situación laboral

quintil=int(input("A continuación ingrese el quintil al que pertenece (del 1 al 5): "))
c_laboral=int(input("Si tiene empleo ingrese '1' si no tiene empleo ingrese '2': "))
age=int(input("a continuación ingrese su edad: "))

#quintil 1 y 2

if (quintil == 1 or 2) and (c_laboral==2) and (age > 65):
    print("su subsidio de agua es de: 95.000") 

elif (quintil == 1 or 2) and (c_laboral==2):
    print("su subsidio de agua es de: 70.000")

elif (quintil == 1 or 2) and (c_laboral==1) and (age > 65):
    print("su subsidio de agua es de: 85.000") 

elif (quintil == 1 or 2) and (c_laboral==1):
    print("su subsidio de agua es de: 60.000")

 #quintil 3

elif (quintil == 3) and (c_laboral==2) and (age > 65):
    print("su subsidio de agua es de 60.000")

elif (quintil == 3) and (c_laboral==2):
    print("su subsidio de agua es de 35.000")

elif (quintil == 3) and (c_laboral==1) and (age > 65):
    print("su subsidio de agua es de 50.000")

elif (quintil == 3) and (c_laboral==1):
    print("su subsidio de agua es de 25.000")

else:
    print("ud no tiene subsidio de agua")

