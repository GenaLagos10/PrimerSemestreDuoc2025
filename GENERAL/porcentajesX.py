
quintil=int(input("ingrese el quintil al que pertenece (1/2/3/4/5): "))
condicion_laboral=input("ingrese su condicion laboral (empleado/desempleado): ")
edad=int(input("ingrese su edad: "))
suma=0

if (quintil==1) or (quintil==2):
    suma+= 60000             
if (quintil==3):
    suma+= 25000
if (condicion_laboral=="desempleado") and (quintil==1) or (quintil==2) or (quintil==3):
    suma+=10000
if edad > 65:
    suma+=25000
print(f"su bono es de: {suma} pesos")

