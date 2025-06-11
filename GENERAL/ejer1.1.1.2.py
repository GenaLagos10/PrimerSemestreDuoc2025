
total=float(input("ingrese el monto total de la compra: "))
Nproductos=int(input("digite con numeros la cantidad de productos que lleva: "))
cliente=input("escriba si ud es cliente nuevo o frecuente (nuevo/frecuente): ").lower()

#calculamos descuento por cliente nuevo o frecuente
if cliente == "frecuente":
    descuento_cliente = 0.10  # 10% para clientes frecuentes
else:
    descuento_cliente = 0.05  # 5% para nuevos clientes


#variable de monto descuento por cliente y se muestra el descuento al cliente
monto_descuento= total * descuento_cliente
print(f"tienes un descuento de {monto_descuento} USD por ser cliente")


#calculamos descuento adicional por productos comprados
if Nproductos > 5:
    descuento_adicional=0.03
else:
    descuento_adicional=0
      
#variable de monto de descuento adicional y print de descuento adicional
monto_descuento_adicional= total * descuento_adicional
print(f"tienes un descuento de {monto_descuento_adicional} USD por cantidad de productos")


#variable de la suma de ambos descuentos, de cliente y de cantidad de productos
descuento_total=monto_descuento + monto_descuento_adicional

#limitar a 25pc de dc
descuento_maximo= total*0.25
if descuento_total > descuento_maximo:
    descuento_total= descuento_maximo


print(f"su descuento total es de: {descuento_total} USD")
print(f"el precio final a pagar es de: {total - descuento_total} USD")

