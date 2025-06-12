
temperaturas_lista = [25.5, 27.0, 23.8, 29.1, 26.5, 24.0, 28.3, 29.8, 22.4, 30.2]
umbra = 24
def calcular_promedio_temperaturas(temperaturas_lista):
    suma_total=0
    for temperatura_individual in (temperaturas_lista):
        suma_total+=temperatura_individual
        
    if len(temperaturas_lista) >0:
        promedio= suma_total/len(temperaturas_lista)
    else:
        promedio = 0
    return promedio
    
semana1 = calcular_promedio_temperaturas(temperaturas_lista)
print(semana1)
print(max(temperaturas_lista))
print(min(temperaturas_lista))

def calcular_umbral():
    sobre_umbral=0
    for temperatura_i in temperaturas_lista:
        if temperatura_i > 24:
            sobre_umbral+=1
            
    print(f"Los días de temperaturas sobre el umbral fueron: {sobre_umbral}")
        
calcular_umbral()


