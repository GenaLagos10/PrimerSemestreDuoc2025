total=float(input("ingrese el total de su compra: "))
productos=int(input("ingrese la cantidad de productos: "))
cliente=input("ingrese si es cliente nuevo o frecuente (nuevo/frecuente)")

if cliente == "frecuente":
    descuento_cliente= 0.10

else:
    descuento_cliente= 0.05

descuento_cliente_total= total * descuento_cliente
print(f"su descuento por ser nuestro cliente es de {descuento_cliente_total}")

if productos > 5:
    descuento_productos=0.03

else:
    descuento_productos=0

descuento_productos_total = total * descuento_productos
print(f"su descuento por cantidad de productos es de: {descuento_productos_total}")


#descuento final
descuento_final= descuento_productos_total+descuento_cliente_total

descuento_maximo=total*0.25
if descuento_final > descuento_maximo:
    descuento_final = descuento_maximo

precio_final_final=total-descuento_final
print(f"su monto total a pagar es de: {precio_final_final:.2f}")