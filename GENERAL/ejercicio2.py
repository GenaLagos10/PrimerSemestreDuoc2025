def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Ejemplo de uso
numero = int(input("Introduce un número para saber si es primo: "))
if es_primo(numero):
    print(f"el {numero} sí es un numero primo.")
else:
    print(f"el {numero} no es un numero primo.")