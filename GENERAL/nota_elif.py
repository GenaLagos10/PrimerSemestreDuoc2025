print("verificacion de acceso")

nota_alumno=float(input("introduce tu nota, por favor: "))

if nota_alumno<4:
    print("insuficiente")
elif nota_alumno<5:
    print("suficiente")
elif nota_alumno<6:
    print("bien")
elif nota_alumno<7:
    print("muy bien!")
elif nota_alumno==7:
    print("excelente!!")
else:
    print("nota fuera de rango")

