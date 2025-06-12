lista_frases1 = [
    "Hola mundo, este es un ejemplo de texto.",
    "Python es un lenguaje de programación muy versátil.",
    "Las funciones nos ayudan a organizar nuestro código.",
    "Este ejercicio es divertido."
]

def contar_total_palabras(lista_frases):
    total_palabras=0
    for frase in lista_frases:
       total_palabras += len(frase.split())
    return total_palabras
    
contador_final=contar_total_palabras(lista_frases1)
print(contador_final)
