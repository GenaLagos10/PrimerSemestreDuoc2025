def analizar_temperaturas(lista_temperaturas):
    """
    Analiza una lista de temperaturas diarias para determinar:
    - Cuántos días fueron calurosos (temperatura > 24.0°C).
    - Cuántos días fueron fríos (temperatura < 19.0°C).
    - La temperatura promedio general.

    Args:
        lista_temperaturas (list): Una lista de números (enteros o flotantes)
                                   representando temperaturas.

    Returns:
        tuple: Una tupla con (dias_calurosos, dias_frios, temperatura_promedio).
               Retorna (0, 0, 0.0) si la lista de temperaturas está vacía.
    """
    # Manejar el caso de una lista vacía para evitar errores de división por cero
    if not lista_temperaturas:
        return 0, 0, 0.0

    # Umbrales definidos
    UMBRAL_CALOR = 24.0
    UMBRAL_FRIO = 19.0

    # Inicializar contadores y sumador
    dias_calurosos = 0
    dias_frios = 0
    suma_temperaturas = 0

    # Bucle para recorrer cada temperatura en la lista
    for temperatura in lista_temperaturas:
        # Sumar la temperatura actual para calcular el promedio al final
        suma_temperaturas += temperatura

        # Condicional para días calurosos
        if temperatura > UMBRAL_CALOR:
            dias_calurosos += 1

        # Condicional para días fríos
        if temperatura < UMBRAL_FRIO:
            dias_frios += 1

    # Calcular la temperatura promedio después de recorrer todos los números
    temperatura_promedio = suma_temperaturas / len(lista_temperaturas)

    # Retornar los resultados
    return dias_calurosos, dias_frios, temperatura_promedio

# --- Parte principal del programa: Definir datos y llamar a la función ---

# Ejemplo 1: Lista de temperaturas de una semana
temperaturas_semanales = [22.5, 18.0, 25.3, 19.5, 17.8, 28.1, 21.0]

# Llamar a la función y desempaquetar los resultados
calurosos, frios, promedio = analizar_temperaturas(temperaturas_semanales)

# Imprimir los resultados del primer ejemplo
print("Análisis de Temperaturas Semanales:")
print(f"Temperaturas registradas: {temperaturas_semanales}")
print(f"Días calurosos (> {UMBRAL_CALOR}°C): {calurosos}")
print(f"Días fríos (< {UMBRAL_FRIO}°C): {frios}")
print(f"Temperatura promedio semanal: {promedio:.2f}°C") # Formateamos a 2 decimales

print("\n" + "="*40 + "\n") # Separador

# Ejemplo 2: Probar con una lista vacía
temperaturas_vacias = []
calurosos_v, frios_v, promedio_v = analizar_temperaturas(temperaturas_vacias)

# Imprimir los resultados del segundo ejemplo
print("Análisis de Temperaturas (Lista Vacía):")
print(f"Temperaturas registradas: {temperaturas_vacias}")
print(f"Días calurosos (> {UMBRAL_CALOR}°C): {calurosos_v}")
print(f"Días fríos (< {UMBRAL_FRIO}°C): {frios_v}")
print(f"Temperatura promedio semanal: {promedio_v:.2f}°C")