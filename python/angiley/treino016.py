# Solicitar dois números do usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Determinar o menor e o maior número
if numero1 < numero2:
    menor = numero1
    maior = numero2
else:
    menor = numero2
    maior = numero1

# Encontrar todos os números pares entre os dois números fornecidos
numeros_pares = [num for num in range(menor + 1, maior) if num % 2 == 0]

# Exibir os números pares encontrados
print(f"Os números pares entre {menor} e {maior} são:")
for numero in numeros_pares:
    print(numero)

# Calcular a soma dos números pares
soma_pares = sum(numeros_pares)
print(f"A soma de todos os números pares entre {menor} e {maior} é: {soma_pares}")
