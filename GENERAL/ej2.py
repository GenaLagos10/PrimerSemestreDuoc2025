# Paso 1: Inicializar la lista vacía y la variable para la suma
numbers_list = []
sum = 0

# Paso 2: Pedir al usuario el número de elementos en la lista
list_length = int(input("Enter the number of elements in the list: "))

# Paso 3: Recoger los números y sumar solo los pares
while len(numbers_list) < list_length:  
# Continuamos pidiendo números hasta tener la lista completa
    value = int(input("Enter a number: "))
    if value % 2 == 0:  # Verificar si el número es par
        sum += value  # Sumar el número par a la variable sum
    numbers_list.append(value)  # Agregar el número a la lista

# Paso 4: Mostrar la suma de los números pares
print(f"The sum of the even numbers in the list {numbers_list} is: {sum}")