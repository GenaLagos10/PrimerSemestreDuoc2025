def analizar_numeros(lista_de_numeros):
  
    # Calculamos los valores usando las funciones incorporadas de Python
    suma = sum(lista_de_numeros)
    promedio = suma / len(lista_de_numeros)
    numero_mas_grande = max(lista_de_numeros)
    numero_mas_pequeno = min(lista_de_numeros)

    # Retornamos los cuatro valores como una tupla
    return suma, promedio, numero_mas_grande, numero_mas_pequeno

# --- Ejemplos de uso ---

# Ejemplo 1: Lista con números
mi_lista_ejemplo = [10, 20, 5, 15, 25]

# Llamamos a la función y "desempaquetamos" la tupla de resultados
suma, promedio, mas_grande, mas_pequeno = analizar_numeros(mi_lista_ejemplo)

print("--- Análisis de Números ---")
print(f"Lista: {mi_lista_ejemplo}")
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
print(f"Número más grande: {mas_grande}")
print(f"Número más pequeño: {mas_pequeno}")

print("\n" + "="*30 + "\n") # Separador para los ejemplos

# Ejemplo 2: Lista vacía
lista_vacia = []

# Llamamos a la función con la lista vacía
suma_vacia, promedio_vacio, mas_grande_vacio, mas_pequeno_vacio = analizar_numeros(lista_vacia)

print("--- Análisis de Números (Lista Vacía) ---")
print(f"Lista: {lista_vacia}")
print(f"Suma: {suma_vacia}")
print(f"Promedio: {promedio_vacio}")
print(f"Número más grande: {mas_grande_vacio}")
print(f"Número más pequeño: {mas_pequeno_vacio}")