print("***GENERADOR DE EMAILS***")

# nombre completo del usuario
name = " Genaro Lagos Nuñez "
print(f"nombre usuario {name}")

nombre_normalizado = name.strip()
nombre_normalizado = nombre_normalizado.replace(" ", ".")
nombre_normalizado = nombre_normalizado.lower()
print(f"nombre usuario normalizado: {nombre_normalizado}")

#DATOS DE LA EMPRESA
nombre_empresa = " Aquaexpert "
print(f"Nombre de la empresa {nombre_empresa}")
nombre_empresa_n2 = nombre_empresa.strip()
nombre_empresa_n2 = nombre_empresa_n2.lower()
print(nombre_empresa_n2)

#DOMINIO
extension_dominio = ".cl"
print(f"extension del dominio: {extension_dominio}")
extension_dominio_n = extension_dominio.strip().lower()
extension_dominio_n = f"@{nombre_empresa_n2}{extension_dominio_n}"

email = f"{nombre_normalizado}{extension_dominio_n}"
print(f"Email:  {email}")
