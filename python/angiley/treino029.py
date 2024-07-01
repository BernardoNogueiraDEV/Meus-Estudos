import random

# Gera 5 números aleatórios e coloca em uma tupla
numeros = tuple(random.randint(1, 100) for _ in range(5))

# Mostra a listagem de números gerados
print("Números gerados:", numeros)

# Indica o menor e o maior número
menor = min(numeros)
maior = max(numeros)

print("Menor número:", menor)
print("Maior número:", maior)
