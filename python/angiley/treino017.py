# Definir o intervalo de números
inicio = 20
fim = 100

# Calcular a soma dos números ímpares no intervalo
soma_impares = sum(num for num in range(inicio, fim + 1) if num % 2 != 0)

# Exibir o resultado
print(f"A soma de todos os números ímpares entre {inicio} e {fim} é: {soma_impares}")
