import random

#lista elecciones válidas en cachipun
lista=["piedra", "papel", "tijera"]

#diccionario con victorias en el juego
victorias = {
    "piedra": "tijera",
    "papel": "piedra",
    "tijera": "papel"
}

#input p1 vs bot
while True:
    print("Ca- chi- pun!!")

    player1=input("escoge: 'piedra', 'papel' o 'tijera': ").lower()
    player2=random.choice(lista)
    
    if player1 not in ("piedra", "papel", "tijera"):
        print("ingresa un valor válido")
        continue
    else:
        break

#resultaos

print(f"el player 1 ha elegido {player1}")
print(f"el player 2 ha elegido {player2}")

if player1 == player2:
    resultado="Empate"

elif victorias.get(player1) == player2:
    resultado="El player 1 gana"

else:
    resultado="El player 2 gana"

print(f"el resultado es: {resultado}!!")


