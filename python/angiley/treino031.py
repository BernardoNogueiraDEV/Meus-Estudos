valores = tuple(int(input(f"Digite o valor {i+1}: ")) for i in range(4))

quantidade_nove = valores.count(9)

posicao_um = valores.index(1) + 1 if 1 in valores else "não encontrado"

numeros_pares = tuple(num for num in valores if num % 2 == 0)

print(f"\nQuantidade de vezes que o valor 9 apareceu: {quantidade_nove}")
print(f"Posição em que o valor 1 foi digitado: {posicao_um}")
print(f"Números pares digitados: {numeros_pares}")
