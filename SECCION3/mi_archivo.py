import json

try:
    # Abre el archivo 'datos.json' en modo lectura ('r')
    with open('datos.json', 'r', encoding='utf-8') as archivo_json:
        # Carga el contenido JSON del archivo a un diccionario de Python
        datos = json.load(archivo_json)

        # Accede a los valores por sus claves y los imprime
        nombre = datos["nombre"]
        edad = datos["edad"]

        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")

except FileNotFoundError:
    print("¡Error! El archivo 'datos.json' no fue encontrado.")
except json.JSONDecodeError:
    print("¡Error! El archivo 'datos.json' no tiene un formato JSON válido.")
except KeyError as e:
    print(f"¡Error! Falta la clave esperada en el JSON: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")