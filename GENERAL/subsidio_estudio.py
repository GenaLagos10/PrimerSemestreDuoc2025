
decil=int(input("ingresa tu decil 1/2/3/4: "))
promedio=float(input("ingresa tu promedio: "))

arancel=2200000
matricula=95000


if (decil==1) or (decil==2) and promedio > 6.5:
    arancel= arancel - (arancel*0.25)

elif (decil==1) or (decil==2) and 5.5 < promedio <= 6.5:
    arancel= arancel - (arancel*0.15)


if (decil==3) or (decil==4) and promedio > 6.5:
    arancel= arancel - (arancel*0.18)

elif (decil==3) or (decil==4) and 5.5 < promedio <= 6.5:
    arancel= arancel - (arancel*0.12)

if (decil==1) or (decil==2) or (decil==3) and promedio > 6.0:
    matricula=matricula -(matricula * 0.175)

elif (decil==1) or (decil==2) or (decil==3):
    matricula=matricula -(matricula * 0.12)


print(f"el valor de su arancel es de: {arancel}")
print(f"el valor de su matricula es de: {matricula}")

