

total_cuenta=float(input("ingrese el monto total de la cuenta: "))
numero_personas=int(input("ingrese el numero total de personas (con numero): "))
propina=int(input("que porcentaje de propina deseas dejar? (10/15/20/otro)"))

monto_propina=total_cuenta* (propina/100)

print("el monto de la propina es: ", monto_propina)

cuentaypropina=total_cuenta+monto_propina
print("el monto de la cuenta mas la propina es: ", cuentaypropina)

monto_personas= cuentaypropina / 4
print("el monto que cada persona debe pagar es de: ", monto_personas)

